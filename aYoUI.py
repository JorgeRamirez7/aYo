from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import re


class aYo(QtWidgets.QMainWindow):
    #This is the login Screen
    def __init__(self):
        super(aYo, self).__init__()
        uic.loadUi("Main\\aYo.ui", self)
        self.w = None
        self.createAccountBtn.clicked.connect(self.newAccountClick)
        self.forgotPasswordBtn.clicked.connect(self.forgotPasswordClick)
        self.loginBtn.clicked.connect(self.loginClick)

        self.mainEmail.textEdited.connect(self.checkEmail)
        self.mainPassword.textEdited.connect(self.checkPassword)

        self.validEmail = False
        self.validPassword = False

    def newAccountClick(self, checked):
        #opened off of the "create account" button, creates new window
        self.w = None
        self.w = newUserWindow()
        self.w.show()
    
    def forgotPasswordClick(self):
        #opened off of the "forgot password" button, creates new window
        self.w = None
        self.w = recoverPasswordWindow()
        self.w.show()

    def loginClick(self):
        #opened off of the "Log In" button, creates new main window and Closes current window
        self.w = None
        body.show()
        self.hide()

    def checkEmail(self):
        #this ensures a valid email is input to the login screen
        regex = '^\S+@\w+\.\w{2,3}$'
        input = self.mainEmail.text()
        if re.search(regex, input):
            self.validEmail = True
            self.activateLogin()
        else:
            self.validEmail = False
            self.activateLogin()

    def checkPassword(self):
        #Checks to see if there is any text in the password box
        if(self.mainPassword.text() != ""):
            self.validPassword = True
            self.activateLogin()
        else:
            self.validPassword = False
            self.activateLogin()
    
    def activateLogin(self):
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

class newUserWindow(QWidget):
    #This is for creating a new account
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\NewUser.ui", self)

        self.createEmail.textEdited.connect(self.authenticateEmail)

        self.confirmPassword.textEdited.connect(self.comparePasswords)

        self.createPassword.textEdited.connect(self.authenticatePassword)

        self.cancelBtn.clicked.connect(self.closeWindow)

        self.submitBtn.clicked.connect(self.createAccount)

        self.validEmail = False
        self.validPassword = False
        self.validatedPassword = False
        
       

    def authenticateEmail(self):
        regex = '^\S+@\w+\.\w{2,3}$'
        input = self.createEmail.text()
        if re.search(regex, input):
            self.createEmailLbl.setText("")
            self.validEmail = True
            self.activateSubmit()
        else:
            self.createEmailLbl.setText("invalid email")
            self.validEmail = False
            self.activateSubmit()
            
    
    def comparePasswords(self):
        if (self.createPassword.text() != self.confirmPassword.text()):
            self.confirmPassLbl.setText("Passwords do not match.")
            self.validatedPassword = False
            self.activateSubmit()
        else:
            self.confirmPassLbl.setText("")
            self.validatedPassword = True
            self.activateSubmit()
    
    def authenticatePassword(self):
        regex = '^(?=.*[A-Z])(?=.*[!@#$&*]).{8,}$'
        input = self.createPassword.text()
        if re.search(regex, input):
            self.createPasswordLbl.setText("")
            self.validPassword = True
            self.activateSubmit()
        else:
            self.createPasswordLbl.setText("Password must contain at least:\n\
            One capital letter\n\
            One special character (!@#$&*)\n\
            And must be at least 8 characters in length.")
            self.validPassword = False
            self.activateSubmit()

    def activateSubmit(self):
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

    def createAccount(self):
        self.closeWindow()

    def closeWindow(self):
        win.show()
        self.close()

class recoverPasswordWindow(QWidget):
    #recover account ui
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\Recovery.ui", self)

        self.recoverCancelBtn.clicked.connect(self.closeWindow)

        self.recoverBtn.clicked.connect(self.recoverPassword)

        self.recoveryEmail.textEdited.connect(self.authenticateEmail)

    def closeWindow(self):
        self.close()
    
    def recoverPassword(self):
        self.close()
    
    def authenticateEmail(self):
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

class aYoBody(QtWidgets.QMainWindow):
    def __init__(self):
        super(aYoBody, self).__init__()
        uic.loadUi("Main\\aYoBody.ui", self)
        self.w = None

        self.exitBtn.clicked.connect(self.exit)
        self.startBtn.clicked.connect(self.listeningActivated)
        self.supportedBtn.clicked.connect(self.viewLanguages)
        self.settingsBtn.clicked.connect(self.settings)

    def listeningActivated(self):
        print("activation Placeholder")

    def viewLanguages(self):
        self.w = None
        self.w = languagesWindow()
        self.w.show()
        

    def settings(self):
        self.w = None
        self.w = settingsWindow()
        self.w.show()
        self.hide()

    def exit(self):
        quit()

class settingsWindow(QWidget):
    #Settings page
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\settings.ui", self)

        
        self.modeToggle.currentIndexChanged.connect(self.changeMode)
        self.secondsBox.valueChanged.connect(self.durationChange)
        self.addLanguageBtn.clicked.connect(self.addLanguage)
        self.yesRadioBtn.toggled.connect(self.onStartup)
        self.linkBtn.clicked.connect(self.linkSpotify)
        self.returnBtn.clicked.connect(self.returnHome)

    def changeMode(self):
        print("Mode Placeholder")
    
    def durationChange(self):
        print("Duration Placeholder")

    def addLanguage(self):
        print("Language Placeholder")

    def onStartup(self):
        print("startup on Placeholder")
    
    def linkSpotify(self):
        print("link Placeholder")

    def returnHome(self):
        body.show()
        self.close()

class languagesWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main\\languages.ui", self)

        self.closeBtn.clicked.connect(self.closeWindow)


    def closeWindow(self):
        self.close()
    


app = QtWidgets.QApplication([])
body = aYoBody()
win = aYo()
body.hide()
win.show()
sys.exit(app.exec())