from azure import get_query
from PyQt5.QtCore import QObject, pyqtSignal

class QueryWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    threadactive = True


    def run(self):
        while (self.threadactive == True):
            get_query.GetQuery.query(self)
            self.threadactive = False
            self.finished.emit()

    def stop(self):
        self.threadactive = False
        print("stop received")
        #self.wait()
        self.finished.emit()
    
    