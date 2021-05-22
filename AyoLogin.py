from AyoBody import AyoBody
from NewUserWindow import NewUserWindow
from PyQt5 import QtWidgets, uic
import re
from RecoverPasswordWindow import RecoverPasswordWindow


class AyoLogin(QtWidgets.QMainWindow):
    #This is the login Screen
    def __init__(self):
        super(AyoLogin, self).__init__()
        uic.loadUi("Main\\aYo.ui", self)
        self.w = None
        self.createAccountBtn.clicked.connect(self.new_account_click)
        self.forgotPasswordBtn.clicked.connect(self.forgot_password_click)
        self.loginBtn.clicked.connect(self.login_click)

        self.mainEmail.textEdited.connect(self.check_email)
        self.mainPassword.textEdited.connect(self.check_password)

        self.validEmail = False
        self.validPassword = False

    def new_account_click(self, checked):
        #opened off of the "create account" button, creates new window
        self.w = None
        self.w = NewUserWindow(self)
        self.w.show()
        
    
    def forgot_password_click(self):
        #opened off of the "forgot password" button, creates new window
        self.w = None
        self.w = RecoverPasswordWindow()
        self.w.show()

    def login_click(self):
        #opened off of the "Log In" button, creates new main window and Closes current window
        self.w = None
        self.w = AyoBody(self)
        self.w.show()
        self.hide()

    def check_email(self):
        #this ensures a valid email is input to the login screen
        regex = '^\S+@\w+\.\w{2,3}$'
        input = self.mainEmail.text()
        if re.search(regex, input):
            self.validEmail = True
            self.activate_login()
        else:
            self.validEmail = False
            self.activate_login()

    def check_password(self):
        #Checks to see if there is any text in the password box
        if(self.mainPassword.text() != ""):
            self.validPassword = True
            self.activate_login()
        else:
            self.validPassword = False
            self.activate_login()
    
    def activate_login(self):
        #Checks to make sure there is a valid email and text in the password field before activating Log In button
        if (self.validEmail == True) and (self.validPassword == True):
            self.loginBtn.setEnabled(True)
            self.loginBtn.setStyleSheet(
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
            self.loginBtn.setEnabled(False)
            self.loginBtn.setStyleSheet(
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