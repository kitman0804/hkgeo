import numpy as np

from ..LatLon import LatLon


def _get_lat_lon(latlon):
    """
    Obtain Latitude & Lontitude in radian
    """
    if isinstance(latlon, LatLon):
        lat = latlon.lat.radian
        lon = latlon.lon.radian
        return lat, lon
    elif isinstance(latlon, (tuple, list)):
        if len(latlon) == 2:
            if isinstance(latlon[0], (int, float)):
                lat = latlon[0] * np.pi / 180
            else:
                raise TypeError('lat must be a number.')
            if isinstance(latlon[1], (int, float)):
                lon = latlon[1] * np.pi / 180
            else:
                raise TypeError('lon must be a number.')
        else:
            raise IndexError('latlon must be of length of 2.')
    else:
        raise TypeError('latlon0 must be a LatLon object or tuple or list.')

