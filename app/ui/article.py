# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'article.ui'
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
        Form.resize(400, 295)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = LabelTitle(Form)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout.addWidget(self.lb_title)

        self.lb_date = QLabel(Form)
        self.lb_date.setObjectName(u"lb_date")

        self.verticalLayout.addWidget(self.lb_date)

        self.desc = Description(Form)
        self.desc.setObjectName(u"desc")

        self.verticalLayout.addWidget(self.desc)

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
        self.lb_title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.lb_date.setText(QCoreApplication.translate("Form", u"date", None))
    # retranslateUi

