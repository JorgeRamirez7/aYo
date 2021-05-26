import sys

#unsure why this is still erroring, It works fine but I dont know if its something to be worried about
from ui_classes.ayo_login import AyoLogin
from PyQt5 import QtWidgets



app = QtWidgets.QApplication([])
win = AyoLogin()
win.show()
sys.exit(app.exec())
