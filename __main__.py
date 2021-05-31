from PyQt5 import QtWidgets

from azure.get_query import GetQuery
from skills.introduction_skill import IntroductionSkill
from ui.ui_classes.ayo_login import AyoLogin

if __name__ == "__main__":
    ayo_introduction = True

    if ayo_introduction:
        IntroductionSkill().ayo_intro()


#If this is giving you an error add "python.analysis.extraPaths": ["./UI"] to your settings.json file
    app = QtWidgets.QApplication([])
    win = AyoLogin()
    win.show()
    app.exec()

    GetQuery().query()
