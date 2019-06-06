# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLIS.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from speech_recog import recognize_speech_from_mic
import speech_recognition as sr
from camera import *
from os import path
from pydub import AudioSegment

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

class ImagePlayer(QWidget):
    def __init__(self, filename, title, parent=None):
        QWidget.__init__(self, parent)

        # Load the file into a QMovie
        self.movie = QMovie(filename, QByteArray(), self)

        size = self.movie.scaledSize()
        self.setGeometry(200, 200, 486, 240)
        self.setWindowTitle(title)

        self.movie_screen = QLabel()
        # Make label fit the gif
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        # Create the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo_tn.png'))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.VIDEO = QtGui.QWidget()
        self.VIDEO.setObjectName(_fromUtf8("VIDEO"))
        self.gridLayout_7 = QtGui.QGridLayout(self.VIDEO)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_4 = QtGui.QLabel(self.VIDEO)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_12.addWidget(self.label_4)
        self.import_video = QtGui.QPushButton(self.VIDEO)
        self.import_video.setObjectName(_fromUtf8("import_video"))
        self.verticalLayout_12.addWidget(self.import_video)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.video_frame = QtGui.QFrame(self.VIDEO)
        self.video_frame.setMinimumSize(QtCore.QSize(480, 250))
        self.video_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.video_frame.setObjectName(_fromUtf8("video_frame"))
        self.horizontalLayout_10.addWidget(self.video_frame)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_5 = QtGui.QLabel(self.VIDEO)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_13.addWidget(self.label_5)
        self.start_recording_video = QtGui.QPushButton(self.VIDEO)
        self.start_recording_video.setObjectName(_fromUtf8("start_recording_video"))
        ######################################################
        self.start_recording_video.clicked.connect(self.camera_start)
        ######################################################
        self.verticalLayout_13.addWidget(self.start_recording_video)
        self.connection_label3 = QtGui.QLabel(self.VIDEO)
        self.connection_label3.setObjectName(_fromUtf8("connection_label3"))
        self.verticalLayout_13.addWidget(self.connection_label3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.textBrowser_video = QtGui.QTextBrowser(self.VIDEO)
        self.textBrowser_video.setObjectName(_fromUtf8("textBrowser_video"))
        ######################################################
        self.textBrowser_video.setReadOnly(True)
        ######################################################
        self.horizontalLayout_7.addWidget(self.textBrowser_video)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.gridLayout_7.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.import_audio = QtGui.QPushButton(self.AUDIO)
        self.import_audio.setObjectName(_fromUtf8("import_audio"))
        self.import_audio.clicked.connect(self.transcribe)
        self.verticalLayout_8.addWidget(self.import_audio)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        gif = "audio_loader.gif"
        player =ImagePlayer(gif,"Record")
        self.graphicsView_audio=player
        self.graphicsView_audio.setObjectName(_fromUtf8("graphicsView_audio"))
        self.horizontalLayout_9.addWidget(self.graphicsView_audio)
        self.horizontalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_7 = QtGui.QLabel(self.AUDIO)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_14.addWidget(self.label_7)
        self.start_recording_audio = QtGui.QPushButton(self.AUDIO)
        self.start_recording_audio.setObjectName(_fromUtf8("start_recording_audio"))
        ###########################################################
        self.start_recording_audio.clicked.connect(self.record)
        ###########################################################
        self.verticalLayout_14.addWidget(self.start_recording_audio)
        self.connection_label2 = QtGui.QLabel(self.AUDIO)
        self.connection_label2.setObjectName(_fromUtf8("connection_label2"))
        self.verticalLayout_14.addWidget(self.connection_label2)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.textBrowser_audio = QtGui.QTextBrowser(self.AUDIO)
        ######################################################
        self.textBrowser_audio.setReadOnly(True)
        ######################################################
        self.textBrowser_audio.setObjectName(_fromUtf8("textBrowser_audio"))
        self.horizontalLayout_4.addWidget(self.textBrowser_audio)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.AUDIO, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuConnection = QtGui.QMenu(self.menubar)
        self.menuConnection.setObjectName(_fromUtf8("menuConnection"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionStatus = QtGui.QAction(MainWindow)
        self.actionStatus.setObjectName(_fromUtf8("actionStatus"))
        self.menuFile.addAction(self.actionClose)
        self.menuConnection.addAction(self.actionStatus)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "RECORD VIDEO OR IMPORT VIDEO", None))
        self.import_video.setText(_translate("MainWindow", "         IMPORT MEDIA           ", None))
        self.label_5.setText(_translate("MainWindow", "RECORDING OPTIONS", None))
        self.start_recording_video.setText(_translate("MainWindow", "START RECORDING", None))
        self.connection_label3.setText(_translate("MainWindow", " ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VIDEO), _translate("MainWindow", "VIDEO", None))
        self.label_2.setText(_translate("MainWindow", "RECORD AUDIO OR IMPORT AUDIO", None))
        self.import_audio.setText(_translate("MainWindow", "         IMPORT MEDIA           ", None))
        self.label_7.setText(_translate("MainWindow", "RECORDING OPTIONS", None))
        self.start_recording_audio.setText(_translate("MainWindow", "START RECORDING", None))
        self.connection_label2.setText(_translate("MainWindow", " ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AUDIO), _translate("MainWindow", "AUDIO", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        ######################################################
        self.actionAbout.setStatusTip('About Sign Language Interpretation System')
        ######################################################
        self.actionAbout.setShortcut(_translate("MainWindow", "F1", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        ######################################################
        self.actionClose.setStatusTip('Leave the App')
        self.actionClose.triggered.connect(self.close_application)
        ######################################################
        self.actionStatus.setText(_translate("MainWindow", "Status", None))
        self.actionStatus.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        ######################################################
        self.actionStatus.setStatusTip('Check Connection')
        ######################################################
        MainWindow.statusBar()

    def close_application(self):
        choice = QtGui.QMessageBox.question(MainWindow,'Extract!',"Close Application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def record(self):
        self.start_recording_audio.setEnabled(False)
        # create recognizer and mic instances
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        speech = recognize_speech_from_mic(recognizer, microphone)
        if speech["transcription"]:
            # show the user the transcription
            print("You said: {}".format(speech["transcription"]))
            self.send_audio_text(speech["transcription"])
        elif not speech["success"]:
            print("I didn't catch that. Hit Start Record Again Please\n")
            choice = QtGui.QMessageBox.question(MainWindow,'Recording Error!!',"I didn't catch that. Please Hit Start Record Button Again and Begin Speaking", QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        elif speech["error"]:
            print("ERROR: {}".format(speech["error"]))
            choice = QtGui.QMessageBox.question(MainWindow,'Recording Error!!',"ERROR: {} Please, Check your Network Connection or Hit Start Record Button Again and Begin Speaking".format(speech["error"]), QtGui.QMessageBox.Yes)
            if choice == QtGui.QMessageBox.Yes:
                pass
        self.start_recording_audio.setEnabled(True)


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

    def send_video_text(self):
        
        text="hi"
        font=self.textBrowser_video.font()
        font.setPointSize(13)
        self.textBrowser_video.setFont(font)
        textFormatted='{:>120}'.format(text)
        #self.textBrowser_video.append(textFormatted)
        #tcpClientA.send(text.encode())
        self.textBrowser_video.append(text)
        #self.chatTextField.setText("")

    
    def transcribe(self):
        self.import_audio.setEnabled(False)
        # convert mp3 file to wav     
        # transcribe audio file 
        try:
            name = QtGui.QFileDialog.getOpenFileName(MainWindow,'Open File','audio','Audio Files(*.mp3 *.wav)')    
            sound = AudioSegment.from_mp3(name)
            sound.export("audio.wav", format="wav")                                                    
            AUDIO_FILE = "audio.wav"

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

    def camera_start(self):

        filename = 'video.avi'
        frames_per_second = 60.0
        res = '480p'

        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

        while True:
            ret, frame = cap.read()
            out.write(frame)
            
            cv2.imshow('Recording... (PLEASE PRESS q TO STOP THE RECORDING)',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

