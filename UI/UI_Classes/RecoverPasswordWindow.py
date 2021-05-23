from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import re

class RecoverPasswordWindow(QWidget):
    #recover account ui
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\Recovery.ui", self)

        self.recoverCancelBtn.clicked.connect(self.close_window)

        self.recoverBtn.clicked.connect(self.recover_password)

        self.recoveryEmail.textEdited.connect(self.authenticate_email)

    def close_window(self):
        self.close()
    
    def recover_password(self):
        self.close()
    
    def authenticate_email(self):
        regex = '^\S+@\w+\.\w{2,3}$'
        input = self.recoveryEmail.text()
        if re.search(regex, input):
            self.recoveryLbl.setText("")
            self.recoverBtn.setEnabled(True)
            self.recoverBtn.setStyleSheet(
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
        else:
            self.recoveryLbl.setText("invalid email")
            self.recoverBtn.setEnabled(False)
            self.recoverBtn.setStyleSheet(
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
            
