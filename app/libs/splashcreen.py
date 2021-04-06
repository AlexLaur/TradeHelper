import os

from PySide2 import QtCore, QtGui, QtWidgets
from ui.splashscreen import Ui_splashscreen


class SplashScreen(QtWidgets.QSplashScreen, Ui_splashscreen):
    """This class is a subclass of a QtWidgets.QSplashScreen

        :param QtWidgets: QtWidgets.QSplashScreen object
        :type QtWidgets: obj
        """
    def __init__(self, path, title):

        pixmap = QtGui.QPixmap(path).scaled(900, 600,
                                            QtCore.Qt.KeepAspectRatio)

        super(SplashScreen, self).__init__(pixmap, QtCore.Qt.WindowStaysOnTopHint)

        self.setupUi(self)

        self.lab_app_name.setText(title)
        self.splash_color = QtGui.QColor(100, 100, 100)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )
        self.center()

        blur = QtWidgets.QGraphicsDropShadowEffect(self)
        blur.setBlurRadius(10)
        blur.setColor(QtGui.QColor(0, 0, 0))
        self.setGraphicsEffect(blur)

    def show_message(self, message=None):
        """Thi function shows the message in the splashscreen

        :param message: The message to show, defaults to None
        :type message: str, optional
        """
        self.showMessage(
            message,
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter,
            self.splash_color,
        )

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())