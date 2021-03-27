from PySide2 import QtWidgets, QtCore, QtGui
from libs.analysies.analyse_financials import AnalyseFondamental


class QTableWidgetFinance(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(QTableWidgetFinance, self).__init__(parent=parent)


class TableFinance(QTableWidgetFinance):
    def __init__(self, parent=None):
        super(TableFinance, self).__init__(parent=parent)

    @QtCore.Slot(str)
    def on_set_financials_table(self, ticker):
        """
        This method get the fondamental from the compagny
        and fill the table.
        """
        analyses = AnalyseFondamental(ticker)
        self.data = analyses.datas

        self.clear()
        self.header = self.data['YEAR']
        self.header[-1] = "Bilan"
        self.header.insert(0, 'Valorisation')
        score = self.data["Score"]

        del self.data["YEAR"]
        del self.data["Score"]

        self.setColumnCount(len(self.header))
        self.setHorizontalHeaderLabels(self.header)
        self.horizontalHeader().resizeSection(0, 150)
        self.setColumnWidth(len(self.header) - 1, 250)
        self.setWordWrap(True)

        # Rows
        for row, (title, donnee) in enumerate(sorted(self.data.items())):
            self.insertRow(row)
            cell_val = QtWidgets.QTableWidgetItem()
            cell_val.setData(QtCore.Qt.DisplayRole, title)
            self.setItem(row, 0, cell_val)
            for column, data in enumerate(donnee):
                cell = QtWidgets.QTableWidgetItem()
                cell.setData(QtCore.Qt.DisplayRole, str(data))
                cell.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(row, column + 1, cell)

        # Add Score to the last Row
        last_row = len(self.data)
        self.insertRow(last_row)
        cell_score_title = QtWidgets.QTableWidgetItem()
        cell_score_title.setData(QtCore.Qt.DisplayRole, "Score")
        self.setItem(last_row, 0, cell_score_title)
        cell_score = QtWidgets.QTableWidgetItem()
        cell_score.setData(QtCore.Qt.DisplayRole, str(score[0]))
        cell_score.setTextAlignment(QtCore.Qt.AlignCenter)
        self.setItem(last_row, len(self.header) - 1, cell_score)

        for i in range(self.rowCount()):
            self.setRowHeight(i, 50)

        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
        self.setMouseTracking(True)
        self.cellEntered.connect(self.cellHover)

    def cellHover(self, row, column):
        """
        This method get position (row,column) of cursor.
        """
        self.clearSelection()
        self.current_hover = [0, 0]
        for i in range(len(self.header)):
            item = self.item(row, i)
            item.setSelected(True)
