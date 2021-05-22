from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class LanguagesWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\languages.ui", self)

        self.closeBtn.clicked.connect(self.close_window)


    def close_window(self):
        self.close()
