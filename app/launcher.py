import os
import json
from PySide2 import QtWidgets

from resources.style import style
from libs.yahoo_fin import stock_info as sf
import view

SCRIPT_PATH = os.path.dirname(__file__)


def read_data():
    """Temp function to load all tickers. Should be loaded by a request in the future"""
    data = {}
    try:
        with open(os.path.join(SCRIPT_PATH, "data", "dataset.json"), "r") as f:
            data = json.load(f)
    except:
        dow = sf.tickers_dow()
        cac = sf.tickers_cac()
        sp500 = sf.tickers_sp500()
        nasdaq = sf.tickers_nasdaq()
        for i in [cac, dow, nasdaq, sp500]:
            data.update(i)
        with open(os.path.join(SCRIPT_PATH, "data", "dataset.json", "dataset.json"), "w") as outfile:
            json.dump(data, outfile)

    return data


if __name__ == "__main__":
    data = read_data()

    app = QtWidgets.QApplication([])
    style.dark(app)
    win = view.MainWindow(data=data)
    win.show()
    app.exec_()
