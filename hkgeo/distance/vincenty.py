# -*- coding: utf-8 -*-

"""
Vincenty's formulae

Reference:
https://en.wikipedia.org/wiki/Vincenty%27s_formulae
http://www.movable-type.co.uk/scripts/latlong-vincenty.html
http://www.ga.gov.au/scientific-topics/positioning-navigation/geodesy/geodetic-techniques/distance-calculation-algorithms
"""

import numpy as np

from .. import constants
from ..LatLon import LatLon


def vincenty(latlon0=None, latlon1=None, lat0=None, lon0=None, lat1=None, lon1=None, 
             tol=1e-12, max_iter=100):
    if isinstance(latlon0, LatLon):
        lat0 = latlon0.lat.radian
        lon0 = latlon0.lon.radian
    else:
        if isinstance(lat0, (int, float)):
            lat0 *= np.pi / 180
        if isinstance(lon0, (int, float)):
            lon0 *= np.pi / 180
    if isinstance(latlon1, LatLon):
        lat1 = latlon1.lat.radian
        lon1 = latlon1.lon.radian
    else:
        if isinstance(lat1, (int, float)):
            lat1 *= np.pi / 180
        if isinstance(lon1, (int, float)):
            lon1 *= np.pi / 180
    args = [('lat0', lat0), ('lon0', lon0), ('lat1', lat1), ('lon1', lon1)]
    if None in [x for _, x in args]:
        msg = 'Missing {:}'.format(', '.join(name for name, x in args if x is None))
        raise ValueError(msg)
    if (lat0 == lat1) & (lon0 == lon1):
        return 0
    # Some constants for WGS 84
    a, f = constants.WGS84_PARAMS.get('a'), constants.WGS84_PARAMS.get('f')
    b = (1 - f) * a
    
    tan_u1, tan_u2 = (1 - f) * np.tan(lat0), (1 - f) * np.tan(lat1)
    cos_u1, cos_u2 = 1 / np.sqrt(1 + tan_u1**2), 1 / np.sqrt(1 + tan_u2**2)
    sin_u1, sin_u2 = tan_u1 * cos_u1, tan_u2 * cos_u2
    delta_lon = lon1 - lon0
    lambda0, lambda1 = (delta_lon,) * 2
    i = 0
    while (abs(lambda0 - lambda1) > tol) | (i == 0):
        if i >= max_iter:
            print('100 iterations were done, but lambda has not converged yet.')
            break
        lambda0 = lambda1
        sin_lambda, cos_lambda = np.sin(lambda0), np.cos(lambda0)
        # sigma
        sin_sigma = np.sqrt((cos_u2 * sin_lambda)**2 + (cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lambda)**2)
        cos_sigma = sin_u1 * sin_u2 + cos_u1 * cos_u2 * cos_lambda
        sigma = np.arctan(sin_sigma / cos_sigma)
        # alpha
        sin_alpha = (cos_u1 * cos_u2 * sin_lambda) / sin_sigma
        cos_alpha_sq = 1 - sin_alpha**2
        # 2 * sigma
        cos_2sigma_m = cos_sigma - (2 * sin_u1 * sin_u2) / cos_alpha_sq
        # c
        c = f / 16 * cos_alpha_sq * (4 + f * (4 - 3 * cos_alpha_sq))
        # lambda1
        lambda1 = (
            delta_lon
            + (1 - c) * f * sin_alpha
            * (sigma + c * sin_sigma * (cos_2sigma_m + c * cos_sigma * (-1 + 2 * cos_2sigma_m**2)))
        )
        i += 1
    # Final
    u_sq = cos_alpha_sq * (a**2 - b**2) / b**2
    A = 1 + u_sq / 16384 * (4096 + u_sq * (-768 + u_sq * (320 - 175 * u_sq)))
    B = u_sq / 1024 * (256 + u_sq * (-128 + u_sq * (74 - 47 * u_sq)))
    sigma_diff = B * sin_sigma * (
        cos_2sigma_m + B / 4 * (
            cos_sigma * (-1 + 2 * cos_2sigma_m**2) 
            - B / 6 * cos_2sigma_m * (-3 + 4 * sin_sigma**2) * (-3 + 4 * cos_2sigma_m**2)
        )
    )
    s = b * A * (sigma - sigma_diff)
    return s

