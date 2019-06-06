# encoding: utf-8
"""
@author: Akampurira Rugumambaju Mark
@contact: akamps.mark@gmail.com
"""

import requests
import argparse
import cv2

# Initialize the PyTorch REST API endpoint URL.
PyTorch_REST_API_URL = 'http://127.0.0.1/predict'


def predict_result(video_path):
    # Initialize image path
    
    #video = bytearray(video)
    payload = {'video': open(video_path, 'rb')}

    # Submit the request.
    r = requests.post(PyTorch_REST_API_URL, files=payload, stream=True).json()
    

    # Ensure the request was successful.
    if r['success']:
        # Loop over the predictions and display them.
        for (i, result) in enumerate(r['predictions']):
            print('{}. {}: {:.4f}'.format(i + 1, result['label'],
                                          result['probability']))
    # Otherwise, the request failed.
    else:
        print('Request failed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classification demo')
    parser.add_argument('--file', type=str, help='test image file')

    args = parser.parse_args()
    predict_result(args.file)
