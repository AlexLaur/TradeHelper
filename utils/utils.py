from statistics import mean

from scipy import signal
from peakdetect import peakdetect

def get_resistances(values):
    resistances = []
    # Find peaks
    peaks, _ = signal.find_peaks(values, height=min(values), distance=2)
    # Round all values with 3 digits after comma.
    peaks_rounded = [round(values[val], 3) for val in peaks]
    # Group by nearest values
    peaks_grouped = group_values_nearest(values=peaks_rounded)
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
    _, peaks = peakdetect(values, lookahead=5)
    peaks = [x[1] for x in peaks]
    # Round all values with 3 digits after comma.
    peaks_rounded = [round(x, 3) for x in peaks]
    # Group by nearest values
    peaks_grouped = group_values_nearest(values=peaks_rounded)
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
