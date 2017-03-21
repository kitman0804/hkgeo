## hkgeo

*version 0.1*

A Hong Kong Geodetic Datum Transformation Package.

## Installation

First, you need Python 3 installed. Sorry for those Python 2 users.

If you don't have python 3 installed in your computer, you can download
it from the following links and install:

- [Anaconda (Recommended)](https://www.continuum.io/downloads)
- [python.org](https://www.python.org/downloads/)
- [Enthought Canopy](https://www.enthought.com/products/canopy/)

To install the package, run the following code in your console.

```
pip install git+https://github.com/kitman0804/hkgeo.git
```

## Examples

```
import hkgeo
from hkgeo import distance, transform
from hkgeo import LatLon
from hkgeo.geometry import Angle
hkgeo.settings.N_DIGITS = 3

# Geomotry
abs(Angle(40, 'd') / 3 - Angle(20, 'd') * 2)
# 26.667°

# Latitude and Longitude
print(LatLon(22.322172084, 114.141187917))
# 22.322°N, 114.141°E


# Transformation
transform.hk80g_to_hk80(836055, 832699)
# 22.43521015261264, 114.17234807490858

transform.hk80_to_hk80g(22+26/60+6.76/3600, 114+10/60+20.46/3600)
# 836055.20143992256, 832699.10613402259

transform.wgs84_to_hk80g(22.322172084, 114.141187917)
# 832592.1959246879, 820351.17784365441


# Distance
distance.vincenty(LatLon(-37, 144), LatLon(-37, 143))
# 89011.262537100483

distance.vincenty(lat0=50, lon0=5, lat1=58, lon1=3)
# 899937.70573241916
```

