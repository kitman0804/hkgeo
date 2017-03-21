# -*- coding: utf-8 -*-

import numpy as np

from .hk80g_to_hk80 import hk80g_to_hk80
from .hk80_to_wgs84 import hk80_to_to_wgs84


def hk80g_to_to_wgs84(E, N, unit='d'):
    lat, lon = hk80g_to_hk80(E=E, N=N, unit=unit)
    lat, lon = hk80_to_to_wgs84(lat=lat, lon=lon, unit=unit)
    return lat, lon

