# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'company_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.pushbutton import PushButton

import resources_rc


class Ui_CompanyWidget(object):
    def setupUi(self, CompanyWidget):
        if not CompanyWidget.objectName():
            CompanyWidget.setObjectName(u"CompanyWidget")
        CompanyWidget.resize(642, 224)
        self.verticalLayout_14 = QVBoxLayout(CompanyWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pub_company_logo = PushButton(CompanyWidget)
        self.pub_company_logo.setObjectName(u"pub_company_logo")
        self.pub_company_logo.setMinimumSize(QSize(100, 100))
        self.pub_company_logo.setMaximumSize(QSize(100, 100))
        self.pub_company_logo.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/svg/business.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pub_company_logo.setIcon(icon)
        self.pub_company_logo.setIconSize(QSize(100, 100))
        self.pub_company_logo.setFlat(True)

        self.verticalLayout.addWidget(self.pub_company_logo)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lab_company_name = QLabel(CompanyWidget)
        self.lab_company_name.setObjectName(u"lab_company_name")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lab_company_name.setFont(font)

        self.verticalLayout_3.addWidget(self.lab_company_name)

        self.lab_market_price = QLabel(CompanyWidget)
        self.lab_market_price.setObjectName(u"lab_market_price")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.lab_market_price.setFont(font1)

        self.verticalLayout_3.addWidget(self.lab_market_price)

        self.lab_company_industry = QLabel(CompanyWidget)
        self.lab_company_industry.setObjectName(u"lab_company_industry")

        self.verticalLayout_3.addWidget(self.lab_company_industry)

        self.lab_currency = QLabel(CompanyWidget)
        self.lab_currency.setObjectName(u"lab_currency")

        self.verticalLayout_3.addWidget(self.lab_currency)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line = QFrame(CompanyWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lab_open = QLabel(CompanyWidget)
        self.lab_open.setObjectName(u"lab_open")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.lab_open.setFont(font2)

        self.verticalLayout_4.addWidget(self.lab_open)

        self.lab_open_value = QLabel(CompanyWidget)
        self.lab_open_value.setObjectName(u"lab_open_value")

        self.verticalLayout_4.addWidget(self.lab_open_value)

        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lab_market_day_high = QLabel(CompanyWidget)
        self.lab_market_day_high.setObjectName(u"lab_market_day_high")
        self.lab_market_day_high.setFont(font2)

        self.verticalLayout_5.addWidget(self.lab_market_day_high)

        self.lab_market_day_high_value = QLabel(CompanyWidget)
        self.lab_market_day_high_value.setObjectName(
            u"lab_market_day_high_value"
        )

        self.verticalLayout_5.addWidget(self.lab_market_day_high_value)

        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lab_previous_close = QLabel(CompanyWidget)
        self.lab_previous_close.setObjectName(u"lab_previous_close")
        self.lab_previous_close.setFont(font2)

        self.verticalLayout_6.addWidget(self.lab_previous_close)

        self.lab_previous_close_value = QLabel(CompanyWidget)
        self.lab_previous_close_value.setObjectName(
            u"lab_previous_close_value"
        )

        self.verticalLayout_6.addWidget(self.lab_previous_close_value)

        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lab_market_day_low = QLabel(CompanyWidget)
        self.lab_market_day_low.setObjectName(u"lab_market_day_low")
        self.lab_market_day_low.setFont(font2)

        self.verticalLayout_7.addWidget(self.lab_market_day_low)

        self.lab_market_day_low_value = QLabel(CompanyWidget)
        self.lab_market_day_low_value.setObjectName(
            u"lab_market_day_low_value"
        )

        self.verticalLayout_7.addWidget(self.lab_market_day_low_value)

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_2 = QFrame(CompanyWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lab_volume = QLabel(CompanyWidget)
        self.lab_volume.setObjectName(u"lab_volume")
        self.lab_volume.setFont(font2)

        self.verticalLayout_13.addWidget(self.lab_volume)

        self.lab_volume_value = QLabel(CompanyWidget)
        self.lab_volume_value.setObjectName(u"lab_volume_value")

        self.verticalLayout_13.addWidget(self.lab_volume_value)

        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_3 = QFrame(CompanyWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lab_dividend = QLabel(CompanyWidget)
        self.lab_dividend.setObjectName(u"lab_dividend")
        self.lab_dividend.setFont(font2)

        self.verticalLayout_12.addWidget(self.lab_dividend)

        self.lab_dividend_value = QLabel(CompanyWidget)
        self.lab_dividend_value.setObjectName(u"lab_dividend_value")

        self.verticalLayout_12.addWidget(self.lab_dividend_value)

        self.horizontalLayout_5.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lab_last_dividend = QLabel(CompanyWidget)
        self.lab_last_dividend.setObjectName(u"lab_last_dividend")
        self.lab_last_dividend.setFont(font2)

        self.verticalLayout_11.addWidget(self.lab_last_dividend)

        self.lab_last_dividend_value = QLabel(CompanyWidget)
        self.lab_last_dividend_value.setObjectName(u"lab_last_dividend_value")

        self.verticalLayout_11.addWidget(self.lab_last_dividend_value)

        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lab_last_dividend_date = QLabel(CompanyWidget)
        self.lab_last_dividend_date.setObjectName(u"lab_last_dividend_date")
        self.lab_last_dividend_date.setFont(font2)

        self.verticalLayout_10.addWidget(self.lab_last_dividend_date)

        self.lab_last_dividend_date_value = QLabel(CompanyWidget)
        self.lab_last_dividend_date_value.setObjectName(
            u"lab_last_dividend_date_value"
        )

        self.verticalLayout_10.addWidget(self.lab_last_dividend_date_value)

        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.retranslateUi(CompanyWidget)

        QMetaObject.connectSlotsByName(CompanyWidget)

    # setupUi

    def retranslateUi(self, CompanyWidget):
        CompanyWidget.setWindowTitle(
            QCoreApplication.translate("CompanyWidget", u"CompanyWidget", None)
        )
        self.pub_company_logo.setText("")
        self.lab_company_name.setText(
            QCoreApplication.translate("CompanyWidget", u"Company", None)
        )
        self.lab_market_price.setText(
            QCoreApplication.translate("CompanyWidget", u"Market price", None)
        )
        self.lab_company_industry.setText(
            QCoreApplication.translate("CompanyWidget", u"Industry", None)
        )
        self.lab_currency.setText(
            QCoreApplication.translate("CompanyWidget", u"Currency", None)
        )
        self.lab_open.setText(
            QCoreApplication.translate("CompanyWidget", u"Opening", None)
        )
        self.lab_open_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_market_day_high.setText(
            QCoreApplication.translate("CompanyWidget", u"Day High", None)
        )
        self.lab_market_day_high_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_previous_close.setText(
            QCoreApplication.translate(
                "CompanyWidget", u"Previous close", None
            )
        )
        self.lab_previous_close_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_market_day_low.setText(
            QCoreApplication.translate("CompanyWidget", u"Day Low", None)
        )
        self.lab_market_day_low_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_volume.setText(
            QCoreApplication.translate("CompanyWidget", u"Volume", None)
        )
        self.lab_volume_value.setText(
            QCoreApplication.translate("CompanyWidget", u"0", None)
        )
        self.lab_dividend.setText(
            QCoreApplication.translate(
                "CompanyWidget", u"Dividend Value", None
            )
        )
        self.lab_dividend_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_last_dividend.setText(
            QCoreApplication.translate(
                "CompanyWidget", u"Last Dividend Value", None
            )
        )
        self.lab_last_dividend_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )
        self.lab_last_dividend_date.setText(
            QCoreApplication.translate(
                "CompanyWidget", u"Last Dividend Date", None
            )
        )
        self.lab_last_dividend_date_value.setText(
            QCoreApplication.translate("CompanyWidget", u"00.00", None)
        )

    # retranslateUi
