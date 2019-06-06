# encoding: utf-8
"""
@author: Akampurira Rugumambaju Mark
@contact: akamps.mark@gmail.com
"""

import io
import json
from moviepy.editor import VideoFileClip
import flask
import torch
import torch
import torch.nn.functional as F
from PIL import Image
from torch import nn
from torchvision import transforms as T
import os
import re
import cv2
import functools
import subprocess
import numpy as np
import moviepy.editor as mpy
import tempfile
import torch.nn.parallel
import torch.optim
from models import TSN
from transforms import *
import datasets_video


def load_model():
    """Load the pre-trained model, you can use your model.
    """
    #Load the categories or words to which interpretations are made
    categories_file = 'model/{}_categories.txt'.format('SLIS')
    global categories
    categories = [line.rstrip() for line in open(categories_file, 'r').readlines()]
    num_class = len(categories)

    #Define The model to be loaded as weights globally    
    global model
    model = TSN(num_class,
          8,
          'RGB',
          base_model='BNInception',
          consensus_type='TRNmultiscale',
          img_feature_dim=256, print_spec=False)
    
    #Load the weight file into memory and send it to the GPU
    weights = 'model/TRN_SLIS_RGB_BNInception_TRNmultiscale_segment8_best.pth.tar'
    checkpoint = torch.load(weights)
    

    base_dict = {'.'.join(k.split('.')[1:]): v for k, v in list(checkpoint['state_dict'].items())}
    model.load_state_dict(base_dict)
    model.cuda().eval()

def extract_frames(video_file, num_frames=8):
    try:
        os.makedirs(os.path.join(os.getcwd(), 'frames'))
    except OSError:
        pass
   # Get the durtion of the uploaded video    
    clip = VideoFileClip(video_file)
    seconds = clip.duration
    
    #Calculate the frame rate at which to extract frames
    rate = num_frames / float(seconds)
    
    #extract the frames from the uploaded video
    output = subprocess.Popen(['ffmpeg', '-i', video_file,
                               '-vf', 'fps={}'.format(rate),
                               '-vframes', str(num_frames),
                               '-loglevel', 'panic',
                               'frames/%d.jpg']).communicate()
    
    frame_paths = sorted([os.path.join('frames', frame)
                          for frame in os.listdir('frames')])
    
    #Load the frames into memory for interpretation
    frames = load_frames(frame_paths)
    
    return frames

def load_frames(frame_paths, num_frames=8):
    frames = [Image.open(frame).convert('RGB') for frame in frame_paths]
    if len(frames) >= num_frames:
        return frames[::int(np.ceil(len(frames) / float(num_frames)))]
    else:
        raise ValueError('Video must have at least {} frames'.format(num_frames))



# Initialize our Flask application and the PyTorch model.
app = flask.Flask(__name__)
load_model()



# Api method to perform the interpretation
@app.route("/predict", methods=["POST"])
def predict():
    # Initialize the data dictionary that will be returned from the view.
    retdata = {"success": False}
    
    # Ensure a video was properly uploaded to our endpoint.
    if flask.request.method == 'POST':
        if flask.request.files.get("video"):
            
            # Read the video in PIL format
            video = flask.request.files["video"]

            #Create a log folder for the videos uploaded if its not already existent
            try:
                os.makedirs(os.path.join(os.getcwd(), 'SLIS-data'))
            except OSError:
                pass
            #Log the uploaded video into the folder and acquire the path to the file
            video.save(os.path.join('SLIS-data',video.filename))
            video = os.path.join('SLIS-data',video.filename)

        
            # Initialize frame transforms.
            transform = torchvision.transforms.Compose([
                GroupOverSample(model.input_size, model.scale_size),
                Stack(roll=('BNInception'.encode() in ['BNInception', 'InceptionV3'])),
                ToTorchFormatTensor(div=('BNInception'.encode() not in ['BNInception', 'InceptionV3'])),
                GroupNormalize(model.input_mean, model.input_std),
            ])

            #Extract Frames from the video
            frames = extract_frames(video, 8)

            # Make video prediction.
            data = transform(frames)
            input_var = torch.autograd.Variable(data.view(-1, 3, data.size(1), data.size(2)),
                                                volatile=True).unsqueeze(0).cuda()
            logits = model(input_var)
            h_x = torch.mean(F.softmax(logits, 1), dim=0).data
            probs, idx = h_x.sort(0, True)


            # Initialize the list of predictions to return to the client.
            retdata['predictions'] = list()

            # Loop over the results and add them to the list of returned predictions
            for i in range(0, 3):
                r = {"label": categories[idx[i]], "probability": float(probs[i])}
                retdata['predictions'].append(r)
            
            # Indicate that the request was a success.
            retdata["success"] = True

    # Return the data dictionary as a JSON response.
    return flask.jsonify(retdata)


if __name__ == '__main__':

    load_model()
    app.run(host='127.0.0.1',port=8081)
