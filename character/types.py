import numpy as np
import os
import random
from pixart import abstract
from character.shape import PugShape
from character.color import PugColor
from character.attribute import PugAttribute


class Pug(abstract.Character):
    """Register pug's blueprints."""
    ctype = 'Pug'

    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    @property
    def attributes(self):
        return self._attr

    def create(self, num, **kwargs):        
        self.num = num
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
        self._attr = PugAttribute(self, **kwargs)


class AnonyPug(Pug):
    """Register anonypug's blueprints."""
    ctype = 'AnonyPug'

    def makeAttributes(self, **kwargs):        
        kwargs['face'] = 'anonymous'
        kwargs['mouth'] = False
        self._attr = PugAttribute(self, **kwargs)


class SleepingPug(Pug):
    """Register sleeping-pug's blueprints."""
    ctype = 'SleepingPug'

    def makeShape(self, **kwargs):        
        kwargs['eyes'] = 'sleeping'
        kwargs['mouth'] = 'sleeping'
        self._shape = PugShape(**kwargs)

