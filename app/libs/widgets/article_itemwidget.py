from ui.article import Ui_Form
from PySide2 import QtWidgets, QtCore

class ArticlesWidgetItem(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ArticlesWidgetItem, self).__init__(parent)
        self.setupUi(self)

    def set_title(self, text):
        self.lb_title.setText(text)

    def set_date(self, text):
        self.lb_date.setText(text)

    def set_description(self, text):
        self.desc.setText(text)
