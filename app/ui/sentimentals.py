# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sentimentals.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Sentiment_Form(object):
    def setupUi(self, Sentiment_Form):
        if not Sentiment_Form.objectName():
            Sentiment_Form.setObjectName(u"Sentiment_Form")
        Sentiment_Form.resize(300, 90)
        Sentiment_Form.setMaximumSize(QSize(300, 90))
        self.verticalLayout = QVBoxLayout(Sentiment_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Sentiment_Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(16777215, 80))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(Sentiment_Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(Sentiment_Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(Sentiment_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(Sentiment_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(Sentiment_Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSlider = QSlider(Sentiment_Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.retranslateUi(Sentiment_Form)

        QMetaObject.connectSlotsByName(Sentiment_Form)
    # setupUi

    def retranslateUi(self, Sentiment_Form):
        Sentiment_Form.setWindowTitle(QCoreApplication.translate("Sentiment_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Sentiment_Form", u"Compagny", None))
        self.label_6.setText(QCoreApplication.translate("Sentiment_Form", u"Strong Sell", None))
        self.label_7.setText(QCoreApplication.translate("Sentiment_Form", u"Sell", None))
        self.label_8.setText(QCoreApplication.translate("Sentiment_Form", u"Neutral", None))
        self.label_9.setText(QCoreApplication.translate("Sentiment_Form", u"Buy", None))
        self.label_10.setText(QCoreApplication.translate("Sentiment_Form", u"Strong Buy", None))
    # retranslateUi

