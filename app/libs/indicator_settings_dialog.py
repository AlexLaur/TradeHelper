from PySide2 import QtGui, QtCore, QtWidgets

from ui.indicator_settings_dialog import Ui_IndicatorSettingsDialogWindow
from ui.indicator_setting_style_widget import Ui_IndicatorStyleSettingWidget
from ui.indicator_setting_input_widget import Ui_IndicatorInputSettingWidget
from libs.events_handler import EventHandler


class IndicatorSettingsDialogWindow(
    QtWidgets.QDialog, Ui_IndicatorSettingsDialogWindow
):
    def __init__(self, parent=None):
        super(IndicatorSettingsDialogWindow, self).__init__(parent)

        self.setupUi(self)

        # Constant
        self._current_indicator = None
        self.signals = EventHandler()

        # Signals
        self.pub_cancel.clicked.connect(self._on_canceled)
        self.pub_ok.clicked.connect(self._on_ok)
        self.pub_reset.clicked.connect(self._on_reset)

    @property
    def indicator(self):
        """Return the current indicator

        :return: The current indicator
        :rtype: Indicator
        """
        return self._current_indicator

    def show(self, indicator, *args, **kwargs):
        """Show this widget

        :param indicator: The indicator assicated
        :type indicator: Indicator
        """
        self.move(self.parent().rect().center() - self.rect().center())
        self.build_settings(indicator=indicator)
        super(IndicatorSettingsDialogWindow, self).show()

    def build_settings(self, indicator):
        """Build settings widget with all parameters of the indicator

        :param indicator: The indicator
        :type indicator: Indicator
        """
        self.lst_inputs.clear()
        self.lst_styles.clear()
        self._current_indicator = indicator
        for _field in indicator.fields:
            if _field.value is not None:

                item = QtWidgets.QListWidgetItem()
                self.lst_inputs.addItem(item)

                wgt_input = IndicatorInputSettingWidget(field=_field)
                item.setSizeHint(wgt_input.sizeHint())
                self.lst_inputs.setItemWidget(item, wgt_input)

            if _field.color is not None:

                item = QtWidgets.QListWidgetItem()
                self.lst_styles.addItem(item)

                wgt_style = IndicatorStyleSettingWidget(field=_field)
                item.setSizeHint(wgt_style.sizeHint())
                self.lst_styles.setItemWidget(item, wgt_style)

    @QtCore.Slot()
    def _on_canceled(self):
        """Called on clicked on CANCEL button"""
        self._current_indicator = None
        # TODO Clear all widget, restore to default
        self.signals.sig_indicator_settings_canceled.emit(self.indicator)
        self.close()

    @QtCore.Slot()
    def _on_ok(self):
        """Called on clicked on OK button"""
        self.signals.sig_indicator_settings_validated.emit(self.indicator)
        self.close()

    @QtCore.Slot()
    def _on_reset(self):
        """Called on clicked on Reset settings button"""
        # TODO Reset all settings to default
        self.signals.sig_indicator_settings_reseted.emit(self.indicator)


class IndicatorInputSettingWidget(
    QtWidgets.QWidget, Ui_IndicatorInputSettingWidget
):
    def __init__(self, field, parent=None):
        super(IndicatorInputSettingWidget, self).__init__(parent)

        self.setupUi(self)

        # Constans
        self._field = field

        # Init Ui from field values
        self.lab_field_name.setText(self._field.attribute_name)
        self.spi_value.setValue(self._field.value)

        # Signals
        self.spi_value.valueChanged.connect(self._on_value_changed)

    @QtCore.Slot(int)
    def _on_value_changed(self, value: int):
        """Called on value changed in the spinbox

        :param value: The new value
        :type value: int
        """
        self._field.value = value


class IndicatorStyleSettingWidget(
    QtWidgets.QWidget, Ui_IndicatorStyleSettingWidget
):
    def __init__(self, field, parent=None):
        super(IndicatorStyleSettingWidget, self).__init__(parent)

        self.setupUi(self)

        # Constans
        self._field = field
        self.color_picker = QtWidgets.QColorDialog(parent=self)
        self.color_picker.setOption(
            QtWidgets.QColorDialog.ShowAlphaChannel, on=True
        )

        # Init Ui from field values
        self.lab_field_name.setText(self._field.attribute_name)
        self.set_button_background_color(color=self._field.color)

        # Signal
        self.pub_color.clicked.connect(self._on_color_button_clicked)
        self.color_picker.colorSelected.connect(self._on_color_selected)

    def set_button_background_color(self, color: QtGui.QColor):
        """Set the background color of the button color

        :param color: The color to apply
        :type color: QtGui.QColor
        """
        self.pub_color.setStyleSheet(
            "background-color: {color};".format(color=color.name())
        )

    @QtCore.Slot()
    def _on_color_button_clicked(self):
        """Called on clicked button color"""
        self.color_picker.setCurrentColor(self._field.color)
        self.color_picker.show()

    @QtCore.Slot(object)
    def _on_color_selected(self, color: QtGui.QColor):
        """Called when the color is selected from the color picker

        :param color: The choosen color
        :type color: QtGui.QColor
        """
        self.set_button_background_color(color=color)
        self._field.set_color(color=color)
