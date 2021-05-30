import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
overdir = os.path.dirname(parentdir)
sys.path.append(overdir)

#from main import main
from .languages_window import LanguagesWindow
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, QThreadPool
from .settings_window import SettingsWindow
from .worker import Worker


class AyoBody(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(AyoBody, self).__init__()
        uic.loadUi("ui\\ui_files\\aYo_body.ui", self)
        self.w = None
        self.parent = parent

        self.exitBtn.clicked.connect(self.exit)
        self.startBtn.clicked.connect(self.listening_activated)
        self.supportedBtn.clicked.connect(self.view_languages)
        self.settingsBtn.clicked.connect(self.settings)

        self.threadpool = QThreadPool()

      #  print("overdirectory = " + overdir)
        
    def listening_activated(self):
        #main.main()
        print("activation Placeholder")

    def view_languages(self):
        self.w = None
        self.w = LanguagesWindow()
        self.w.show()
        

    def settings(self):
        self.w = None
        self.w = SettingsWindow(self)
        self.w.show()
        self.hide()

    def exit(self):
        self.parent.show()
        quit()
