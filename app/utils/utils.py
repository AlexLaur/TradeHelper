import datetime
import urllib.request
from statistics import mean

from sklearn import preprocessing
import numpy as np
import pandas as pd
from scipy import signal

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication


def normalize_data(data):
    data = data.reshape(1, -1)
    normalized = preprocessing.normalize(np.nan_to_num(data))
    return normalized


def savgol_filter(values, window_length, polyorder=3):
    """Just a savgol filter wrapper

    :param values: The data to be filtered.
    :type values: np.array
    :param window_length: The length of the filter window
    :type window_length: int
    :param polyorder: The order of the polynomial used to fit the samples, defaults to 3
    :type polyorder: int, optional
    :return: The filtered data.
    :rtype: np.array
    """
    return signal.savgol_filter(
        x=values,
        window_length=window_length,
        polyorder=polyorder,
        mode="interp",
    )


def remove_nan(values):
    """Remove NaN from array

    :param values: array of data
    :type values: np.array
    :return: The array without NaN
    :rtype: np.array
    """
    return values[~np.isnan(values)]


def _peaks_detection(values, rounded=3, direction="up"):
    """Peak detection for the given data.

    :param values: All values to analyse
    :type values: np.array
    :param rounded: round values of peaks with n digits, defaults to 3
    :type rounded: int, optional
    :param direction: The direction is use to find peaks.
    Two available choices: (up or down), defaults to "up"
    :type direction: str, optional
    :return: The list of peaks founded
    :rtype: list
    """
    data = np.copy(values)
    if direction == "down":
        data = -data
    peaks, _ = signal.find_peaks(data, height=min(data))
    if rounded:
        peaks = [abs(round(data[val], rounded)) for val in peaks]
    return peaks


def get_resistances(values, closest=2):
    """Get resistances in values

    :param values: Values to analyse
    :type values: np.array
    :param closest: The value for grouping. It represent the max difference
    between values in order to be considering inside the same
    bucket, more the value is small, more the result will be precises.
    defaults to 2
    :type closest: int, optional
    :return: list of values which represents resistances
    :rtype: list
    """
    return _get_support_resistances(
        values=values, direction="up", closest=closest
    )


def get_supports(values, closest=2):
    """Get supports in values

    :param values: Values to analyse
    :type values: np.array
    :param closest: The value for grouping. It represent the max difference
    between values in order to be considering inside the same
    bucket, more the value is small, more the result will be precises.
    defaults to 2
    :type closest: int, optional
    :return: list of values which represents supports
    :rtype: list
    """
    return _get_support_resistances(
        values=values, direction="down", closest=closest
    )


def _get_support_resistances(values, direction, closest=2):
    """Private function which found all supports and resistances

    :param values: values to analyse
    :type values: np.array
    :param direction: The direction (up for resistances, down for supports)
    :type direction: str
    :param closest: closest is the maximun value difference between two values
    in order to be considering in the same bucket, default to 2
    :type closest: int, optional
    :return: The list of support or resistances
    :rtype: list
    """
    result = []
    # Find peaks
    peaks = _peaks_detection(values=values, direction=direction)
    # Group by nearest values
    peaks_grouped = group_values_nearest(values=peaks, closest=closest)
    # Mean all groups in order to have an only one value for each group
    for val in peaks_grouped:
        if not val:
            continue
        if len(val) < 3:  # need 3 values to confirm resistance
            continue
        result.append(mean(val))
    return result


def group_values_nearest(values, closest=2):
    """Group given values together under multiple buckets.

    :param values: values to group
    :type values: list
    :param closest: closest is the maximun value difference between two values
    in order to be considering in the same bucket, defaults to 2
    :type closest: int, optional
    :return: The list of the grouping (list of list)
    :rtype: list    s
    """
    values.sort()
    il = []
    ol = []
    for k, v in enumerate(values):
        if k <= 0:
            continue
        if abs(values[k] - values[k - 1]) < closest:
            if values[k - 1] not in il:
                il.append(values[k - 1])
            if values[k] not in il:
                il.append(values[k])
        else:
            ol.append(list(il))
            il = []
    ol.append(list(il))
    return ol


def find_method(module, obj):
    """Return the method obj for the given string module

    >>> module = "wgt_graph.hello_world"
    >>> obj = self
    >>> find_method(module, obj)
    >>> <bound method ... >

    :param module: The module to find
    :type module: string
    :param obj: The object source
    :type obj: object
    :return: The module found
    :rtype: object
    """
    _module, sep, rest = module.partition(".")
    if getattr(obj, _module, None):
        obj = getattr(obj, _module)
        if sep:
            obj = find_method(module=rest, obj=obj)
    else:
        return None
    return obj


def convert_date_to_timestamp(data):
    final = []
    for date in data.index:
        print(date, type(date))
        _date = datetime.datetime.strptime(date, "%Y-%m-%d")
        timestamp = datetime.datetime.timestamp(_date)
        final.append(timestamp)
    return final


def convert_timestamp_to_date(timestamp: int) -> object:
    """Convert a timestamp to a datetime object

    :param timestamp: The timestamp to convert
    :type timestamp: int
    :return: The datetime resulted from the conversion
    :rtype: object
    """
    return datetime.datetime.fromtimestamp(timestamp)


def get_image_from_url(url: str) -> QPixmap:
    """Get an image on the web and return a Qpixmap

    :param url: The url to request
    :type url: str
    :return: The image
    :rtype: QtGui.QPixmap
    """
    data = urllib.request.urlopen(url).read()
    image = QPixmap()
    image.loadFromData(data)
    return image


def get_main_window_instance(name: str = "MainWindow"):
    """Get the main window object

    :param name: The name of the main window, defaults to "MainWindow"
    :type name: str, optional
    :return: The main window object
    :rtype: object
    """
    top_widgets = QApplication.topLevelWidgets()
    for widget in top_widgets:
        if widget.objectName() != name:
            continue
        return widget
    return None
