from azure.get_query import GetQuery

from ui.ui_classes.ayo_login import AyoLogin
from PyQt5 import QtWidgets

def main():
    GetQuery().get_query()

if __name__ == "__main__":


#If this is giving you an error add "python.analysis.extraPaths": ["./UI"] to your settings.json file
    app = QtWidgets.QApplication([])
    win = AyoLogin()
    win.show()
    app.exec()

    main()
