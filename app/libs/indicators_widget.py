import json
from PySide2 import QtGui, QtCore, QtWidgets

import resources_rc
from app.libs.events_handler import EventHandler
from app.libs.plugin_collection import PluginCollection
from app.libs.widgets.tablewidgetitem import TableWidgetItem
from app.libs.widgets.pushbutton import IndicatorPushButton
from app.ui import indicators_widget


class Indicator(object):
    """Base class that each indicator must inherit from. within this class
    you must define the methods that all of your plugins must implement
    """

    def __init__(self):
        self.name = "Indicator"
        self.description = "Indicator description"

        # Var for plot items
        self._plots = []

    def create_indicator(self, graph_view, *args, **kwargs):
        """The method that we expect all plugins to implement. This is the
        method that our framework will call to draw the indicator
        """
        raise NotImplementedError

    def remove_indicator(self, graph_view, *args, **kwargs):
        """The method that we expect all plugins to implement. This is the
        method that our framework will call to remove the indicator
        """
        if not self._plots:
            return
        # Remove all plots
        for plot in self._plots:
            plot.clear()
        # Update graph
        graph_view.update()


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

        # Init customs signals
        self.signals = EventHandler()

        headerView = QtWidgets.QHeaderView(
            QtCore.Qt.Horizontal, self.tab_indicators
        )
        self.tab_indicators.setHorizontalHeader(headerView)
        headerView.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        headerView.setSectionsClickable(True)

        self.build_indicators()

        # Signals
        self.lie_indicators_search.textChanged.connect(
            self.tab_indicators.search_items
        )

    def build_indicators(self):
        indicators = self._indicators_collection.plugins

        self.tab_indicators.clearContents()
        self.tab_indicators.setRowCount(len(indicators))

        for index, indicator in enumerate(indicators):
            name_item = TableWidgetItem(text=indicator.name)
            name_item.setToolTip(indicator.description)
            active_button = IndicatorPushButton(indicator=indicator)

            active_button.signals.sig_indicator_enable.connect(
                self.signals.sig_indicator_switched.emit
            )

            active_button.signals.sig_indicator_disable.connect(
                self.signals.sig_indicator_switched.emit
            )

            self.tab_indicators.setItem(index, 0, name_item)
            self.tab_indicators.setCellWidget(index, 1, active_button)

    def reload_indicators(self):
        self._indicators_collection.reload_plugins()
        self.build_indicators()
