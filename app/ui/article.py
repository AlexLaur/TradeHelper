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


class Ui_Article(object):
    def setupUi(self, Article):
        if not Article.objectName():
            Article.setObjectName(u"Article")
        Article.resize(638, 219)
        self.verticalLayout_2 = QVBoxLayout(Article)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.thumbnail = QLabel(Article)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setMinimumSize(QSize(250, 150))
        self.thumbnail.setMaximumSize(QSize(250, 150))

        self.horizontalLayout.addWidget(self.thumbnail)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = LabelTitle(Article)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout.addWidget(self.lb_title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_compagny = QLabel(Article)
        self.lb_compagny.setObjectName(u"lb_compagny")
        self.lb_compagny.setMinimumSize(QSize(0, 25))
        self.lb_compagny.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.lb_compagny)

        self.lb_date = QLabel(Article)
        self.lb_date.setObjectName(u"lb_date")
        self.lb_date.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.lb_date)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.desc = QLabel(Article)
        self.desc.setObjectName(u"desc")
        self.desc.setMinimumSize(QSize(175, 0))

        self.verticalLayout.addWidget(self.desc)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(Article)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)


        self.retranslateUi(Article)

        QMetaObject.connectSlotsByName(Article)
    # setupUi

    def retranslateUi(self, Article):
        Article.setWindowTitle(QCoreApplication.translate("Article", u"Form", None))
        self.thumbnail.setText("")
        self.lb_title.setText(QCoreApplication.translate("Article", u"Title", None))
        self.lb_compagny.setText("")
        self.lb_date.setText(QCoreApplication.translate("Article", u"date", None))
        self.desc.setText(QCoreApplication.translate("Article", u"desc", None))
    # retranslateUi

