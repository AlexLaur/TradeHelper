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


class FavoriteButton(PushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(FavoriteButton, self).__init__(parent)

        self.setCheckable(True)
        self.setFlat(True)

        icon_otpions = [{"scale_factor": 1.4, "color": "white"}]
        self.icon_star = qta.icon("mdi.star", options=icon_otpions)
        self.icon_star_outline = qta.icon(
            "mdi.star-outline", options=icon_otpions
        )

        if kwargs.get("checked", False):
            self.setChecked(True)
            self.setIcon(self.icon_star)
        else:
            self.setChecked(False)
            self.setIcon(self.icon_star_outline)

        self.setFixedSize(QtCore.QSize(20, 20))

        # Signals
        self.clicked.connect(self.toggle_button)

    def toggle_button(self):
        self.toggle()
        if self.isChecked():
            self.setChecked(False)
            self.setIcon(self.icon_star_outline)
        else:
            self.setChecked(True)
            self.setIcon(self.icon_star)
