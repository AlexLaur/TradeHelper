import os
import json

from PySide2 import QtCore, QtGui, QtWidgets
import qtawesome as qta

from libs.events_handler import EventHandler
import resources_rc


class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super(ToolBar, self).__init__(parent=parent)

        # CONSTANTS
        self.signals = EventHandler()
        self._actions = []

        self.setIconSize(QtCore.QSize(20, 20))
        self.toolbar_settings_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "resources",
            "toolbar",
            "toolbar.json",
        )
        # TODO Use resrouces and QFile

    def _trigger_action(self):
        """Called on action triggered"""
        sender = self.sender()
        self.signals.sig_action_triggered.emit(sender.action, sender.args)

    def init_toolbar(self):
        """This method inits the toolbar of the app"""
        toolbar_items = self.open_toolbar_settings()
        self.create_menu(menu_recipe=toolbar_items, parent=self)

    def create_menu(self, menu_recipe: list, parent: object, depth: int = 0):
        """This method create the menu of the toolbar

        :param menu_recipe: [description]
        :type menu_recipe: list
        :param parent: [description], defaults to None
        :type parent: [type], optional
        :param depth: [description], defaults to 0
        :type depth: int, optional
        """
        for item in menu_recipe:
            if item.get("type") == "separator":
                parent.addSeparator()
                continue

            submenu = item.pop("submenu", None)
            icon = self.get_icon(icon=item.pop("icon", None))

            # Need submenu
            if submenu:
                if depth == 0:
                    # First level, so create ToolButton with a linked menu
                    _btn = ToolButton(parent=parent, icon=icon, **item)
                    parent.addWidget(_btn)

                    menu = Menu(parent=_btn, **item)
                    _btn.setMenu(menu)
                else:
                    # Not first level, the parent is a menu
                    menu = Menu(
                        parent=parent,
                        icon=icon,
                        title=item.get("text"),
                        **item
                    )
                    parent.addMenu(menu)
                # Call the method itself to continue the creation of submenus
                self.create_menu(
                    menu_recipe=submenu, parent=menu, depth=depth + 1
                )

            # No need submenu
            else:
                btn = Action(parent=parent, icon=icon, **item)
                btn.triggered.connect(self._trigger_action)
                parent.addAction(btn)
                self._actions.append(btn)

    def open_toolbar_settings(self) -> list:
        """This method loads the json content for toolbar items

        :return: The list of actions to create
        :rtype: list
        """
        if os.path.exists(self.toolbar_settings_file):
            with open(self.toolbar_settings_file, "r") as f:
                data = json.load(f)
            return data
        print("%s doesn't exists" % self.toolbar_settings_file)
        return []

    def get_actions(self) -> list:
        """Get all actions which can be triggered in the toolbar

        :return: List of all actions
        :rtype: list
        """
        return self._actions

    def get_icon(self, icon: dict) -> QtGui.QIcon:
        """Get the icon for the given icon from the toolbar config

        :param icon: The icon from the config
        :type icon: dict
        :return: The icon
        :rtype: QtGui.QIcon
        """
        if not icon:
            return icon
        if not isinstance(icon, dict):
            return None
        icon_type = icon.get("type", None)
        icon_value = icon.get("value")
        icon_options = icon.get("options", [{}])
        if icon_type not in ["font", "resources"]:
            return None
        if icon_type == "font":
            return qta.icon(icon_value, options=icon_options)
        else:
            # resources
            return QtGui.QIcon(icon_value)


class Action(QtWidgets.QAction):
    def __init__(self, parent=None, text=None, action=None, **kwargs):
        super(Action, self).__init__(parent, text=text)

        self.__dict__.update(kwargs)

        # Properties
        self.action = action
        self.args = kwargs.get("args", {})

        icon = kwargs.get("icon", None)
        if icon:
            self.setIcon(icon)

        checkable = kwargs.get("checkable", False)
        self.setCheckable(checkable)

        shortcut = kwargs.get("shortcut", None)
        if shortcut:
            sequence = QtGui.QKeySequence(shortcut)
            self.setShortcut(sequence)

        tooltip = kwargs.get("tooltip", None)
        if tooltip:
            self.setToolTip(tooltip)


class Menu(QtWidgets.QMenu):
    def __init__(self, parent=None, title=None, *args, **kwargs):
        super(Menu, self).__init__(parent=parent, title=title)

        self.__dict__.update(kwargs)

        icon = kwargs.get("icon", None)
        if icon:
            self.setIcon(icon)

        tooltip = kwargs.get("tooltip", None)
        if tooltip:
            self.setToolTip(tooltip)


class ToolButton(QtWidgets.QToolButton):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(ToolButton, self).__init__(parent=parent, text=text)

        self.__dict__.update(kwargs)

        self.setPopupMode(QtWidgets.QToolButton.InstantPopup)

        icon = kwargs.get("icon", None)
        if icon:
            self.setIcon(icon)

        tooltip = kwargs.get("tooltip", None)
        if tooltip:
            self.setToolTip(tooltip)
