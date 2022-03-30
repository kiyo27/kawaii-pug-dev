import numpy as np
import os
import random
from abc import ABCMeta, abstractmethod


class Attributes:
    
    def __init__(self, **kwargs):
        pass

    def face(self):
        pass

    def head(self):
        pass

    def neck(self):
        pass

    def mouth(self):
        pass

    def eyes(self):
        pass

    def ears(self):
        pass


class Shape(metaclass=ABCMeta):
    @property
    @abstractmethod
    def edge(self):
        pass

    @property
    @abstractmethod
    def eyes(self):
        pass

    @property
    @abstractmethod
    def mouth(self):
        pass

class PugShape(Shape):
    def __init__(self, **kwargs):
        self._edge = 'basic.csv'
        self._eyes = 'basic.csv'
        self._mouth = 'basic.csv'

    @property
    def edge(self):
        return self._edge

    @property
    def eyes(self):
        return self._eyes

    @property
    def mouth(self):
        return self._mouth

class Color(metaclass=ABCMeta):
    @property
    @abstractmethod
    def base(self):
        pass

    @property
    @abstractmethod
    def eyes(self):
        pass

    @property
    @abstractmethod
    def ears(self):
        pass


class PugColor(Color):
    def __init__(self, **kwargs):
        self._base = 'basic.csv'
        self._eyes = None
        self._ears = None

    @property
    def base(self):
        return self._base

    @property
    def eyes(self):
        return self._eyes

    @property
    def ears(self):
        return self._ears


class Character(metaclass=ABCMeta):
    @property
    @abstractmethod
    def shape(self):
        pass

    @property
    @abstractmethod
    def color(self):
        pass

    @property
    @abstractmethod
    def attributes(self):
        pass

class Pug(Character):
    """Register pug's blueprints."""

    def __init__(self, **kwargs):
        self._shape = PugShape()
        self._color = PugColor()
        self._attr = Attributes()

    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    @property
    def attributes(self):
        return self._attr


class AnonyPug(Pug):
    """
    Register AnonyPug's blueprints.
    """
    def __init__(self, **kwargs):
        self._shape = PugShape()
        self._color = PugColor()
        self._attr = Attributes(face='anonymous')


