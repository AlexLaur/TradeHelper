from PySide2 import QtCore, QtGui, QtWidgets

from libs.events_handler import EventHandler


class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(PushButton, self).__init__(parent=parent)

        self.__dict__.update(kwargs)


class IndicatorPushButton(PushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(IndicatorPushButton, self).__init__(
            parent=parent, *args, **kwargs
        )

        self.signals = EventHandler()

        # self.setFlat(True)
        self.setCheckable(True)

        self.blockSignals(True)
        self.toggle_button()
        self.blockSignals(False)

        # Signals
        self.clicked.connect(self.toggle_button)

    def toggle_button(self):
        self.toggle()
        if self.isChecked():
            self.setChecked(False)
            self.setText("Activate")
            self.signals.sig_indicator_disable.emit(self.indicator, False)
        else:
            self.setChecked(True)
            self.setText("Activated")
            self.signals.sig_indicator_enable.emit(self.indicator, True)
