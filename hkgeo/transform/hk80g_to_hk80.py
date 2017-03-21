# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import fsolve

from .meridian_distance import meridian_distance
from .get_proj_params import get_proj_params
from .. import constants


def hk80g_to_hk80(E, N, unit='d'):
    # Get all necessary parameters
    lambda0 = constants.HK80G_PARAMS.get('lambda0')
    phi0 = constants.HK80G_PARAMS.get('phi0')
    E0 = constants.HK80G_PARAMS.get('E0')
    N0 = constants.HK80G_PARAMS.get('N0')
    m0 = constants.HK80G_PARAMS.get('m0')
    M0 = meridian_distance(phi=phi0)  # M0 = 2468395.723
    # Find phi_p using eqt3 in Note
    phi_p = fsolve(lambda phi: meridian_distance(phi) - (N - N0 + M0) / m0, x0=0)
    phi_p = np.asscalar(phi_p)
    proj_params = get_proj_params(phi_p)
    upsilon = proj_params.get('upsilon')
    rho = proj_params.get('rho')
    psi = proj_params.get('psi')
    # Obtain lon and lat in HK80
    lon = (
        lambda0 + 
        1 / np.cos(phi_p) * (E - E0) / (m0 * upsilon) 
        - 1 / np.cos(phi_p) * (E - E0) ** 3 / (6 * m0 ** 3 * upsilon ** 3) * (psi + 2 * np.tan(phi_p) ** 2)
    )
    lat = phi_p - np.tan(phi_p) / (m0 * rho) * (E - E0)**2 / (2 * m0 * upsilon)
    if unit == 'd':
        lon *= 180 / np.pi
        lat *= 180 / np.pi
    # Output
    return lat, lon

