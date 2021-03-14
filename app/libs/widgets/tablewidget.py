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


class TableFinancial(QtWidgets.QTableWidget):
    def __init__(self, parent=None, data=None):
        super(TableFinancial, self).__init__(parent=parent)
        print(data)
        if data:
            self.data = data.datas
            print(self.data)
            self.test()

    def test(self):
        # Columns
        header = self.data['YEAR']
        hearder_len = len(header)
        header.insert(0, 'Valorisation')
        header.insert(len(header), 'Bilan')
        score = self.data["Score"]
        del self.data["YEAR"]
        del self.data["Score"]

        print(header)
        print(self)

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.horizontalHeader().resizeSection(0, 150)
        self.setColumnWidth(len(header) - 1, 250)
        self.setWordWrap(True)

        # Rows
        # for row, (title, donnee) in enumerate(sorted(self.data.items())):
        #     self.insertRow(row)
        #     cell_val = QtWidgets.QTableWidgetItem()
        #     cell_val.setData(QtCore.Qt.DisplayRole, title)
        #     self.tableWidget.setItem(row, 0, cell_val)
        #     for column, data in enumerate(donnee):
        #         cell = QtWidgets.QTableWidgetItem()
        #         cell.setData(QtCore.Qt.DisplayRole, str(data))
        #         cell.setTextAlignment(QtCore.Qt.AlignRight)
        #         self.setItem(row, column + 1, cell)
        #
        #     analyse_cell = QtWidgets.QTableWidgetItem()
        #     analyse_cell.setData(QtCore.Qt.DisplayRole, self.data[title])
        #     self.setItem(row, 7, analyse_cell)
        #
        # # Add Score to the last Row
        # last_row = len(self.data)
        # self.insertRow(last_row)
        # cell_score_title = QtWidgets.QTableWidgetItem()
        # cell_score_title.setData(QtCore.Qt.DisplayRole, "Score")
        # self.setItem(last_row, 0, cell_score_title)
        # cell_score = QtWidgets.QTableWidgetItem()
        # cell_score.setData(QtCore.Qt.DisplayRole, str(score[0]))
        # cell_score.setTextAlignment(QtCore.Qt.AlignRight)
        # self.setItem(last_row, hearder_len + 1, cell_score)