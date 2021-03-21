from PySide2 import QtGui, QtCore, QtWidgets


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None, *args, **kwargs):
        super(ComboBox, self).__init__(parent)


class StyleComboBox(ComboBox):
    """Combox used to define line style in the setting indicator dialog"""

    def __init__(self, parent=None, *args, **kwargs):
        super(StyleComboBox, self).__init__(parent, *args, **kwargs)

        self._items = []

    def build(self, line_styles: dict):
        """Build items of the combobox

        :param line_styles: Available line styles
        :type line_styles: dict
        """
        for name, line_style in line_styles.items():
            icon = QtGui.QIcon(line_style.get("icon"))
            data = line_style
            self.addItem(icon, name, data)
            self._items.append(data)

    def set_current_style(self, line_style):
        """Set the current item of the combobox

        :param line_style: The line style
        :type line_style: QtCore.Qt.PenStyle
        """
        for index, item in enumerate(self._items):
            if item.get("style") != line_style:
                continue
            self.setCurrentIndex(index)
