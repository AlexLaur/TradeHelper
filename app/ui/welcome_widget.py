# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WelcomeWidget(object):
    def setupUi(self, WelcomeWidget):
        if not WelcomeWidget.objectName():
            WelcomeWidget.setObjectName(u"WelcomeWidget")
        WelcomeWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(WelcomeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lab_label = QLabel(WelcomeWidget)
        self.lab_label.setObjectName(u"lab_label")

        self.verticalLayout.addWidget(self.lab_label)

        self.scr_area = QScrollArea(WelcomeWidget)
        self.scr_area.setObjectName(u"scr_area")
        self.scr_area.setWidgetResizable(True)
        self.wgt_welcome_content = QWidget()
        self.wgt_welcome_content.setObjectName(u"wgt_welcome_content")
        self.wgt_welcome_content.setGeometry(QRect(0, 0, 380, 257))
        self.scr_area.setWidget(self.wgt_welcome_content)

        self.verticalLayout.addWidget(self.scr_area)

        self.retranslateUi(WelcomeWidget)

        QMetaObject.connectSlotsByName(WelcomeWidget)

    # setupUi

    def retranslateUi(self, WelcomeWidget):
        WelcomeWidget.setWindowTitle(
            QCoreApplication.translate("WelcomeWidget", u"WelcomeWidget", None)
        )
        self.lab_label.setText(
            QCoreApplication.translate(
                "WelcomeWidget", u"Get a rapid access.", None
            )
        )

    # retranslateUi
