# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'markets_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_markets(object):
    def setupUi(self, markets):
        if not markets.objectName():
            markets.setObjectName(u"markets")
        markets.resize(125, 80)
        markets.setMinimumSize(QSize(125, 80))
        markets.setMaximumSize(QSize(125, 80))
        self.horizontalLayout = QHBoxLayout(markets)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(markets)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(12)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title)

        self.price = QLabel(markets)
        self.price.setObjectName(u"price")
        font1 = QFont()
        font1.setPointSize(10)
        self.price.setFont(font1)

        self.verticalLayout.addWidget(self.price)

        self.pourcentage = QLabel(markets)
        self.pourcentage.setObjectName(u"pourcentage")
        self.pourcentage.setFont(font1)

        self.verticalLayout.addWidget(self.pourcentage)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(markets)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)


        self.retranslateUi(markets)

        QMetaObject.connectSlotsByName(markets)
    # setupUi

    def retranslateUi(self, markets):
        markets.setWindowTitle(QCoreApplication.translate("markets", u"Form", None))
        self.title.setText(QCoreApplication.translate("markets", u"Markets", None))
        self.price.setText(QCoreApplication.translate("markets", u"Price", None))
        self.pourcentage.setText(QCoreApplication.translate("markets", u"%", None))
    # retranslateUi

