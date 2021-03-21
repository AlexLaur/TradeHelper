from PySide2 import QtWidgets, QtGui, QtCore


class Description(QtWidgets.QTextEdit):
    def __init__(self, text):
        super(Description, self).__init__()
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        size_policy = self.sizePolicy()
        document = self.document()
        margins = self.contentsMargins()
        # document_width = size_policy - margins.left() - margins.right()
        # print(QtCore.QSize(size_policy))
        # print(document.setTextWidth(document_width))

        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)

        self.setFixedHeight(self.document().size().height() + self.contentsMargins().top() * 2)

        if text:
            self.setText("text")
            self.setFont(QtGui.QFont("Times", 10))
