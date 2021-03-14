# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_ticker_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_WelcomeTickerWidget(object):
    def setupUi(self, WelcomeTickerWidget):
        if not WelcomeTickerWidget.objectName():
            WelcomeTickerWidget.setObjectName(u"WelcomeTickerWidget")
        WelcomeTickerWidget.resize(150, 150)
        self.verticalLayout = QVBoxLayout(WelcomeTickerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lab_ticker_img = QLabel(WelcomeTickerWidget)
        self.lab_ticker_img.setObjectName(u"lab_ticker_img")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_ticker_img.sizePolicy().hasHeightForWidth()
        )
        self.lab_ticker_img.setSizePolicy(sizePolicy)
        self.lab_ticker_img.setPixmap(QPixmap(u":/svg/anchored-vwap.svg"))
        self.lab_ticker_img.setScaledContents(False)
        self.lab_ticker_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lab_ticker_img)

        self.lab_ticker_name = QLabel(WelcomeTickerWidget)
        self.lab_ticker_name.setObjectName(u"lab_ticker_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.lab_ticker_name.sizePolicy().hasHeightForWidth()
        )
        self.lab_ticker_name.setSizePolicy(sizePolicy1)
        self.lab_ticker_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lab_ticker_name)

        self.retranslateUi(WelcomeTickerWidget)

        QMetaObject.connectSlotsByName(WelcomeTickerWidget)

    # setupUi

    def retranslateUi(self, WelcomeTickerWidget):
        WelcomeTickerWidget.setWindowTitle(
            QCoreApplication.translate(
                "WelcomeTickerWidget", u"WelcomeTickerWidget", None
            )
        )
        self.lab_ticker_img.setText("")
        self.lab_ticker_name.setText(
            QCoreApplication.translate(
                "WelcomeTickerWidget", u"Ticker Name", None
            )
        )

    # retranslateUi
