import os
import inspect
import pkgutil


class PluginCollection(object):
    """Upon creation, this class will read the add-ons package for modules
    that contain a class definition that is inheriting from the given class
    """

    def __init__(self, plugin_package, plugin_class):
        """Constructor that initiates the reading of all available plugins
        when an instance of the PluginCollection object is created
        """
        self.plugins = []
        self.plugin_class = plugin_class

        self.plugin_package = plugin_package
        self.reload_plugins()

        self._disable = False

    def reload_plugins(self):
        """Reset the list of all plugins and initiate the walk over the main
        provided plugin package to load all available plugins
        """
        self.plugins = []
        self.seen_paths = []
        self.walk_package(self.plugin_package)

    def disable_plugin_manager(self, disable):
        """This method disable/enable the plugin manager

        :param disable: The status of the disable
        :type disable: bool
        """
        if not isinstance(disable, bool):
            return
        self._disable = disable
        if self._disable:
            print("Disable plugin manager")
        else:
            print("Enable plugin manager")
        if not self._disable:
            self.reload_plugins()

    def walk_package(self, package):
        """Recursively walk the supplied package to retrieve all plugins"""
        imported_package = __import__(package, fromlist=["blah"])

        for _, pluginname, ispkg in pkgutil.iter_modules(
            imported_package.__path__, imported_package.__name__ + "."
        ):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=["blah"])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Plugin,
                    # but NOT Plugin itself
                    if issubclass(c, self.plugin_class) & (
                        c is not self.plugin_class
                    ):
                        print(
                            f"Found plugin class: {c.__module__}.{c.__name__}"
                        )
                        self.plugins.append(c())

        # Now that we have looked at all the modules in the current package,
        # start looking recursively for additional modules in sub packages
        all_current_paths = []
        if isinstance(imported_package.__path__, str):
            all_current_paths.append(imported_package.__path__)
        else:
            all_current_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_current_paths:
            if pkg_path not in self.seen_paths:
                self.seen_paths.append(pkg_path)

                # Get all sub directory of the current package path directory
                child_pkgs = [
                    p
                    for p in os.listdir(pkg_path)
                    if os.path.isdir(os.path.join(pkg_path, p))
                ]

                # For each sub directory,
                # apply the walk_package method recursively
                for child_pkg in child_pkgs:
                    self.walk_package(package + "." + child_pkg)
