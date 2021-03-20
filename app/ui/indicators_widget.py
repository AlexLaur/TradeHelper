# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicators_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.tablewidget import IndicatorsTableWidget


class Ui_IndicatorsWidget(object):
    def setupUi(self, IndicatorsWidget):
        if not IndicatorsWidget.objectName():
            IndicatorsWidget.setObjectName(u"IndicatorsWidget")
        IndicatorsWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(IndicatorsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lie_indicators_search = QLineEdit(IndicatorsWidget)
        self.lie_indicators_search.setObjectName(u"lie_indicators_search")

        self.verticalLayout.addWidget(self.lie_indicators_search)

        self.tab_indicators = IndicatorsTableWidget(IndicatorsWidget)
        if self.tab_indicators.columnCount() < 3:
            self.tab_indicators.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_indicators.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_indicators.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_indicators.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tab_indicators.setObjectName(u"tab_indicators")
        self.tab_indicators.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_indicators.setAlternatingRowColors(True)
        self.tab_indicators.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_indicators.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tab_indicators)

        self.retranslateUi(IndicatorsWidget)

        QMetaObject.connectSlotsByName(IndicatorsWidget)

    # setupUi

    def retranslateUi(self, IndicatorsWidget):
        IndicatorsWidget.setWindowTitle(
            QCoreApplication.translate(
                "IndicatorsWidget", u"IndicatorsWidget", None
            )
        )
        self.lie_indicators_search.setPlaceholderText(
            QCoreApplication.translate(
                "IndicatorsWidget", u"Average Mean", None
            )
        )
        ___qtablewidgetitem = self.tab_indicators.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("IndicatorsWidget", u"Name", None)
        )

    # retranslateUi
