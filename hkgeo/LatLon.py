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
        if isinstance(lat, Angle):
            self._lat = lat.to_deg()
        elif isinstance(lat, (int, float)):
            self._lat = Angle(lat, unit='deg')
        else:
            raise TypeError('lat must be an Angle, int or float.')
        if isinstance(lon, Angle):
            self._lon = lon.to_deg()
        elif isinstance(lon, (int, float)):
            self._lon = Angle(lon, unit='deg')
        else:
            raise TypeError('lon must be an Angle, int or float.')
    
    def __repr__(self):
        print_text = '({:}N, {:}E)'.format(
            round(self._lat, settings.N_DIGITS),
            round(self._lon, settings.N_DIGITS))
        return print_text
    
    @property
    def lat(self):
        return self._lat
    
    @property
    def lon(self):
        return self._lon
    
    def __eq__(self, other):
        if isinstance(self, type(self)):
            return (self.lat == other.lat) & (self.lon == other.lon)
        else:
            return False
    
    def __ne__(self, other):
        return not (self == other)
    
    def __round__(self, n=None):
        return type(self)(lat=round(self._lat.degree, n), lon=round(self._lon.degree, n))
    
    @property
    def compass(self):
        print_text = '{:}{:}, {:}{:}'.format(
            abs(self._lat), 'N' if self._lat < 0 else 'S',
            abs(self._lon), 'W' if self._lon < 0 else 'E')
        return print_text
    
    def to_tuple(self):
        return (self._lat.degree, self._lon.degree)
