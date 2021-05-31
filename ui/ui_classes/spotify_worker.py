from skills import music_skills
from PyQt5.QtCore import QObject, pyqtSignal

class SpotifyWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    threadactive = True


    def run(self):
    
        music_skills.MusicSkill.login(self)
        self.finished.emit()

    def stop(self):
        self.threadactive = False
        print("stop recieved")
        #self.wait()
        self.finished.emit()
    
    