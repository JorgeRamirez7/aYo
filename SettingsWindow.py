from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class SettingsWindow(QWidget):
    #Settings page
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("Main\\settings.ui", self)

        self.parent = parent

        
        self.modeToggle.currentIndexChanged.connect(self.change_mode)
        self.secondsBox.valueChanged.connect(self.duration_change)
        self.addLanguageBtn.clicked.connect(self.add_language)
        self.yesRadioBtn.toggled.connect(self.on_startup)
        self.linkBtn.clicked.connect(self.link_spotify)
        self.returnBtn.clicked.connect(self.return_home)

    def change_mode(self):
        print("Mode Placeholder")
    
    def duration_change(self):
        print("Duration Placeholder")

    def add_language(self):
        print("Language Placeholder")

    def on_startup(self):
        print("startup on Placeholder")
    
    def link_spotify(self):
        print("link Placeholder")

    def return_home(self):
        self.parent.show()
        self.close()
        