from pprint import pprint
from libs.thread_pool import ThreadPool
from PySide2 import QtWidgets, QtCore, QtGui
from libs.analysies.analyse_financials import AnalyseFondamental

class QTableWidgetFinance(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(QTableWidgetFinance, self).__init__(parent=parent)
        # cellExited = QtCore.pyqtSignal(int, int)
        # itemExited = QtCore.pyqtSignal(QtWidgets.QTableWidgetItem)

    # def eventFilter(self, widget, event):
    #     item = self.table.item(row, column)
    #     old_item = self.table.item(self.current_hover[0], self.current_hover[1])
    #     if self.current_hover != [row, column]:
    #         old_item.setBackground(QBrush(QColor('white')))
    #         item.setBackground(QBrush(QColor('yellow')))
    #     self.current_hover = [row, column]

class TableFinance(QTableWidgetFinance):
    def __init__(self, parent=None):
        super(TableFinance, self).__init__(parent=parent)
        self.thread_pool = ThreadPool()

    @QtCore.Slot(str)
    def get_financials_table(self, ticker):
        analyses = AnalyseFondamental(ticker)
        self.data = analyses.datas

        # pprint(self.data)

        self.clear()
        header = self.data['YEAR']
        # hearder_len = len(header)
        header.insert(0, 'Valorisation')
        header.insert(len(header), 'Bilan')
        score = self.data["Score"]

        del self.data["YEAR"]
        del self.data["Score"]

        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.horizontalHeader().resizeSection(0, 150)
        self.setColumnWidth(len(header) - 1, 250)
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
                cell.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.setItem(row, column + 1, cell)

            analyse_cell = QtWidgets.QTableWidgetItem()
            analyse_cell.setData(QtCore.Qt.DisplayRole, self.data[title])
            self.setItem(row, 7, analyse_cell)

        # Add Score to the last Row
        last_row = len(self.data)
        self.insertRow(last_row)
        cell_score_title = QtWidgets.QTableWidgetItem()
        cell_score_title.setData(QtCore.Qt.DisplayRole, "Score")
        self.setItem(last_row, 0, cell_score_title)
        cell_score = QtWidgets.QTableWidgetItem()
        cell_score.setData(QtCore.Qt.DisplayRole, str(score[0]))
        cell_score.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.setItem(last_row, len(header)-1, cell_score)

        for i in range(self.rowCount()):
            self.setRowHeight(i, 50)

        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
        self.setMouseTracking(True)
        # self.cellEntered.connect(self.cellHover)

    def cellHover(self, row, column):
        self.current_hover = [0, 0]
        item = self.item(row, column)
        # print(self.itemFromIndex(row))
        print(row)


