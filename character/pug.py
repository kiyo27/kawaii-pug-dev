import numpy as np
import os
import random
from  pixart import abstract


class Attributes:
    def __init__(self, obj, **kwargs):
        self.base_dir = 'character/blueprints/attributes/'
        self._obj = obj
        self.make(**kwargs)

    def __eq__(self, other):
        if (self.face == other.face
              and self.head == other.head
              and self.neck == other.neck
              and self.mouth == other.mouth):
            return True
        return False

    @property
    def face(self):
        return self._face

    @property
    def head(self):
        return self._head

    @property
    def neck(self):
        return self._neck

    @property
    def mouth(self):
        return self._mouth

    @property
    def eyes(self):
        return self._eyes

    def make(self, **kwargs):
        self.makeFace(**kwargs)
        self.makeHead(**kwargs)
        self.makeNeck(**kwargs)
        self.makeMouth(**kwargs)
        self.makeEyes(**kwargs)

    def choice(self, path):
        target = []
        with os.scandir(path) as it:
            for d in it:
                if d.name.endswith('.csv') and d.is_file():
                    target.append(d.name)
        return path + random.choice(target) 

    def makeFace(self, **kwargs):
        bp_dir = self.base_dir + 'face/'
        if 'face' in kwargs:
            self._face = kwargs['face']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._face = None
            else:
                self._face = self.choice(bp_dir) 

    def makeHead(self, **kwargs):
        bp_dir = self.base_dir + 'head/'
        if 'head' in kwargs:
            self._head = kwargs['head']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._head = None
            else:
                self._head = self.choice(bp_dir) 

    def makeNeck(self, **kwargs):
        bp_dir = self.base_dir + 'neck/'
        if 'neck' in kwargs:
            self._neck = kwargs['neck']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._neck = None
            else:
                self._neck = self.choice(bp_dir) 

    def makeMouth(self, **kwargs):
        bp_dir = self.base_dir + 'mouth/'
        if 'mouth' in kwargs:
            self._mouth = kwargs['mouth']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._mouth = None
            else:
                self._mouth = self.choice(bp_dir) 

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + 'eyes/'
        if self.face is not None:
            self._eyes = None
        elif 'eyes' in kwargs:
            self._eyes = kwargs['eyes']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._eyes = None
            else:
                self._eyes = self.choice(bp_dir) 


class Shape(abstract.Shape):
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
        bp_dir = self.base_dir + 'edge/'
        if 'edge' in kwargs:
            self._edge = bp_dir + kwargs['edge'] + '.csv'
        else:
            self._edge = bp_dir + 'basic.csv'
        
    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + 'eyes/'
        if 'eyes' in kwargs:
            self._eyes = bp_dir + kwargs['eyes'] + '.csv'
        else:
            self._eyes = bp_dir + 'basic.csv'
        
    def makeMouth(self, **kwargs):
        bp_dir = self.base_dir + 'mouth/'
        if 'mouth' in kwargs:
            self._mouth = bp_dir + kwargs['mouth'] + '.csv'
        else:
            self._mouth = bp_dir + 'basic.csv'


class Color(abstract.Color):
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


class Pug(abstract.Character):
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
        self._shape = Shape(**kwargs)
        
    def makeColor(self,**kwargs):
        self._color = Color(**kwargs)

    def makeAttributes(self,**kwargs):
        self._attr = Attributes(self, **kwargs)


class AnonyPug(Pug):
    """Register anonypug's blueprints."""
    def makeAttributes(self, **kwargs):        
        kwargs['face'] = 'anonymous'
        self._attr = Attributes(self, **kwargs)


class SleepingPug(Pug):
    """Register sleeping-pug's blueprints."""
    def makeShape(self, **kwargs):        
        kwargs['eyes'] = 'sleeping'
        kwargs['mouth'] = 'sleeping'
        self._shape = Shape(**kwargs)
