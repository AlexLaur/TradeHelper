# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicator_setting_style_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.combobox import StyleComboBox


class Ui_IndicatorStyleSettingWidget(object):
    def setupUi(self, IndicatorStyleSettingWidget):
        if not IndicatorStyleSettingWidget.objectName():
            IndicatorStyleSettingWidget.setObjectName(
                u"IndicatorStyleSettingWidget"
            )
        IndicatorStyleSettingWidget.resize(412, 55)
        self.verticalLayout_2 = QVBoxLayout(IndicatorStyleSettingWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_field_name = QLabel(IndicatorStyleSettingWidget)
        self.lab_field_name.setObjectName(u"lab_field_name")
        self.lab_field_name.setMinimumSize(QSize(0, 0))
        self.lab_field_name.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout.addWidget(self.lab_field_name)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pub_color = QPushButton(IndicatorStyleSettingWidget)
        self.pub_color.setObjectName(u"pub_color")
        self.pub_color.setMinimumSize(QSize(50, 25))
        self.pub_color.setMaximumSize(QSize(50, 25))
        self.pub_color.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pub_color)

        self.cob_line_style = StyleComboBox(IndicatorStyleSettingWidget)
        self.cob_line_style.setObjectName(u"cob_line_style")
        self.cob_line_style.setMaximumSize(QSize(50, 16777215))
        self.cob_line_style.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.cob_line_style)

        self.spi_line_width = QDoubleSpinBox(IndicatorStyleSettingWidget)
        self.spi_line_width.setObjectName(u"spi_line_width")
        self.spi_line_width.setMaximum(999.000000000000000)

        self.horizontalLayout.addWidget(self.spi_line_width)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(IndicatorStyleSettingWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.retranslateUi(IndicatorStyleSettingWidget)

        self.pub_color.setDefault(False)

        QMetaObject.connectSlotsByName(IndicatorStyleSettingWidget)

    # setupUi

    def retranslateUi(self, IndicatorStyleSettingWidget):
        IndicatorStyleSettingWidget.setWindowTitle(
            QCoreApplication.translate(
                "IndicatorStyleSettingWidget",
                u"IndicatorStyleSettingWidget",
                None,
            )
        )
        self.lab_field_name.setText(
            QCoreApplication.translate(
                "IndicatorStyleSettingWidget", u"Field Name", None
            )
        )
        self.pub_color.setText("")

    # retranslateUi
