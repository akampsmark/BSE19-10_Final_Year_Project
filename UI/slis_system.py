# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLIS.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from camera import *
from os import path
import time
from threading import *
from pydub import AudioSegment
import queue

import cv2
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Speeech(Thread):
    def run(self, my_queue):
        from speech_recog import recognize_speech_from_mic
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        speech = recognize_speech_from_mic(recognizer, microphone)
        if speech["transcription"]:
            # show the user the transcription
            print("hi")
            return "transcription"
        elif not speech["success"]:
            print("hi")
            return "success"
        elif speech["error"]:
            print("hi")
            return "error"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon('images/logo_tn.png'))
        MainWindow.resize(889, 712)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.stop=True
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("font:rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background: rgb(165, 165, 165);\n"
"font: bold 11pt \"Calibri\";"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.VIDEO = QtGui.QWidget()
        self.VIDEO.setObjectName(_fromUtf8("VIDEO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.VIDEO)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.line_2 = QtGui.QFrame(self.VIDEO)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_11.addWidget(self.line_2)
        self.label = QtGui.QLabel(self.VIDEO)
        self.label.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_11.addWidget(self.label)
        self.line = QtGui.QFrame(self.VIDEO)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_11.addWidget(self.line)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.textBrowser_video = QtGui.QTextBrowser(self.VIDEO)
        ######################################################
        self.textBrowser_video.setReadOnly(True)
        ######################################################
        self.textBrowser_video.setStyleSheet(_fromUtf8("border-radius: 24px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Times New Roman\";"))
        self.textBrowser_video.setObjectName(_fromUtf8("textBrowser_video"))
        self.horizontalLayout_7.addWidget(self.textBrowser_video)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.gridLayout_7.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_4 = QtGui.QLabel(self.VIDEO)
        self.label_4.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";"))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_12.addWidget(self.label_4)
        self.import_video = QtGui.QPushButton(self.VIDEO)
        self.import_video.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"font: 75 bold 11pt \"Calibri\";\n"
"  border-radius: 12px;\n"
"  padding: 8px 8px;\n"
"  background: grey;"))
        self.import_video.setObjectName(_fromUtf8("import_video"))
        self.verticalLayout_12.addWidget(self.import_video)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_12.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        #########################################################################################
        self.graphicsView_video = QtGui.QLabel(self.VIDEO)
        self.graphicsView_video.setObjectName(_fromUtf8("graphicsView_video"))
        image_path = 'images/1.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object  
        self.graphicsView_video.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
        ##########################################################################################
        self.horizontalLayout_10.addWidget(self.graphicsView_video)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_5 = QtGui.QLabel(self.VIDEO)
        self.label_5.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";\n"
"text-align: center;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_13.addWidget(self.label_5)
        self.start_recording_video = QtGui.QPushButton(self.VIDEO)
        self.start_recording_video.setStyleSheet(_fromUtf8("background-color: red;\n"
"font: 75 bold 16pt \"Calibri\";\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
" border-radius:24px;"))
        self.start_recording_video.setObjectName(_fromUtf8("start_recording_video"))
        ######################################################
        self.start_recording_video.clicked.connect(self.camera_start)
        ######################################################
        self.verticalLayout_13.addWidget(self.start_recording_video)
        self.stop_recording = QtGui.QPushButton(self.VIDEO)
        self.stop_recording.setStyleSheet(_fromUtf8("background-color: green;\n"
"font: 75 bold 16pt \"Calibri\";\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 50px;\n"
" border-radius:12px;"))
        self.stop_recording.setObjectName(_fromUtf8("stop_recording"))
        ######################################################
        self.stop_recording.clicked.connect(self.stopp)
        ######################################################
        self.verticalLayout_13.addWidget(self.stop_recording)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_13.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.VIDEO, _fromUtf8(""))
        self.AUDIO = QtGui.QWidget()
        self.AUDIO.setObjectName(_fromUtf8("AUDIO"))
        self.gridLayout_3 = QtGui.QGridLayout(self.AUDIO)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_2 = QtGui.QLabel(self.AUDIO)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.import_audio = QtGui.QPushButton(self.AUDIO)
        self.import_audio.setStyleSheet(_fromUtf8("border: 2px solid gray;\n"
"font: 75 bold 11pt \"Calibri\";\n"
"  border-radius: 12px;\n"
"  padding: 8px 8px;\n"
"  background: grey;"))
        self.import_audio.setObjectName(_fromUtf8("import_audio"))
        ######################################################################
        self.import_audio.clicked.connect(self.transcribe)
        ######################################################################
        self.verticalLayout_8.addWidget(self.import_audio)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.graphicsView_audio = QtGui.QLabel(self.AUDIO)
        self.graphicsView_audio.setObjectName(_fromUtf8("graphicsView_audio"))
        #label_Image = QtGui.QLabel(frame)
        image_path = 'images/1.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object# To scale image for example and keep its Aspect Ration    
        self.graphicsView_audio.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
        self.horizontalLayout_9.addWidget(self.graphicsView_audio)
        self.horizontalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_7 = QtGui.QLabel(self.AUDIO)
        self.label_7.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";\n"
"text-align: center;"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_14.addWidget(self.label_7)
        self.start_recording_audio = QtGui.QPushButton(self.AUDIO)
        self.start_recording_audio.setStyleSheet(_fromUtf8("background-color: red;\n"
"font: 75 bold 16pt \"Calibri\";\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 17px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
" border-radius:24px;"))
        self.start_recording_audio.setObjectName(_fromUtf8("start_recording_audio"))
        ###########################################################
        self.start_recording_audio.clicked.connect(self.record)
        ###########################################################
        self.verticalLayout_14.addWidget(self.start_recording_audio)
        self.connection_label2 = QtGui.QLabel(self.AUDIO)
        self.connection_label2.setText(_fromUtf8(""))
        self.connection_label2.setObjectName(_fromUtf8("connection_label2"))
        self.verticalLayout_14.addWidget(self.connection_label2)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.line_6 = QtGui.QFrame(self.AUDIO)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_4.addWidget(self.line_6)
        self.label_8 = QtGui.QLabel(self.AUDIO)
        self.label_8.setStyleSheet(_fromUtf8("font: 75 bold 11pt \"Calibri\";"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_4.addWidget(self.label_8)
        self.line_5 = QtGui.QFrame(self.AUDIO)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_4.addWidget(self.line_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.textBrowser_audio = QtGui.QTextBrowser(self.AUDIO)
        ######################################################
        self.textBrowser_audio.setReadOnly(True)
        ######################################################
        self.textBrowser_audio.setStyleSheet(_fromUtf8("border-radius: 24px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Times New Roman\";"))
        self.textBrowser_audio.setObjectName(_fromUtf8("textBrowser_audio"))
        self.horizontalLayout_4.addWidget(self.textBrowser_audio)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.AUDIO, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.setStatusTip('About Application')
        self.actionAbout.triggered.connect(self.about_sys)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClose.setStatusTip('Leave the App')
        self.actionClose.triggered.connect(self.close_application)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Language Interpretation System", None))
        self.label.setText(_translate("MainWindow", "TEXT TRANSLATION", None))
        self.label_4.setText(_translate("MainWindow", "RECORD VIDEO OR IMPORT VIDEO FOR TRANSLATION", None))
        self.import_video.setText(_translate("MainWindow", "         IMPORT MEDIA           ", None))
        self.label_5.setText(_translate("MainWindow", "RECORDING OPTIONS", None))
        self.start_recording_video.setText(_translate("MainWindow", "START RECORDING", None))
        self.stop_recording.setText(_translate("MainWindow", "STOP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VIDEO), _translate("MainWindow", "VIDEO", None))
        self.label_2.setText(_translate("MainWindow", "RECORD AUDIO OR IMPORT AUDIO FOR TRANSLATION", None))
        self.import_audio.setText(_translate("MainWindow", "         IMPORT MEDIA           ", None))
        self.label_7.setText(_translate("MainWindow", "RECORDING OPTIONS", None))
        self.start_recording_audio.setText(_translate("MainWindow", "START RECORDING", None))
        self.label_8.setText(_translate("MainWindow", "TEXT TRANSLATION", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AUDIO), _translate("MainWindow", "AUDIO", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

    def about_sys(self):
        import about
        self.dialog = QtGui.QDialog()
        self.dialog.ui = about.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(MainWindow,'Extract!',"Close Application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def camera_start(self):
        self.stop = True
        self.start_recording_video.setEnabled(False)
        self.horizontalLayout_10.removeWidget(self.graphicsView_video)

        self.graphicsView_video = QtGui.QLabel(self.VIDEO)
        self.graphicsView_video.setObjectName(_fromUtf8("graphicsView_video"))
        image_path = 'images/2.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object  
        self.graphicsView_video.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
        self.horizontalLayout_10.addWidget(self.graphicsView_video)
        ##########################################################################################
        
        dirName = 'temp'
        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            pass
        filename = 'temp/video.avi'
        frames_per_second = 60.0
        res = '480p'

        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

        while self.stop:
            ret, frame = cap.read()
            out.write(frame)
            
            cv2.imshow('Recording... (PLEASE PRESS STOP BUTTON or q on keyboard TO STOP THE RECORDING)',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.horizontalLayout_10.removeWidget(self.graphicsView_video)

                self.graphicsView_video = QtGui.QLabel(self.VIDEO)
                self.graphicsView_video.setObjectName(_fromUtf8("graphicsView_video"))
                image_path = 'images/1.png' #path to your image file
                image_profile = QtGui.QImage(image_path) #QImage object  
                self.graphicsView_video.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
                self.horizontalLayout_10.addWidget(self.graphicsView_video)
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        self.start_recording_video.setEnabled(True)

    def stopp(self):
        self.stop = False
        self.horizontalLayout_10.removeWidget(self.graphicsView_video)

        self.graphicsView_video = QtGui.QLabel(self.VIDEO)
        self.graphicsView_video.setObjectName(_fromUtf8("graphicsView_video"))
        image_path = 'images/1.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object  
        self.graphicsView_video.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
        self.horizontalLayout_10.addWidget(self.graphicsView_video)


    def record(self):
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

        my_queue = queue.Queue()

        thread1 = Thread(Speeech(my_queue))
        thread1.start()
        thread1.join()
        func_value = my_queue.get()
        self.send_audio_text(str(func_value))       
        self.start_recording_audio.setEnabled(True)
        # self.horizontalLayout_9.removeWidget(self.graphicsView_audio)
        # self.graphicsView_audio = QtGui.QLabel(self.AUDIO)
        # self.graphicsView_audio.setObjectName(_fromUtf8("graphicsView_audio"))
        # #label_Image = QtGui.QLabel(frame)
        # image_pathss = 'images/1.png' #path to your image file
        # image_profiless = QtGui.QImage(image_pathss) #QImage object# To scale image for example and keep its Aspect Ration    
        # self.graphicsView_audio.setPixmap(QtGui.QPixmap.fromImage(image_profiless)) 
        # self.horizontalLayout_9.addWidget(self.graphicsView_audio)


    def send_audio_text(self,text):
        text2 = ">>"+text
        font=self.textBrowser_audio.font()
        font.setPointSize(13)
        self.textBrowser_audio.setFont(font)
        textFormatted='{:>120}'.format(text2)
        #self.textBrowser_audio.append(textFormatted)
        #tcpClientA.send(text.encode())
        self.textBrowser_audio.append(text2)
        #self.chatTextField.setText("")

    def send_video_text(self,text):
        
        text2 = ">>"+text
        font=self.textBrowser_video.font()
        font.setPointSize(13)
        self.textBrowser_video.setFont(font)
        textFormatted='{:>120}'.format(text2)
        #self.textBrowser_video.append(textFormatted)
        #tcpClientA.send(text.encode())
        self.textBrowser_video.append(text2)
        #self.chatTextField.setText("")

    
    def transcribe(self):
        self.import_audio.setEnabled(False)
        # convert mp3 file to wav     
        # transcribe audio file 
        dirName = 'temp'
        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            pass

        try:
            name = QtGui.QFileDialog.getOpenFileName(MainWindow,'Open File','audio','Audio Files(*.mp3 *.wav)')    
            sound = AudioSegment.from_mp3(name)
            sound.export("temp/audio.wav", format="wav")                                                    
            AUDIO_FILE = "temp/audio.wav"

            # use the audio file as the audio source                                        
            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file                  

                self.send_audio_text(r.recognize_google(audio))
        except FileNotFoundError as e:
            choice = QtGui.QMessageBox.question(MainWindow,'Error!!',"ERROR: File Not Found. Please Try Again", QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        except Exception as e:
            choice = QtGui.QMessageBox.question(MainWindow,'Error!!',"An Error Occurred. Please Try Again", QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        self.import_audio.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

