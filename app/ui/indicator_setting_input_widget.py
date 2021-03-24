# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indicator_setting_input_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.combobox import InputComboBox


class Ui_IndicatorInputSettingWidget(object):
    def setupUi(self, IndicatorInputSettingWidget):
        if not IndicatorInputSettingWidget.objectName():
            IndicatorInputSettingWidget.setObjectName(
                u"IndicatorInputSettingWidget"
            )
        IndicatorInputSettingWidget.resize(400, 55)
        self.verticalLayout = QVBoxLayout(IndicatorInputSettingWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_field_name = QLabel(IndicatorInputSettingWidget)
        self.lab_field_name.setObjectName(u"lab_field_name")
        self.lab_field_name.setMinimumSize(QSize(0, 0))
        self.lab_field_name.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout.addWidget(self.lab_field_name)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cob_value_list = InputComboBox(IndicatorInputSettingWidget)
        self.cob_value_list.setObjectName(u"cob_value_list")

        self.horizontalLayout.addWidget(self.cob_value_list)

        self.spi_value_double = QDoubleSpinBox(IndicatorInputSettingWidget)
        self.spi_value_double.setObjectName(u"spi_value_double")
        self.spi_value_double.setMaximum(9999.989999999999782)

        self.horizontalLayout.addWidget(self.spi_value_double)

        self.spi_value_int = QSpinBox(IndicatorInputSettingWidget)
        self.spi_value_int.setObjectName(u"spi_value_int")
        self.spi_value_int.setMaximum(9999)

        self.horizontalLayout.addWidget(self.spi_value_int)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(IndicatorInputSettingWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.retranslateUi(IndicatorInputSettingWidget)

        QMetaObject.connectSlotsByName(IndicatorInputSettingWidget)

    # setupUi

    def retranslateUi(self, IndicatorInputSettingWidget):
        IndicatorInputSettingWidget.setWindowTitle(
            QCoreApplication.translate(
                "IndicatorInputSettingWidget",
                u"IndicatorInputSettingWidget",
                None,
            )
        )
        self.lab_field_name.setText(
            QCoreApplication.translate(
                "IndicatorInputSettingWidget", u"Field Name", None
            )
        )

    # retranslateUi
