import numpy as np


WGS84_PARAMS = {
    'semi_major_axis': 6378137.0, # meters
    'semi_minor_axis': (1 - 1 / 298.257223563) * 6378137.0,  # meters
    'invserse_flattening': 1 / 298.257223563, 
    'a': 6378137.0,
    'f': 1 / 298.257223563,
}

HK80G_PARAMS = {
    'a': 6378388,
    'f': 1 / 297,
    'e_sq': 2 / 297 - (1 / 297)**2,
    'm0': 1,
    'E0': 836694.05,
    'N0': 819069.80,
    'lambda0': (114 + 10 / 60 + 42.80 / 3600) * np.pi / 180,
    'phi0': (22 + 18 / 60 + 43.68 / 3600) * np.pi / 180
}

