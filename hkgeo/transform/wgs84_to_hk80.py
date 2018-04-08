import numpy as np


def wgs84_to_hk80(lat, lon, unit='d'):
    if unit == 'r':
        lon -= 8.8 / 60**2 * np.pi / 180
        lat += 5.5 / 60**2 * np.pi / 180
    elif unit == 'd':
        lon -= 8.8 / 60**2
        lat += 5.5 / 60**2
    return lat, lon

