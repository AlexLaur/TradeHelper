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

from libs.widgets.label import LabelTitle
from libs.graph.graphwidget import GraphWidget
from libs.indicators_widget import IndicatorsWidget
from libs.widgets.toolbar import ToolBar
from libs.widgets.stackedwidget import StackedWidget
from libs.company_widget import CompanyWidget
from libs.favorites_widget import FavoritesWidget
from libs.articles_widget import ArticlesWidget
from libs.financial_widget import TableFinance
from libs.welcome_widget import WelcomeWidget
from libs.markets_widget import MarketsWidget
from libs.widgets.sentimentals_widget import Sentimental_Widget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 754)
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
        self.verticalLayout_3 = QVBoxLayout(self.wgt_welcome)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = LabelTitle(self.wgt_welcome)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.pub_go_market_prev = QPushButton(self.wgt_welcome)
        self.pub_go_market_prev.setObjectName(u"pub_go_market_prev")
        self.pub_go_market_prev.setMinimumSize(QSize(25, 25))
        self.pub_go_market_prev.setMaximumSize(QSize(25, 25))
        self.pub_go_market_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.pub_go_market_prev.setIcon(icon)
        self.pub_go_market_prev.setIconSize(QSize(28, 28))
        self.pub_go_market_prev.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pub_go_market_prev)

        self.wgt_markets_2 = MarketsWidget(self.wgt_welcome)
        self.wgt_markets_2.setObjectName(u"wgt_markets_2")
        self.wgt_markets_2.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout_3.addWidget(self.wgt_markets_2)

        self.pub_go_market_next = QPushButton(self.wgt_welcome)
        self.pub_go_market_next.setObjectName(u"pub_go_market_next")
        self.pub_go_market_next.setMinimumSize(QSize(25, 25))
        self.pub_go_market_next.setMaximumSize(QSize(25, 25))
        self.pub_go_market_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.pub_go_market_next.setIcon(icon1)
        self.pub_go_market_next.setIconSize(QSize(28, 28))
        self.pub_go_market_next.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pub_go_market_next)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.wgt_welcome)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.wdg_article_welcome = WelcomeWidget(self.wgt_welcome)
        self.wdg_article_welcome.setObjectName(u"wdg_article_welcome")

        self.horizontalLayout_5.addWidget(self.wdg_article_welcome)

        self.verticalWidget = Sentimental_Widget(self.wgt_welcome)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(0, 0))
        self.verticalWidget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_5.addWidget(self.verticalWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.stw_main.addWidget(self.wgt_welcome)
        self.wgt_article = QWidget()
        self.wgt_article.setObjectName(u"wgt_article")
        self.verticalLayout_2 = QVBoxLayout(self.wgt_article)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = LabelTitle(self.wgt_article)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(self.wgt_article)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.wgt_articles = ArticlesWidget(self.wgt_article)
        self.wgt_articles.setObjectName(u"wgt_articles")

        self.verticalLayout_2.addWidget(self.wgt_articles)

        self.stw_main.addWidget(self.wgt_article)
        self.wgt_graph = GraphWidget()
        self.wgt_graph.setObjectName(u"wgt_graph")
        self.wgt_graph.setCursor(QCursor(Qt.CrossCursor))
        self.stw_main.addWidget(self.wgt_graph)
        self.wgt_financ = QWidget()
        self.wgt_financ.setObjectName(u"wgt_financ")
        self.verticalLayout_4 = QVBoxLayout(self.wgt_financ)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.financial_label = LabelTitle(self.wgt_financ)
        self.financial_label.setObjectName(u"financial_label")
        self.financial_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.financial_label)

        self.financials_layout = QHBoxLayout()
        self.financials_layout.setObjectName(u"financials_layout")

        self.verticalLayout_4.addLayout(self.financials_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.wid_table_financ = TableFinance(self.wgt_financ)
        self.wid_table_financ.setObjectName(u"wid_table_financ")
        self.wid_table_financ.setMinimumSize(QSize(850, 0))
        self.wid_table_financ.setMaximumSize(QSize(850, 16777215))

        self.horizontalLayout_2.addWidget(self.wid_table_financ)

        self.horizontalSpacer_2 = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.stw_main.addWidget(self.wgt_financ)

        self.verticalLayout.addWidget(self.stw_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 21))
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
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_wgt_favorites)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_reload_indicators)

        self.retranslateUi(MainWindow)

        self.stw_main.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trade Helper", None))
        self.action_reload_indicators.setText(QCoreApplication.translate("MainWindow", u"Reload Indicators", None))
        self.pub_go_welcome.setText("")
        self.pub_go_graph.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trading Visualisation", None))
        self.pub_go_market_prev.setText("")
        self.pub_go_market_next.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Related News", None))
        self.financial_label.setText(QCoreApplication.translate("MainWindow", u"Financials", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.dock_wgt_company.setWindowTitle(QCoreApplication.translate("MainWindow", u"Company", None))
        self.dock_wgt_indicators.setWindowTitle(QCoreApplication.translate("MainWindow", u"Indicators", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.dock_wgt_favorites.setWindowTitle(QCoreApplication.translate("MainWindow", u"Favorites", None))
    # retranslateUi

