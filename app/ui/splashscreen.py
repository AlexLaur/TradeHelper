# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_splashscreen(object):
    def setupUi(self, splashscreen):
        if not splashscreen.objectName():
            splashscreen.setObjectName(u"splashscreen")
        splashscreen.resize(900, 500)
        self.verticalLayout = QVBoxLayout(splashscreen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lab_app_name = QLabel(splashscreen)
        self.lab_app_name.setObjectName(u"lab_app_name")
        self.lab_app_name.setMinimumSize(QSize(0, 230))
        font = QFont()
        font.setPointSize(18)
        self.lab_app_name.setFont(font)
        self.lab_app_name.setStyleSheet(u"color:#FFFFFF; ")
        self.lab_app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lab_app_name)


        self.retranslateUi(splashscreen)

        QMetaObject.connectSlotsByName(splashscreen)
    # setupUi

    def retranslateUi(self, splashscreen):
        splashscreen.setWindowTitle(QCoreApplication.translate("splashscreen", u"Form", None))
        self.lab_app_name.setText(QCoreApplication.translate("splashscreen", u"app_name", None))
    # retranslateUi

