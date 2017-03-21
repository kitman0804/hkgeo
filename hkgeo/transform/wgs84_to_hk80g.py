# -*- coding: utf-8 -*-

from .wgs84_to_hk80 import wgs84_to_hk80
from .hk80_to_hk80g import hk80_to_hk80g


def wgs84_to_hk80g(lat, lon, unit='d'):
    lat, lon = wgs84_to_hk80(lat=lat, lon=lon, unit=unit)
    E, N = hk80_to_hk80g(lat=lat, lon=lon, unit=unit)
    return E, N

