from PySide2 import QtGui, QtCore, QtWidgets

from ui.indicator_settings_dialog import Ui_IndicatorSettingsDialogWindow
from ui.indicator_setting_style_widget import Ui_IndicatorStyleSettingWidget
from ui.indicator_setting_input_widget import Ui_IndicatorInputSettingWidget
from libs.events_handler import EventHandler
from utils.indicators_utils import ChoiceField, InputField
from utils import utils


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

        :param indicator: The indicator associated
        :type indicator: Indicator
        """
        main_window = utils.get_main_window_instance()
        if main_window:
            self.move(main_window.rect().center() - self.rect().center())
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
            # TODO Refacto this
            if isinstance(_field, InputField):
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

            elif isinstance(_field, ChoiceField):
                item = QtWidgets.QListWidgetItem()
                self.lst_inputs.addItem(item)
                wgt_input = IndicatorInputSettingWidget(field=_field)
                item.setSizeHint(wgt_input.sizeHint())
                self.lst_inputs.setItemWidget(item, wgt_input)

            else:
                ...

    def reset_settings_default(self):
        """Reset all fields to default values"""
        for field in self.indicator.fields:
            field.reset()

    @QtCore.Slot()
    def _on_canceled(self):
        """Called on clicked on CANCEL button"""
        self._current_indicator = None
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
        # Reset values
        self.reset_settings_default()
        # Rebuild UI
        self.build_settings(indicator=self.indicator)
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

        if self._field.value_type is int:
            self.spi_value_int.setValue(self._field.value)
            self.spi_value_double.hide()
            self.cob_value_list.hide()
        elif self._field.value_type is float:
            self.spi_value_int.hide()
            self.spi_value_double.setValue(self._field.value)
            self.cob_value_list.hide()
        elif self._field.value_type in [list, tuple]:
            self.spi_value_int.hide()
            self.spi_value_double.hide()
            self.cob_value_list.build(choices=self._field.choices)
            self.cob_value_list.setCurrentText(self._field.current)

        # Signals
        self.spi_value_int.valueChanged.connect(self._on_value_changed)
        self.spi_value_double.valueChanged.connect(self._on_value_changed)
        self.cob_value_list.currentTextChanged.connect(
            self._on_value_choice_changed
        )

    @QtCore.Slot(int)
    def _on_value_changed(self, value):
        """Called on value changed in the spinbox

        :param value: The new value
        :type value: int or float
        """
        self._field.value = value

    @QtCore.Slot(str)
    def _on_value_choice_changed(self, choice):
        """Called on text changed inside the combobox

        :param choice: The new text
        :type choice: str
        """
        self._field.current = choice


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

        if not self._field.disable_line_style:
            self.cob_line_style.build(line_styles=self._field._line_styles)
            self.cob_line_style.set_current_style(
                line_style=self._field.line_style
            )
        else:
            self.cob_line_style.hide()

        # Signal
        self.pub_color.clicked.connect(self._on_color_button_clicked)
        self.color_picker.colorSelected.connect(self._on_color_selected)
        self.cob_line_style.currentIndexChanged.connect(
            self._on_line_style_selected
        )

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

    @QtCore.Slot(int)
    def _on_line_style_selected(self, index: int):
        """Called when the line style is changed from the combobox

        :param index: The index of the current selected item
        :type index: int
        """
        line_style_name = self.cob_line_style.currentText()
        self._field.set_line_style(line_style_name=line_style_name)
