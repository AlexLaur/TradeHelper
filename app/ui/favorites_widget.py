# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'favorites_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from libs.widgets.treewidget import FavoritesTreeWidget


class Ui_FavoritesWidget(object):
    def setupUi(self, FavoritesWidget):
        if not FavoritesWidget.objectName():
            FavoritesWidget.setObjectName(u"FavoritesWidget")
        FavoritesWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(FavoritesWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lie_search_favorite = QLineEdit(FavoritesWidget)
        self.lie_search_favorite.setObjectName(u"lie_search_favorite")

        self.verticalLayout.addWidget(self.lie_search_favorite)

        self.trw_favorites = FavoritesTreeWidget(FavoritesWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.trw_favorites.setHeaderItem(__qtreewidgetitem)
        self.trw_favorites.setObjectName(u"trw_favorites")
        self.trw_favorites.viewport().setProperty(
            "cursor", QCursor(Qt.PointingHandCursor)
        )
        self.trw_favorites.setSortingEnabled(True)
        self.trw_favorites.header().setVisible(False)

        self.verticalLayout.addWidget(self.trw_favorites)

        self.retranslateUi(FavoritesWidget)

        QMetaObject.connectSlotsByName(FavoritesWidget)

    # setupUi

    def retranslateUi(self, FavoritesWidget):
        FavoritesWidget.setWindowTitle(
            QCoreApplication.translate(
                "FavoritesWidget", u"FavoritesWidget", None
            )
        )
        self.lie_search_favorite.setPlaceholderText(
            QCoreApplication.translate(
                "FavoritesWidget", u"Favorite name...", None
            )
        )

    # retranslateUi
