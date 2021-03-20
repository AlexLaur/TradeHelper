# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicator_settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_IndicatorSettingsDialogWindow(object):
    def setupUi(self, IndicatorSettingsDialogWindow):
        if not IndicatorSettingsDialogWindow.objectName():
            IndicatorSettingsDialogWindow.setObjectName(
                u"IndicatorSettingsDialogWindow"
            )
        IndicatorSettingsDialogWindow.resize(400, 300)
        self.verticalLayout = QVBoxLayout(IndicatorSettingsDialogWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_settings = QTabWidget(IndicatorSettingsDialogWindow)
        self.tab_settings.setObjectName(u"tab_settings")
        self.wgt_settings_input = QWidget()
        self.wgt_settings_input.setObjectName(u"wgt_settings_input")
        self.verticalLayout_3 = QVBoxLayout(self.wgt_settings_input)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.wgt_settings_input)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.wgt_inputs = QWidget()
        self.wgt_inputs.setObjectName(u"wgt_inputs")
        self.wgt_inputs.setGeometry(QRect(0, 0, 358, 189))
        self.scrollArea.setWidget(self.wgt_inputs)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.tab_settings.addTab(self.wgt_settings_input, "")
        self.wgt_settings_styles = QWidget()
        self.wgt_settings_styles.setObjectName(u"wgt_settings_styles")
        self.verticalLayout_2 = QVBoxLayout(self.wgt_settings_styles)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.wgt_settings_styles)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.wgt_styles = QWidget()
        self.wgt_styles.setObjectName(u"wgt_styles")
        self.wgt_styles.setGeometry(QRect(0, 0, 358, 189))
        self.scrollArea_2.setWidget(self.wgt_styles)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tab_settings.addTab(self.wgt_settings_styles, "")

        self.verticalLayout.addWidget(self.tab_settings)

        self.line = QFrame(IndicatorSettingsDialogWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pub_reset = QPushButton(IndicatorSettingsDialogWindow)
        self.pub_reset.setObjectName(u"pub_reset")

        self.horizontalLayout.addWidget(self.pub_reset)

        self.pub_cancel = QPushButton(IndicatorSettingsDialogWindow)
        self.pub_cancel.setObjectName(u"pub_cancel")

        self.horizontalLayout.addWidget(self.pub_cancel)

        self.pub_ok = QPushButton(IndicatorSettingsDialogWindow)
        self.pub_ok.setObjectName(u"pub_ok")

        self.horizontalLayout.addWidget(self.pub_ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(IndicatorSettingsDialogWindow)

        self.tab_settings.setCurrentIndex(0)
        self.pub_ok.setDefault(True)

        QMetaObject.connectSlotsByName(IndicatorSettingsDialogWindow)

    # setupUi

    def retranslateUi(self, IndicatorSettingsDialogWindow):
        IndicatorSettingsDialogWindow.setWindowTitle(
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow",
                u"IndicatorSettingsDialogWindow",
                None,
            )
        )
        self.tab_settings.setTabText(
            self.tab_settings.indexOf(self.wgt_settings_input),
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow", u"Input", None
            ),
        )
        self.tab_settings.setTabText(
            self.tab_settings.indexOf(self.wgt_settings_styles),
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow", u"Style", None
            ),
        )
        self.pub_reset.setText(
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow", u"Reset values", None
            )
        )
        self.pub_cancel.setText(
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow", u"Cancel", None
            )
        )
        self.pub_ok.setText(
            QCoreApplication.translate(
                "IndicatorSettingsDialogWindow", u"Ok", None
            )
        )

    # retranslateUi
