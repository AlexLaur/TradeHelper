from statistics import mean

import numpy as np

from scipy import signal


def rolling_mean(values, lenght):
    """Find the rolling mean for the given data dans the given lenght

    :param values: All values to analyse
    :type values: np.array
    :param lenght: The lenght to calculate the mean
    :type lenght: int
    :return: The rolling mean
    :rtype: np.array
    """
    ret = np.cumsum(values, dtype=float)
    ret[lenght:] = ret[lenght:] - ret[:-lenght]
    return ret[lenght - 1:] / lenght

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


def get_resistances(values):
    resistances = []
    # Find peaks
    peaks = _peaks_detection(values=values, direction="up")
    # Group by nearest values
    peaks_grouped = group_values_nearest(values=peaks)
    # Mean all groups in order to have an only one value for each group
    for val in peaks_grouped:
        if not val:
            continue
        if len(val) < 3: # need 3 values to confirm resistance
            continue
        resistances.append(mean(val))
    return resistances


def get_supports(values):
    supports = []
    # Find peaks
    peaks = _peaks_detection(values=values, direction="down")
    # Group by nearest values
    peaks_grouped = group_values_nearest(values=peaks)
    # Mean all groups in order to have an only one value for each group
    for val in peaks_grouped:
        if not val:
            continue
        if len(val) < 3: # need 3 values to confirm resistance
            continue
        supports.append(mean(val))
    return supports

def group_values_nearest(values):
    # values.sort()
    il = []
    ol = []
    for k, v in enumerate(values):
        if k <= 0:
            continue
        if abs(values[k] - values[k-1]) < 3:
            if values[k-1] not in il:
                il.append(values[k-1])
            if values[k] not in il:
                il.append(values[k])
        else:
            ol.append(list(il))
            il = []
    ol.append(list(il))
    return ol
