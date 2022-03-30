import numpy as np
import os
import random
from abc import ABCMeta, abstractmethod


class Attributes:
    def __init__(self, obj, **kwargs):
        self.base_dir = 'blueprints/attributes/'
        self._obj = obj
        self.make(**kwargs)

    @property
    def face(self):
        return self._face

    @property
    def head(self):
        return self._head

    @property
    def mouth(self):
        return self._mouth

    @property
    def eyes(self):
        return self._eyes

    @property
    def ears(self):
        return self._ears

    def make(self, **kwargs):
        self.makeFace(**kwargs)
        self.makeHead(**kwargs)
        self.makeNeck(**kwargs)
        self.makeMouth(**kwargs)
        self.makeEyes(**kwargs)
        self.makeEars(**kwargs)

    def makeFace(self, **kwargs):
        if 'face' in kwargs:
            self._face = kwargs['face']
        else:
            self._face = None

    def makeHead(self, **kwargs):
        self._head = None

    def makeNeck(self, **kwargs):
        self._neck = None

    def makeMouth(self, **kwargs):
        if 'mouth' in kwargs:
            self._mouth = kwargs['mouth']
        else:
            self._mouth = None

    def makeEyes(self, **kwargs):
        if self.face is not None:
            self._eyes = None

        self._eyes = None

    def makeEars(self, **kwargs):
        self._ears = None


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

    @abstractmethod
    def make(self, **kwargs):
        pass


class PugShape(Shape):
    def __init__(self, **kwargs):
        self.base_dir = 'blueprints/base/shape/'
        self.make(**kwargs)

    @property
    def edge(self):
        return self._edge

    @property
    def eyes(self):
        return self._eyes

    @property
    def mouth(self):
        return self._mouth

    def make(self, **kwargs):
        self.makeEdge(**kwargs)
        self.makeEyes(**kwargs)
        self.makeMouth(**kwargs)

    def makeEdge(self, **kwargs):
        self._edge = self.base_dir + 'edge/basic.csv'
        
    def makeEyes(self, **kwargs):
        self._eyes = self.base_dir + 'eyes/basic.csv'
        
    def makeMouth(self, **kwargs):
        self._mouth = self.base_dir + 'mouth/basic.csv'


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

    @abstractmethod
    def make(self, **kwargs):
        pass


class PugColor(Color):
    def __init__(self, **kwargs):
        self.base_dir = 'blueprints/base/color/'
        self.make(**kwargs)

    @property
    def base(self):
        return self._base

    @property
    def eyes(self):
        return self._eyes

    @property
    def ears(self):
        return self._ears

    def make(self, **kwargs):
        self._base = self.base_dir + 'base/basic.csv' 
        self._eyes = None
        self._ears = None


class Character(metaclass=ABCMeta):
    @classmethod
    def get_factory(cls, classname):
        mod = __import__(__name__)
        factory = getattr(mod, classname)
        return factory()

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

    @abstractmethod
    def create(self, **kwargs):
        pass


class Pug(Character):
    """Register pug's blueprints."""
    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    @property
    def attributes(self):
        return self._attr

    def create(self, **kwargs):        
        kwargs.setdefault('shape', {})
        kwargs.setdefault('color', {})
        kwargs.setdefault('attributes', {})

        self.makeShape(**kwargs['shape'])
        self.makeColor(**kwargs['color'])
        self.makeAttributes(**kwargs['attributes'])

    def makeShape(self,**kwargs):
        self._shape = PugShape(**kwargs)
        
    def makeColor(self,**kwargs):
        self._color = PugColor(**kwargs)

    def makeAttributes(self,**kwargs):
        self._attr = Attributes(self, **kwargs)


class AnonyPug(Pug):
    """Register pug's blueprints."""
    def makeAttributes(self, **kwargs):        
        kwargs['face'] = 'anonymous'
        self._attr = Attributes(self, **kwargs)

