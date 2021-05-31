from azure import get_query
from PyQt5.QtCore import QObject, pyqtSignal

class QueryWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    threadactive = True


    def run(self):
        while (self.threadactive == True):
            get_query.GetQuery.query(self)

    def stop(self):
        self.threadactive = False
        print("stop recieved")
        #self.wait()
        self.finished.emit()
    
    