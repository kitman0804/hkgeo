import numpy as np

from .meridian_distance import meridian_distance
from .get_proj_params import get_proj_params
from .. import constants


def hk80_to_hk80g(lat, lon, unit='d'):
    if unit == 'd':
        lon *= np.pi / 180
        lat *= np.pi / 180
    lambda0 = constants.HK80G_PARAMS.get('lambda0')
    phi0 = constants.HK80G_PARAMS.get('phi0')
    E0 = constants.HK80G_PARAMS.get('E0')
    N0 = constants.HK80G_PARAMS.get('N0')
    m0 = constants.HK80G_PARAMS.get('m0')
    M0 = meridian_distance(phi0)  # M0 = 2468395.723
    M = meridian_distance(lat)
    proj_params = get_proj_params()
    upsilon = proj_params.get('upsilon')
    psi = proj_params.get('psi')
    # Obtain E, N coordinates
    E = E0 + m0 * (
        upsilon * (lon - lambda0) * np.cos(lat)
        + upsilon * (lon - lambda0)**3 / 6 * (np.cos(lat))**3 * (psi - (np.tan(lat))**2)
    )
    N = N0 + m0 * (M - M0 + upsilon * np.sin(lat) * (lon - lambda0)**2 / 2 * np.cos(lat))
    return E, N

