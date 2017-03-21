# -*- coding: utf-8 -*-

from .Angle import Angle


class Degree(Angle):
    def __init__(self, value):
        super().__init__(value, unit='d')

