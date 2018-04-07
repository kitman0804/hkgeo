"""
Haversine Formula
-----------------
Reference:
http://andrew.hedges.name/experiments/haversine/
https://en.wikipedia.org/wiki/Haversine_formula
"""

import numpy as np

from ._utils import _get_lat_lon
from .. import constants


# Haversine Function
def hav(theta):
    # (sin(x/2))**2 = (1-cos(x)) / 2
    return (1 - np.cos(theta)) / 2


# Inverse Haversine Function
def inv_hav(h):
    return 2 * np.arcsin(np.sqrt(h))


# Haversine Formula
def haversine(latlon0=None, latlon1=None):
    lat0, lon0 = _get_lat_lon(latlon0)
    lat1, lon1 = _get_lat_lon(latlon1)
    d_lat = lat1 - lat0
    d_lon = lon1 - lon0
    h = hav(d_lat) + np.cos(lat0) * np.cos(lat1) * hav(d_lon)
    r = constants.EARTH_PARAMS.get('radius')
    d = inv_hav(h) * r
    return d

