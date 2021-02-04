from statistics import mean

import numpy as np
import pandas as pd
from scipy import signal


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


def get_rsi(values, length=14):
    """Relative strength index"""
    # Approximate; good enough
    gain = pd.Series(values).diff()
    loss = gain.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    rs = gain.ewm(length).mean() / loss.abs().ewm(length).mean()
    return (100 - 100 / (1 + rs)).to_numpy()


def remove_nan(values):
    """Remove NaN from array

    :param values: array of data
    :type values: np.array
    :return: The array without NaN
    :rtype: np.array
    """
    return values[~np.isnan(values)]


def rolling_mean(values, length):
    """Find the rolling mean for the given data dans the given length

    :param values: All values to analyse
    :type values: np.array
    :param length: The length to calculate the mean
    :type length: int
    :return: The rolling mean
    :rtype: np.array
    """
    ret = np.cumsum(values, dtype=float)
    ret[length:] = ret[length:] - ret[:-length]
    mva = ret[length - 1 :] / length

    # Padding
    padding = np.array([np.nan for i in range(length)])
    mva = np.append(padding, mva)

    return mva


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
