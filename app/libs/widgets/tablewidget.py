from PySide2 import QtCore, QtGui, QtWidgets


class TableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent=parent)

    def search_items(self, text: str):
        """Search all items correcponding to the text

        :param text: The text to search
        :type text: str
        :param column: The column on which to search, defaults to 0
        :type column: int, optional
        """
        found = self.findItems(text, QtCore.Qt.MatchContains)
        # Unhides all items if no text
        if not text:
            for index in range(self.rowCount()):
                self.showRow(index)
        else:
            # Hide all items
            for index in range(self.rowCount()):
                self.hideRow(index)
            for item in found:
                # show only item
                self.showRow(self.row(item))


class IndicatorsTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(IndicatorsTableWidget, self).__init__(parent=parent)

    def set_header(self):
        """Sets a custom header to the Tablewidget"""
        header = QtWidgets.QHeaderView(QtCore.Qt.Horizontal, self)
        self.setHorizontalHeader(header)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.resizeSection(1, 25)
        header.resizeSection(2, 25)
        header.setSectionsClickable(True)
