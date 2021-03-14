import sys
import traceback
from PySide2 import QtGui, QtCore, QtWidgets

from app.libs.events_handler import EventHandler


class ThreadPool(QtCore.QThreadPool):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.setExpiryTimeout(3000)
        self.signals = EventHandler()

    def execution(self, function, *args, **kwargs):
        worker = Runnable(self, function, *args, **kwargs)

        self.start(worker, 1)


class Runnable(QtCore.QRunnable):
    def __init__(self, parent, fn, *args, **kwargs):
        super(Runnable, self).__init__(parent=parent)

        self.fn = fn
        self.args = args
        self.kwargs = kwargs

        self.parent = parent

    def run(self):
        try:
            self.parent.signals.sig_thread_pre.emit()
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            self.parent.signals.sig_thread_failed.emit()
        finally:
            self.parent.signals.sig_thread_post.emit()
