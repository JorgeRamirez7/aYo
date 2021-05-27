import re

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class NewUserWindow(QWidget):
    #This is for creating a new account
    def __init__(self, parent):
        super().__init__()
        uic.loadUi(r"ui\\ui_files\\new_user.ui", self)

        self.parent = parent

        self.createEmail.textEdited.connect(self.authenticate_email)

        self.createPassword.textEdited.connect(self.authenticate_password)

        self.confirmPassword.textEdited.connect(self.compare_passwords)

        self.cancelBtn.clicked.connect(self.close_window)

        self.submitBtn.clicked.connect(self.create_account)

        self.validEmail = False
        self.validPassword = False
        self.validatedPassword = False
        
       

    def authenticate_email(self):
        regex = '^\S+@\w+\.\w{2,3}$'
        input = self.createEmail.text()
        if re.search(regex, input):
            self.createEmailLbl.setText("")
            self.validEmail = True
            self.activate_submit()
        else:
            self.createEmailLbl.setText("invalid email")
            self.validEmail = False
            self.activate_submit()
            
    
    def compare_passwords(self):
        if (self.createPassword.text() != self.confirmPassword.text()):
            self.confirmPassLbl.setText("Passwords do not match.")
            self.validatedPassword = False
            self.activate_submit()
        else:
            self.confirmPassLbl.setText("")
            self.validatedPassword = True
            self.activate_submit()
    
    def authenticate_password(self):
        regex = '^(?=.*[A-Z])(?=.*[!@#$&*]).{8,}$'
        input = self.createPassword.text()
        if re.search(regex, input):
            self.createPasswordLbl.setText("")
            self.validPassword = True
            self.activate_submit()
        else:
            self.createPasswordLbl.setText("Password must contain at least:\n\
            One capital letter\n\
            One special character (!@#$&*)\n\
            And must be at least 8 characters in length.")
            self.validPassword = False
            self.activate_submit()

    def activate_submit(self):
        if (self.validEmail == True) and (self.validPassword == True) and (self.validatedPassword == True):
            self.submitBtn.setEnabled(True)
            self.submitBtn.setStyleSheet(
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
            self.submitBtn.setEnabled(False)
            self.submitBtn.setStyleSheet(
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

    def create_account(self):
        self.close_window()

    def close_window(self):
        self.close()
