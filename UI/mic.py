from threading import *
from time import sleep
class Record(Thread):
    def run(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        speech = recognize_speech_from_mic(recognizer, microphone)
        if speech["transcription"]:
            # show the user the transcription
            self.send_audio_text(speech["transcription"])
        elif not speech["success"]:
            choice = QtGui.QMessageBox.question(MainWindow,'Recording Error!!',"I didn't catch that. Please Hit Start Record Button Again and Begin Speaking", QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        elif speech["error"]:
            choice = QtGui.QMessageBox.question(MainWindow,'Recording Error!!',"ERROR: {} Please, Check your Network Connection or Hit Start Record Button Again and Begin Speaking".format(speech["error"]), QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        self.start_recording_audio.setEnabled(True)
        # self.horizontalLayout_9.removeWidget(self.graphicsView_audio)
        # self.graphicsView_audio = QtGui.QLabel(self.AUDIO)
        # self.graphicsView_audio.setObjectName(_fromUtf8("graphicsView_audio"))
        # #label_Image = QtGui.QLabel(frame)
        # image_pathss = 'images/1.png' #path to your image file
        # image_profiless = QtGui.QImage(image_pathss) #QImage object# To scale image for example and keep its Aspect Ration    
        # self.graphicsView_audio.setPixmap(QtGui.QPixmap.fromImage(image_profiless)) 
        # self.horizontalLayout_9.addWidget(self.graphicsView_audio)
        

class RecordSwitch(Thread):
    def run(self):
        self.start_recording_audio.setEnabled(False)
        
        self.horizontalLayout_9.removeWidget(self.graphicsView_audio)

        self.graphicsView_audio = QtGui.QLabel(self.AUDIO)
        self.graphicsView_audio.setObjectName(_fromUtf8("graphicsView_audio"))
        #label_Image = QtGui.QLabel(frame)
        image_paths = 'images/2.png' #path to your image file
        image_profiles = QtGui.QImage(image_paths) #QImage object# To scale image for example and keep its Aspect Ration    
        self.graphicsView_audio.setPixmap(QtGui.QPixmap.fromImage(image_profiles)) 
        self.horizontalLayout_9.addWidget(self.graphicsView_audio)
        # create recognizer and mic instances

