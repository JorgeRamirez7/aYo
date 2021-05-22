from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget
import re
import sys




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
        self.w = NewUserWindow()
        self.w.show()
    
    def forgot_password_click(self):
        #opened off of the "forgot password" button, creates new window
        self.w = None
        self.w = RecoverPasswordWindow()
        self.w.show()

    def login_click(self):
        #opened off of the "Log In" button, creates new main window and Closes current window
        self.w = None
        body.show()
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

class NewUserWindow(QWidget):
    #This is for creating a new account
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\NewUser.ui", self)

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
        win.show()
        self.close()

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

class AyoBody(QtWidgets.QMainWindow):
    def __init__(self):
        super(AyoBody, self).__init__()
        uic.loadUi("Main\\AyoBody.ui", self)
        self.w = None

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
        self.w = SettingsWindow()
        self.w.show()
        self.hide()

    def exit(self):
        quit()

class SettingsWindow(QWidget):
    #Settings page
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\settings.ui", self)

        
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
        body.show()
        self.close()

class LanguagesWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\languages.ui", self)

        self.closeBtn.clicked.connect(self.close_window)


    def close_window(self):
        self.close()
    


app = QtWidgets.QApplication([])
body = AyoBody()
win = AyoLogin()
body.hide()
win.show()
sys.exit(app.exec())
