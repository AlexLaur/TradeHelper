# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from libs.graph.graphwidget import GraphWidget
from libs.indicators_widget import IndicatorsWidget
from libs.widgets.toolbar import ToolBar
from libs.widgets.stackedwidget import StackedWidget

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.action_reload_indicators = QAction(MainWindow)
        self.action_reload_indicators.setObjectName(
            u"action_reload_indicators"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lie_ticker = QLineEdit(self.centralwidget)
        self.lie_ticker.setObjectName(u"lie_ticker")
        self.lie_ticker.setCursor(QCursor(Qt.PointingHandCursor))
        self.lie_ticker.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.lie_ticker)

        self.stw_main = StackedWidget(self.centralwidget)
        self.stw_main.setObjectName(u"stw_main")
        self.wgt_welcome = QWidget()
        self.wgt_welcome.setObjectName(u"wgt_welcome")
        self.verticalLayout = QVBoxLayout(self.wgt_welcome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.wgt_welcome)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.stw_main.addWidget(self.wgt_welcome)
        self.wgt_graph = GraphWidget()
        self.wgt_graph.setObjectName(u"wgt_graph")
        self.stw_main.addWidget(self.wgt_graph)

        self.verticalLayout_2.addWidget(self.stw_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_wgt_company = QDockWidget(MainWindow)
        self.dock_wgt_company.setObjectName(u"dock_wgt_company")
        self.wgt_company = QWidget()
        self.wgt_company.setObjectName(u"wgt_company")
        self.dock_wgt_company.setWidget(self.wgt_company)
        MainWindow.addDockWidget(
            Qt.BottomDockWidgetArea, self.dock_wgt_company
        )
        self.dock_wgt_indicators = QDockWidget(MainWindow)
        self.dock_wgt_indicators.setObjectName(u"dock_wgt_indicators")
        self.wgt_indicators = IndicatorsWidget()
        self.wgt_indicators.setObjectName(u"wgt_indicators")
        self.dock_wgt_indicators.setWidget(self.wgt_indicators)
        MainWindow.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_wgt_indicators
        )
        self.tool_bar = ToolBar(MainWindow)
        self.tool_bar.setObjectName(u"tool_bar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_reload_indicators)

        self.retranslateUi(MainWindow)

        self.stw_main.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.action_reload_indicators.setText(
            QCoreApplication.translate(
                "MainWindow", u"Reload Indicators", None
            )
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"Select a Ticker.", None)
        )
        self.menuOptions.setTitle(
            QCoreApplication.translate("MainWindow", u"Options", None)
        )
        self.dock_wgt_company.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Company", None)
        )
        self.dock_wgt_indicators.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Indicators", None)
        )
        self.tool_bar.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"toolBar", None)
        )

    # retranslateUi
