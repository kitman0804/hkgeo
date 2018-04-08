import numpy as np
from .. import settings


class Angle(object):
    """
    Parameters
    ----------
    value: float, default=0
        Angle value.
    unit: str, default='deg'
        Unit of angle.
            'deg': degree
            'rad': radian
    """
    
    def __init__(self, value, unit='deg'):
        unit = str(unit).lower()
        if not isinstance(value, (float, int, np.integer, np.floating)):
            raise TypeError('value must be a float/int.')
        if unit == 'rad':
            self._value = value
            self._unit = unit
        elif unit == 'deg':
            self._value = value * np.pi / 180
            self._unit = unit
        else:
            raise ValueError('unit must be either \'deg\' (degree) or \'rad\' (radian).')
    
    def __repr__(self):
        if self._unit == 'rad':
            print_text = '{:}r'.format(
                round(self.radian, settings.N_DIGITS))
        elif self._unit == 'deg':
            print_text = '{:}\u00b0'.format(
                round(self.degree, settings.N_DIGITS))
        return print_text
    
    @property
    def value(self):
        return self._value
    
    @property
    def unit(self):
        return self._unit
    
    @property
    def radian(self):
        return self._value
    
    @property
    def degree(self):
        return self._value * (180 / np.pi)
    
    @property
    def dms(self):
        d = np.trunc(self._value)
        m = np.trunc((self._value - d) * 60)
        s = (self._value - d - m / 60) * 3600
        return (d, m, s)
    
    def to_rad(self):
        self._unit = 'rad'
    
    def to_deg(self):
        self._unit = 'deg'
    
    def _change_unit(self, unit):
        unit = str(unit).lower()
        if unit == 'rad':
            self.to_rad()
        elif unit == 'deg':
            self.to_deg()
        else:
            raise ValueError('No such unit {:}.'.format(unit))
    
    # Comparison functions
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self._value < other.value
        elif isinstance(other, (float, int)):
            return self._value < other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '<', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __le__(self, other):
        if isinstance(other, type(self)):
            return self._value <= other.value
        elif isinstance(other, (float, int)):
            return self._value <= other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '<=', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._value == other.value
        elif isinstance(other, (float, int)):
            return self._value == other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '==', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __ne__(self, other):
        if isinstance(other, type(self)):
            return self._value != other.value
        elif isinstance(other, (float, int)):
            return self._value != other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '!=', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self._value > other.value
        elif isinstance(other, (float, int)):
            return self._value > other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '>', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __ge__(self, other):
        if isinstance(other, type(self)):
            return self._value >= other.value
        elif isinstance(other, (float, int)):
            return self._value >= other
        else:
            msg = 'unorderable types: {:}() {:} {:}().'.format(
                '>=', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    # Mathematical operations
    def __add__(self, other):
        if isinstance(other, type(self)):
            a = type(self)(self.radian + other.radian, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '+', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __sub__(self, other):
        if isinstance(other, type(self)):
            a = type(self)(self.radian - other.radian, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '-', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            a = type(self)(self.radian * other, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '*', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            a = type(self)(self.radian / other, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '/', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __floordiv__(self, other):
        if isinstance(other, (float, int)):
            a = type(self)(self.radian // other, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '//', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __mod__(self, other):
        if isinstance(other, (float, int)):
            a = type(self)(self.radian % other, unit='rad')
            a._change_unit(self.unit)
            return a
        else:
            msg = 'unsupported operand type(s) for {:}: \'{:}\' and \'{:}\'.'.format(
                '%', 
                type(self).__name__, 
                type(other).__name__)
            raise TypeError(msg)
    
    def __neg__(self):
        a = type(self)(-self.radian, unit='rad')
        a._change_unit(self.unit)
        return a
    
    def __abs__(self):
        a = type(self)(abs(self.radian), unit='rad')
        a._change_unit(self.unit)
        return a
    
    def __round__(self, n=None):
        if self._unit == 'rad':
            return type(self)(round(self.radian, n), unit='rad')
        elif self._unit == 'deg':
            return type(self)(round(self.degree, n), unit='deg')
    
    # Trigonometric functions
    def sin(self):
        x = self._value
        return np.sin(x)
    
    def cos(self):
        x = self._value
        return np.cos(x)
    
    def tan(self):
        x = self._value
        return np.tan(x)
    
    def sinh(self):
        x = self._value
        return np.sinh(x)
    
    def cosh(self):
        x = self._value
        return np.cosh(x)
    
    def tanh(self):
        x = self._value
        return np.tanh(x)


class Radian(Angle):
    def __init__(self, value):
        super().__init__(value, unit='rad')


class Degree(Angle):
    def __init__(self, value):
        super().__init__(value, unit='deg')

