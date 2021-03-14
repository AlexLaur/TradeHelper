# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tickers_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.treewidget import TickersTreeWidget

import resources_rc


class Ui_TickersDialogWindow(object):
    def setupUi(self, TickersDialogWindow):
        if not TickersDialogWindow.objectName():
            TickersDialogWindow.setObjectName(u"TickersDialogWindow")
        TickersDialogWindow.resize(400, 300)
        self.verticalLayout = QVBoxLayout(TickersDialogWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TickersDialogWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pub_close = QPushButton(TickersDialogWindow)
        self.pub_close.setObjectName(u"pub_close")
        self.pub_close.setMinimumSize(QSize(24, 24))
        self.pub_close.setMaximumSize(QSize(24, 24))
        self.pub_close.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/svg/times.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pub_close.setIcon(icon)
        self.pub_close.setFlat(True)

        self.horizontalLayout.addWidget(self.pub_close)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lie_ticker_search = QLineEdit(TickersDialogWindow)
        self.lie_ticker_search.setObjectName(u"lie_ticker_search")

        self.verticalLayout.addWidget(self.lie_ticker_search)

        self.trw_all_tickers = TickersTreeWidget(TickersDialogWindow)
        self.trw_all_tickers.setObjectName(u"trw_all_tickers")
        self.trw_all_tickers.viewport().setProperty(
            "cursor", QCursor(Qt.PointingHandCursor)
        )
        self.trw_all_tickers.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout.addWidget(self.trw_all_tickers)

        self.retranslateUi(TickersDialogWindow)

        QMetaObject.connectSlotsByName(TickersDialogWindow)

    # setupUi

    def retranslateUi(self, TickersDialogWindow):
        TickersDialogWindow.setWindowTitle(
            QCoreApplication.translate(
                "TickersDialogWindow", u"TickersDialogWindow", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "TickersDialogWindow", u"Ticker search", None
            )
        )
        self.pub_close.setText("")
        ___qtreewidgetitem = self.trw_all_tickers.headerItem()
        ___qtreewidgetitem.setText(
            1,
            QCoreApplication.translate(
                "TickersDialogWindow", u"Company", None
            ),
        )
        ___qtreewidgetitem.setText(
            0,
            QCoreApplication.translate("TickersDialogWindow", u"Ticker", None),
        )

    # retranslateUi
