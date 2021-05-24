import sys

from ui_classes.ayo_login import AyoLogin
from PyQt5 import QtWidgets



app = QtWidgets.QApplication([])
win = AyoLogin()
win.show()
sys.exit(app.exec())
