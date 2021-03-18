# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.graph.graphwidget import GraphWidget
from libs.indicators_widget import IndicatorsWidget
from libs.widgets.toolbar import ToolBar
from libs.widgets.stackedwidget import StackedWidget
from libs.company_widget import CompanyWidget
from libs.articles_widget import ArticlesWidget
from libs.favorites_widget import FavoritesWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.action_reload_indicators = QAction(MainWindow)
        self.action_reload_indicators.setObjectName(u"action_reload_indicators")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pub_go_welcome = QPushButton(self.centralwidget)
        self.pub_go_welcome.setObjectName(u"pub_go_welcome")
        self.pub_go_welcome.setMinimumSize(QSize(25, 25))
        self.pub_go_welcome.setMaximumSize(QSize(25, 25))
        self.pub_go_welcome.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/svg/keyboard-arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pub_go_welcome.setIcon(icon)
        self.pub_go_welcome.setIconSize(QSize(28, 28))
        self.pub_go_welcome.setFlat(True)

        self.horizontalLayout.addWidget(self.pub_go_welcome)

        self.lie_ticker = QLineEdit(self.centralwidget)
        self.lie_ticker.setObjectName(u"lie_ticker")
        self.lie_ticker.setCursor(QCursor(Qt.PointingHandCursor))
        self.lie_ticker.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lie_ticker)

        self.pub_go_graph = QPushButton(self.centralwidget)
        self.pub_go_graph.setObjectName(u"pub_go_graph")
        self.pub_go_graph.setMinimumSize(QSize(25, 25))
        self.pub_go_graph.setMaximumSize(QSize(25, 25))
        self.pub_go_graph.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/svg/keyboard-arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pub_go_graph.setIcon(icon1)
        self.pub_go_graph.setIconSize(QSize(28, 28))
        self.pub_go_graph.setFlat(True)

        self.horizontalLayout.addWidget(self.pub_go_graph)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stw_main = StackedWidget(self.centralwidget)
        self.stw_main.setObjectName(u"stw_main")
        self.wgt_welcome = QWidget()
        self.wgt_welcome.setObjectName(u"wgt_welcome")
        self.stw_main.addWidget(self.wgt_welcome)
        self.wgt_articles = ArticlesWidget()
        self.wgt_articles.setObjectName(u"wgt_articles")
        self.stw_main.addWidget(self.wgt_articles)
        self.wgt_graph = GraphWidget()
        self.wgt_graph.setObjectName(u"wgt_graph")
        self.wgt_graph.setCursor(QCursor(Qt.CrossCursor))
        self.stw_main.addWidget(self.wgt_graph)

        self.verticalLayout.addWidget(self.stw_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_wgt_company = QDockWidget(MainWindow)
        self.dock_wgt_company.setObjectName(u"dock_wgt_company")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dock_wgt_company.sizePolicy().hasHeightForWidth())
        self.dock_wgt_company.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dock_wgt_company.setFont(font)
        self.wgt_company = CompanyWidget()
        self.wgt_company.setObjectName(u"wgt_company")
        self.dock_wgt_company.setWidget(self.wgt_company)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_wgt_company)
        self.dock_wgt_indicators = QDockWidget(MainWindow)
        self.dock_wgt_indicators.setObjectName(u"dock_wgt_indicators")
        self.dock_wgt_indicators.setFont(font)
        self.wgt_indicators = IndicatorsWidget()
        self.wgt_indicators.setObjectName(u"wgt_indicators")
        self.dock_wgt_indicators.setWidget(self.wgt_indicators)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_wgt_indicators)
        self.tool_bar = ToolBar(MainWindow)
        self.tool_bar.setObjectName(u"tool_bar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.tool_bar)
        self.dock_wgt_favorites = QDockWidget(MainWindow)
        self.dock_wgt_favorites.setObjectName(u"dock_wgt_favorites")
        self.dock_wgt_favorites.setFont(font)
        self.wgt_favorites = FavoritesWidget()
        self.wgt_favorites.setObjectName(u"wgt_favorites")
        self.dock_wgt_favorites.setWidget(self.wgt_favorites)
        MainWindow.addDockWidget(
            Qt.RightDockWidgetArea, self.dock_wgt_favorites
        )

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_reload_indicators)

        self.retranslateUi(MainWindow)

        self.stw_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trade Helper", None))
        self.action_reload_indicators.setText(QCoreApplication.translate("MainWindow", u"Reload Indicators", None))
        self.pub_go_welcome.setText("")
        self.pub_go_graph.setText("")
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
        self.dock_wgt_favorites.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Favorites", None)
        )

    # retranslateUi

