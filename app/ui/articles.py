# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'articles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.label import LabelTitle
from libs.widgets.textbrowser import Description


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 282)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_lb = LabelTitle(Form)
        self.title_lb.setObjectName(u"title_lb")

        self.verticalLayout.addWidget(self.title_lb)

        self.date_lb = QLabel(Form)
        self.date_lb.setObjectName(u"date_lb")

        self.verticalLayout.addWidget(self.date_lb)

        self.descri = Description(Form)
        self.descri.setObjectName(u"descri")

        self.verticalLayout.addWidget(self.descri)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_lb.setText(QCoreApplication.translate("Form", u"Title", None))
        self.date_lb.setText(QCoreApplication.translate("Form", u"Dates", None))
    # retranslateUi

