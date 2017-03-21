# -*- coding: utf-8 -*-

import numpy as np
from .. import settings


class Angle(object):
    """
    Parameters
    ----------
    value: float, default=0
        Angle value.
    unit: str, default='d'
        Unit of angle, 'd' for degree, 'r' for radian.
    """
    
    def __init__(self, value, unit='d'):
        unit = str(unit[0]).lower()
        if not isinstance(value, (float, int, np.integer, np.floating)):
            raise TypeError('value must be a float/int.')
        if unit not in 'dr':
            raise ValueError('unit must be either \'d\' (degree) or \'r\' (radian)')
        self._value = value * (np.pi / 180)**(unit == 'd')
        self._unit = unit
    
    def __repr__(self):
        print_text = '{:}{:}'.format(
            round(self._value * (180 / np.pi) ** (self._unit == 'd'), settings.N_DIGITS),
            {'r': 'r', 'd': '\u00b0'}.get(self._unit)
        )
        return print_text
    
    @property
    def value(self):
        return self._value
    
    @property
    def unit(self):
        return self._unit
    
    @property
    def degree(self):
        return self._value * (180 / np.pi)
    
    @property
    def radian(self):
        return self._value
    
    # Comparison functions
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self._value < other.value
        elif isinstance(other, (float, int)):
            return self._value < other
        else:
            msg = 'unorderable types: {:}() < {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __le__(self, other):
        if isinstance(other, type(self)):
            return self._value <= other.value
        elif isinstance(other, (float, int)):
            return self._value <= other
        else:
            msg = 'unorderable types: {:}() <= {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._value == other.value
        elif isinstance(other, (float, int)):
            return self._value == other
        else:
            msg = 'unorderable types: {:}() == {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __ne__(self, other):
        if isinstance(other, type(self)):
            return self._value != other.value
        elif isinstance(other, (float, int)):
            return self._value != other
        else:
            msg = 'unorderable types: {:}() != {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self._value > other.value
        elif isinstance(other, (float, int)):
            return self._value > other
        else:
            msg = 'unorderable types: {:}() > {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __ge__(self, other):
        if isinstance(other, type(self)):
            return self._value >= other.value
        elif isinstance(other, (float, int)):
            return self._value >= other
        else:
            msg = 'unorderable types: {:}() >= {:}().'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    # Mathematical operations
    def __add__(self, other):
        if isinstance(other, type(self)):
            if self._unit == 'd':
                return type(self)(self.degree + other.degree, unit='d')
            else:
                return type(self)(self.radian + other.radian, unit='r')
        else:
            msg = 'unsupported operand type(s) for +: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __sub__(self, other):
        if isinstance(other, type(self)):
            if self._unit == 'd':
                return type(self)(self.degree - other.degree, unit='d')
            else:
                return type(self)(self.radian - other.radian, unit='r')
        else:
            msg = 'unsupported operand type(s) for -: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            if self._unit == 'd':
                return type(self)(self.degree * other, unit='d')
            else:
                return type(self)(self.radian * other, unit='r')
        else:
            msg = 'unsupported operand type(s) for *: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            if self._unit == 'd':
                return type(self)(self.degree / other, unit='d')
            else:
                return type(self)(self.radian / other, unit='r')
        else:
            msg = 'unsupported operand type(s) for /: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __floordiv__(self, other):
        if isinstance(other, (float, int)):
            if self._unit == 'd':
                return type(self)(self.degree // other, unit='d')
            else:
                return type(self)(self.radian // other, unit='r')
        else:
            msg = 'unsupported operand type(s) for //: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __mod__(self, other):
        if isinstance(other, (float, int)):
            if self._unit == 'd':
                return type(self)(self.degree % other, unit='d')
            else:
                return type(self)(self.radian % other, unit='r')
        else:
            msg = 'unsupported operand type(s) for %: \'{:}\' and \'{:}\'.'
            msg = msg.format(type(self).__name__, type(other).__name__)
            raise TypeError(msg)
    
    def __neg__(self):
        if self._unit == 'd':
            return type(self)(-self.degree, unit='d')
        else:
            return type(self)(-self.radian, unit='r')
    
    def __abs__(self):
        if self._unit == 'd':
            return type(self)(abs(self.degree), unit='d')
        else:
            return type(self)(abs(self.radian), unit='r')
    
    def __round__(self, n=None):
        if self._unit == 'd':
            return type(self)(round(self.degree, n), 'd')
        else:
            return type(self)(round(self.radian, n), 'r')
    
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

