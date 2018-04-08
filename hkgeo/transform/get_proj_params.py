"""
Reference:
https://www.geodetic.gov.hk/smo/gsi/data/pdf/explanatorynotes.pdf
https://www.geodetic.gov.hk/smo/gsi/data/pdf/explanatorynotes_c.pdf # (Traditional Chinese version)
https://www.geodetic.gov.hk/smo/gsi/data/parameter/SchematicDiagram.pdf
https://www.geodetic.gov.hk/smo/tform/tform.aspx
https://www.geodetic.gov.hk/smo/en/tform/tform.aspx
http://www.hydro.gov.hk/eng/datumnew.php
http://cs2cs.mygeodata.eu/
https://en.wikipedia.org/wiki/World_Geodetic_System
http://ailin.phychembio.com/miscellany/1387/
http://blog.tiger-workshop.com/hk1980-grid-to-wgs84/

Note that the values of rho and psi obtained by this function will be slightly different from the values in the note.
In the note, upsilon = 6381480.500, rho = 6359840.760, psi = 1.003402560.
This issue has been reported to the Geodetic Survey Section, Lands Department, Hong Kong and under investigation.
"""

import numpy as np

from .. import constants


def get_proj_params(phi=(22 + 18 / 60 + 43.68 / 3600) * np.pi / 180):
    a = constants.HK80G_PARAMS.get('a')
    e_sq = constants.HK80G_PARAMS.get('e_sq')
    upsilon = a / (1 - e_sq * np.sin(phi)**2)**(1 / 2)
    rho = a * (1 - e_sq) / (1 - e_sq * np.sin(phi)**2)**(3 / 2)
    psi = upsilon / rho
    out = {
        'upsilon': upsilon,
        'rho': rho,
        'psi': psi
    }
    return out

