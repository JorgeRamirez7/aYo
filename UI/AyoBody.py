from LanguagesWindow import LanguagesWindow
from PyQt5 import QtWidgets, uic
from SettingsWindow import SettingsWindow


class AyoBody(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(AyoBody, self).__init__()
        uic.loadUi("Main\\AyoBody.ui", self)
        self.w = None
        self.parent = parent

        self.exitBtn.clicked.connect(self.exit)
        self.startBtn.clicked.connect(self.listening_activated)
        self.supportedBtn.clicked.connect(self.view_languages)
        self.settingsBtn.clicked.connect(self.settings)

    def listening_activated(self):
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
