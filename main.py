import sys, time, traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import QFile, QRunnable, Slot, QThreadPool, QObject, Signal
from PySide6.QtGui import QIcon, QPixmap, QAction

from GUI.Icons import icons8_rc
from GUI.MainWindow import Ui_MainWindow

# Thread management
class WorkerSignals(QObject):
    
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    
# Worker thread 
class Worker(QRunnable):
    
    def __init__(self, fn, *args, **kwargs):
        
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kargs = kwargs
        self.signals = WorkerSignals()
        self.kargs['progress_callback'] = self.signals.progress
        
    @Slot()
    def run(self):
        
        try:
            
            result = self.fn(*self.args, **self.kargs)
            
        except:
            
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
            
        else:
            
            self.signals.result.emit(result)
            
        finally:
            
            self.signals.finished.emit()
            
        
class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.threadpool = QThreadPool()
        print("Multi-threading with maximum %d threads" % self.threadpool.maxThreadCount())
        
        leave = QAction("Exit", self)
        leave.triggered.connect(self.close_event)
        
    def close_event(self, event):
        
        reply = QMessageBox.question(self, "Message", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            
            event.accept()
            
        else:
            
            event.ignore()
            
    # Thread management
    
    def progress_fn(self, n):
            
        print("%d%% done" % n)
        
    def print_output(self, s):
        
        print(s)
        
    def thread_complete(self):
            
        print("Thread complete")
        
    def start_thread(self, fn):
            
        # Pass the function to execute
        worker = Worker(fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        
        # Execute
        self.threadpool.start(worker)
        
    # GUI management
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())