# -*- coding: utf-8 -*-

import numpy as np

from .. import constants


def meridian_distance(
        phi,
        a=constants.HK80G_PARAMS.get('a'),
        e_sq=constants.HK80G_PARAMS.get('e_sq')):
    # Constants
    a0 = 1 - e_sq / 4 - 3 * e_sq**2 / 64
    a2 = 3 / 8 * (e_sq + e_sq**2 / 4)
    a4 = 15 / 256 * e_sq**2
    # Meridian Distance
    m_d = a * (a0 * phi - a2 * np.sin(2 * phi) + a4 * np.sin(4 * phi))
    return m_d

