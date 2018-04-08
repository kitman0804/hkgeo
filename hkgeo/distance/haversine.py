"""
Haversine Formula
-----------------
Calculate distance between two points.
Reference:
http://andrew.hedges.name/experiments/haversine/
https://en.wikipedia.org/wiki/Haversine_formula
"""

import numpy as np

from .. import constants
from ..LatLon import LatLon


# Haversine Function
def hav(theta):
    # (sin(x/2))**2 = (1-cos(x)) / 2
    return (1 - np.cos(theta)) / 2


# Inverse Haversine Function
def inv_hav(h):
    return 2 * np.arcsin(np.sqrt(h))


# Haversine Formula
def haversine(latlon0, latlon1):
    if not isinstance(latlon0, LatLon):
        latlon0 = LatLon(*latlon0)
    if not isinstance(latlon1, LatLon):
        latlon1 = LatLon(*latlon1)
    
    lat0 = latlon0.lat.radian
    lon0 = latlon0.lon.radian
    lat1 = latlon1.lat.radian
    lon1 = latlon1.lon.radian
    d_lat = lat1 - lat0
    d_lon = lon1 - lon0
    h = hav(d_lat) + np.cos(lat0) * np.cos(lat1) * hav(d_lon)
    r = constants.EARTH_PARAMS.get('radius')
    d = inv_hav(h) * r
    return d

