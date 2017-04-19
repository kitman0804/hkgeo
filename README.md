## hkgeo

*version 0.1*

---

### Prerequisites

System requirement:
- Python 3
  - [Anaconda (Recommened)](https://www.continuum.io/downloads)
  - [www.python.org](https://www.python.org/downloads/)

Required packages:
- [Scipy](https://www.scipy.org/)
- [Numpy](http://www.numpy.org/)

### Installation

**Method 1:**

1. Run the follow command.

```
pip install git+https://github.com/kitman0804/hkgeo.git
```

**Method 2:**

1. Download the repository.

2. Run the following command in the downloaded directory.

```
python setup.py install
```

---

### Examples

```
from hkgeo import LatLon
from hkgeo import distance, transform


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
