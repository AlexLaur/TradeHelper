import os
import json
from PySide2 import QtWidgets

from resources.style import style
import view

SCRIPT_PATH = os.path.dirname(__file__)


def read_data():
    """Temp function to load all tickers. Should be loaded by a request in the future"""
    data = {}
    with open(os.path.join(SCRIPT_PATH, "data", "dataset.json"), "r") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    data = read_data()

    app = QtWidgets.QApplication([])
    style.dark(app)
    win = view.MainWindow(data=data)
    win.show()
    app.exec_()
