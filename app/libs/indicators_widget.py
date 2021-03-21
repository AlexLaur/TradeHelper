import json
from PySide2 import QtGui, QtCore, QtWidgets

import resources_rc
from libs.events_handler import EventHandler
from libs.indicator_settings_dialog import IndicatorSettingsDialogWindow
from libs.plugin_collection import PluginCollection
from libs.widgets.tablewidgetitem import TableWidgetItem
from libs.widgets.pushbutton import (
    IndicatorPushButton,
    IndicatorSettingsPushButton,
)
from ui import indicators_widget


class InputField(object):
    """Object for value and style management for indicators"""

    def __init__(
        self, attribute_name: str, color=None, value=None, width=None, **kwargs
    ):
        """Create a customisable field in order to customise graph.
        - If no value is providen but a color is, this field will be present
        in the "style" setting page.
        - If no color is provided but a value is, this field will be present
        in the "Input" setting page.
        - If both are provided, this will be present in both settings.

        :param attribute_name: The name of the field
        :type attribute_name: str
        :param color: The color to apply by default, defaults to None
        :type color: tuple, optional
        :param value: The value to apply by default, defaults to None
        :type value: int or float, optional
        :param width: The width to apply by default, defaults to None
        :type width: int or float, optional

        kwargs parameters:

        :param disable_line_style: Disable the posibility to choose a
        line stype from the style page. defaults to False
        :type disable_line_style: bool
        :param line_style: Choose a style to apply for lines.
        3 Choices are available (line, dash-line and dot-line). defaults to line
        :type line_style: str
        """

        # Constans
        self._line_styles = {
            "line": {"icon": ":/svg/line.svg", "style": QtCore.Qt.SolidLine},
            "dash-line": {
                "icon": ":/svg/dash-line.svg",
                "style": QtCore.Qt.DashLine,
            },
            "dot-line": {
                "icon": ":/svg/dot-line.svg",
                "style": QtCore.Qt.DotLine,
            },
        }

        self._attribute_name = attribute_name
        self._default_color = QtGui.QColor(*color) if color else None
        self._default_value = value
        self._default_line_style = QtCore.Qt.SolidLine

        self.color = self._default_color
        self.value = self._default_value
        self.width = width
        self.disable_line_style = False
        self.line_style = self._default_line_style

        # Kwargs settings
        if kwargs.get("disable_line_style", False):
            self.disable_line_style = True
        if kwargs.get("line_style", None):
            self.set_line_style(kwargs.get("line_style"))

    @property
    def attribute_name(self) -> str:
        """Return the attribute name of the InputField

        :return: The attribute name
        :rtype: str
        """
        return self._attribute_name

    def set_color(self, color: QtGui.QColor):
        """Set the color of the InputField

        :param color: The new color to set
        :type color: tuple
        """
        self.color = color

    def set_value(self, value):
        """Set the value of the InputField

        :param value: The new value to set
        :type value: int, float
        """
        self.value = value

    def set_width(self, width):
        """Set the width of the InputField

        :param width: The new width to set
        :type width: int, float
        """
        self.width = width

    def set_line_style(self, line_style_name: str = None, line_style=None):
        """Set the line style of the InputField

        :param line_style_name: The style of the line (line, dash-line, dot-line)
        :type line_style_name: str, optional
        :param line_style: The style of the line (1, 2, 3)
        :type line_style: int, optional
        :raises KeyError: If the style doesn't exists
        """
        if not line_style_name and not line_style:
            return
        if line_style_name:
            if line_style_name not in self._line_styles:
                raise KeyError("%s not in available styles" % line_style_name)
            self.line_style = self._line_styles.get(line_style_name).get(
                "style"
            )
            return
        if line_style:
            for style_data in self._line_styles.values():
                if style_data.get("style") != line_style:
                    continue
                self.line_style = line_style

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __repr__(self):
        return "<InputField %s @0x%08x>" % (self._attribute_name, id(self))

    def __str__(self):
        return "InputField %s" % (self._attribute_name)


class Indicator(object):
    """Base class that each indicator must inherit from. Within this class
    you must define the methods that all of your plugins must implement
    """

    def __init__(self):
        self.name = "Indicator"
        self.description = "Indicator description"
        self.enabled = False

        self._fields = []
        self._plots = []

    @property
    def fields(self) -> list:
        """Return all registered fields in the Indicator plugin

        :return: List of registered fields
        :rtype: list
        """
        return self._fields

    def register_field(self, field: InputField):
        """Register a field setting

        :param field: The input
        :type field: object
        """
        self._fields.append(field)

    def register_fields(self, *args: list):
        """Register all given fields settings"""
        for arg in args:
            if not isinstance(arg, InputField):
                continue
            self.register_field(field=arg)

    def get_field(self, attribute_name: str) -> InputField:
        """Get the filed which correspond to the given attribute name

        :param attribute_name: The name of the attribute what the InputField
        represents.
        :type attribute_name: str
        :return: The InputField which correspond to the given attribute name
        :rtype: InputField
        """
        for _field in self._fields:
            if _field.attribute_name == attribute_name:
                return _field

    def register_plot(self, plot):
        """Register a plot inside the indicator in order to be abble to delete
        it later, if it is necessary.

        :param plot: The plot to add
        :type plot: pyqtgraph.plotItem
        """
        self._plots.append(plot)

    def register_plots(self, *args: list):
        """Register all given plots"""
        for arg in args:
            self.register_plot(plot=arg)

    def create_indicator(self, graph_view, *args, **kwargs):
        """The method that we expect all plugins to implement. This is the
        method that our framework will call to draw the indicator
        """
        self.enabled = True

    def remove_indicator(self, graph_view, *args, **kwargs):
        """The method that we expect all plugins to implement. This is the
        method that our framework will call to remove the indicator
        """
        self.enabled = False
        if not self._plots:
            return
        # Remove all plots
        for plot in self._plots:
            plot.clear()
        self._plots = []
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
