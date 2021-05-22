from AyoLogin import AyoLogin
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication([])
win = AyoLogin()
win.show()
sys.exit(app.exec())
