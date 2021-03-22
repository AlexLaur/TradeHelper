import json
from PySide2 import QtGui, QtCore, QtWidgets

from libs.events_handler import EventHandler
from libs.indicator_settings_dialog import IndicatorSettingsDialogWindow
from libs.plugin_collection import PluginCollection
from libs.widgets.tablewidgetitem import TableWidgetItem
from libs.widgets.pushbutton import (
    IndicatorPushButton,
    IndicatorSettingsPushButton,
)
from ui import indicators_widget
from utils.indicators_utils import Indicator


class IndicatorsWidget(
    QtWidgets.QWidget, indicators_widget.Ui_IndicatorsWidget
):
    def __init__(self, parent=None):
        super(IndicatorsWidget, self).__init__(parent=parent)

        self.setupUi(self)

        # Detect all indicators add-ons
        self._indicators_collection = PluginCollection(
            plugin_package="add_ons",
            plugin_class=Indicator,
        )
        self.indicator_settings_dialog = IndicatorSettingsDialogWindow(
            parent=self
        )

        # Init customs signals
        self.signals = EventHandler()

        self.tab_indicators.set_header()
        self.build_indicators()

        # Signals
        self.lie_indicators_search.textChanged.connect(
            self.tab_indicators.search_items
        )
        self.indicator_settings_dialog.signals.sig_indicator_settings_validated.connect(
            self._on_settings_validated
        )

    def build_indicators(self):
        """Build the table which contains all indicators"""
        indicators = self._indicators_collection.plugins

        self.tab_indicators.clearContents()
        self.tab_indicators.setRowCount(len(indicators))

        for index, indicator in enumerate(indicators):
            name_item = TableWidgetItem(text=indicator.name)
            name_item.setToolTip(indicator.description)

            settings_button = IndicatorSettingsPushButton(indicator=indicator)
            settings_button.signals.sig_indicator_settings_clicked.connect(
                self._on_settings_clicked
            )

            active_button = IndicatorPushButton(indicator=indicator)
            active_button.signals.sig_indicator_enabled.connect(
                self.signals.sig_indicator_switched.emit
            )
            active_button.signals.sig_indicator_disabled.connect(
                self.signals.sig_indicator_switched.emit
            )

            self.tab_indicators.setItem(index, 0, name_item)
            self.tab_indicators.setCellWidget(index, 1, settings_button)
            self.tab_indicators.setCellWidget(index, 2, active_button)

    def reload_indicators(self):
        """Reload all indicators"""
        self._indicators_collection.reload_plugins()
        self.build_indicators()

    @QtCore.Slot(object)
    def _on_settings_clicked(self, indicator: Indicator):
        """Called when the setting button of an indicator is clicked

        :param indicator: The indicator plugin
        :type indicator: Indicator
        """
        self.indicator_settings_dialog.show(indicator=indicator)

    @QtCore.Slot(object)
    def _on_settings_validated(self, indicator: Indicator):
        """Called when the settings have been validated (click on OK button)

        :param indicator: The indicator which has been edited
        :type indicator: Indicator
        """
        if indicator.enabled:
            # First: disable it
            self.signals.sig_indicator_switched.emit(indicator, False)
            # Second: re enable it
            self.signals.sig_indicator_switched.emit(indicator, True)
