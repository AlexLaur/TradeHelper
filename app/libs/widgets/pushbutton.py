import qtawesome as qta
from PySide2 import QtCore, QtGui, QtWidgets

import resources_rc
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

        # Constans
        self.signals = EventHandler()
        self.setFlat(True)
        self.setCheckable(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(QtGui.QIcon(":/svg/toggle-off.svg"))
        self.setIconSize(QtCore.QSize(30, 30))

        # Init button state
        self.blockSignals(True)
        self.toggle_button()
        self.blockSignals(False)

        # Signals
        self.clicked.connect(self.toggle_button)

    def toggle_button(self):
        """Toggle the state of the button"""
        self.toggle()
        if self.isChecked():
            self.setChecked(False)
            self.setIcon(QtGui.QIcon(":/svg/toggle-off.svg"))
            self.signals.sig_indicator_disabled.emit(self.indicator, False)
        else:
            self.setChecked(True)
            self.setIcon(QtGui.QIcon(":/svg/toggle-on.svg"))
            self.signals.sig_indicator_enabled.emit(self.indicator, True)


class IndicatorSettingsPushButton(PushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(IndicatorSettingsPushButton, self).__init__(
            parent=parent, *args, **kwargs
        )

        # Constans
        self.signals = EventHandler()
        self.setFlat(True)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(QtGui.QIcon(":/svg/settings.svg"))
        self.setIconSize(QtCore.QSize(20, 20))

        # Signals
        self.clicked.connect(self._on_clicked)

    @QtCore.Slot()
    def _on_clicked(self):
        """Called when the button is clicked"""
        self.signals.sig_indicator_settings_clicked.emit(self.indicator)
