
from .languages_window import LanguagesWindow
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, QThreadPool, QTimer
from .query_worker import QueryWorker
from .settings_window import SettingsWindow
#from .worker import Worker


class AyoBody(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(AyoBody, self).__init__()
        uic.loadUi("ui\\ui_files\\aYo_body.ui", self)
        self.w = None
        self.parent = parent

        self.timer = QTimer()
        
        self.timer.timeout.connect(self.enable_button)
        self.exitBtn.clicked.connect(self.exit)
        self.startBtn.clicked.connect(self.listening_activated)
        self.supportedBtn.clicked.connect(self.view_languages)
        self.settingsBtn.clicked.connect(self.settings)

        self.threadpool = QThreadPool()

        self.threadStarted = False

      #  print("overdirectory = " + overdir)
        
    def listening_activated(self):
        if (self.threadStarted == False):
            self.thread = QThread()

            self.worker = QueryWorker()

            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()

            self.threadStarted = True

            self.startBtn.setText("Stop")
            
        elif (self.threadStarted == True):
            self.worker.stop()
            self.threadStarted = False

            #change the start/stop button stylesheet to look disabled.
            self.startBtn.setEnabled(False)
            self.startBtn.setText("Please Wait...")
            self.startBtn.setStyleSheet(
                "QPushButton{\
                    background-color: #0F4C75;\
                    color: darkgray;\
                    border-style: outset;\
                    border-width: 2px;\
                    border-radius: 10px;\
                    border-color: black;\
                    min-width: 10em;\
                    padding: 6px;\
                }\
                \
                QPushButton:hover{\
                    border-color: lightgray;\
                    background-color: rgb(60, 158, 223);\
                }\
                \
                QPushButton:pressed {\
                    background-color: #0F4C75;\
                    border-style: inset;\
                }"
            )#end Stylesheet edit

            self.timer.start(6000)

    def view_languages(self):
        self.w = None
        self.w = LanguagesWindow()
        self.w.show()
        

    def settings(self):
        self.w = None
        #self.w = SettingsWindow(self)
        #self.w.show()
        #self.hide()

    def enable_button(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.startBtn.setText("Start")

        self.startBtn.setStyleSheet(
                "QPushButton{\
                    background-color: #3282B8;\
                    color: rgb(228,240,237);\
                    border-style: outset;\
                    border-width: 2px;\
                    border-radius: 10px;\
                    border-color: black;\
                    min-width: 10em;\
                    padding: 6px;\
                }\
            \
                QPushButton:hover{\
                    border-color: lightgray;\
                    background-color: rgb(60, 158, 223);\
                }\
            \
                QPushButton:focus{\
                    border-color: lightgray;\
                    background-color: rgb(60, 158, 223);\
                }\
            \
                QPushButton:pressed {\
                    background-color: #0F4C75;\
                    border-style: inset;\
                }"
            ) #end stylesheet edit

    def exit(self):
        self.parent.show()
        quit()
