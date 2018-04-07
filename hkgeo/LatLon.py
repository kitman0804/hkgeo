# -*- coding: utf-8 -*-

from .geometry import Angle
from . import settings


class LatLon(object):
    """
    Parameters
    ----------
    lat: float, default=0
        Latitude.
    lon: float, default=0
        Longitude.
    """
    
    def __init__(self, lat=0, lon=0):
        self._lat = Angle(lat, unit='d')
        self._lon = Angle(lon, unit='d')
    
    def __repr__(self):
        print_text = '({:}N, {:}E)'
        print_text = print_text.format(
            round(self.lat, settings.N_DIGITS),
            round(self.lon, settings.N_DIGITS)
        )
        return print_text
    
    @property
    def lat(self):
        return self._lat
    
    @property
    def lon(self):
        return self._lon
    
    def __eq__(self, other):
        if isinstance(self, LatLon):
            return (self.lat == other.lat) & (self.lon == other.lon)
        else:
            return False
    
    def __ne__(self, other):
        return not (self == other)
    
    def __round__(self, n=None):
        return type(self)(lat=round(self._lat.degree, n), lon=round(self._lon.degree, n))
    
    @property
    def compass(self):
        print_text = '{:}{:}, {:}{:}'
        print_text = print_text.format(
            abs(self._lat), 'N' if self._lat < 0 else 'S',
            abs(self._lon), 'W' if self._lon < 0 else 'E'
        )
        return print_text
    
    def to_tuple(self):
        return (self.lat.degree, self.lon.degree)
