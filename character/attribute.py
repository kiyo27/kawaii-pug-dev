import yaml
import os
import random
from pixart import abstract


def get_attr(attr_list, key):
    n = []
    w = []
    for o in attr_list[key]['attribute']:
        n.append(o['name'])
        w.append(o['weight'])

    d = {'list': {'names': n, 'weights': w}}
    d['weight'] = attr_list[key]['weight']
    return d 


class AttributeYaml:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.singleton == None:
            cls.singleton = super().__new__(cls)

            with open('character/attributes.yaml') as f:
                attr_list = yaml.safe_load(f)

            cls.face = get_attr(attr_list, 'face')
            cls.head = get_attr(attr_list, 'head')
            cls.neck = get_attr(attr_list, 'neck')
            cls.mouth = get_attr(attr_list, 'mouth')
            cls.eyes = get_attr(attr_list, 'eyes')

        return cls.singleton


class PugAttribute:
    def __init__(self, obj, **kwargs):
        self.base_dir = 'character/blueprints/attributes/'
        self._obj = obj
        self.attr = AttributeYaml()
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

    def choice(self, path, attr):
        target = random.choices(attr['names'], weights=attr['weights'], k=1)[0]
        return path + target + '.csv'

    def makeFace(self, **kwargs):
        bp_dir = self.base_dir + 'face/'
        if 'face' in kwargs:
            self._face = bp_dir + kwargs['face'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if self.attr.face['weight'] < r:
                self._face = None
            else:
                print(r, 'anony')
                self._face = self.choice(bp_dir, self.attr.face['list'])

    def makeHead(self, **kwargs):
        bp_dir = self.base_dir + 'head/'

        if 'head' in kwargs:
            self._head = bp_dir + kwargs['head'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if self.attr.head['weight'] < r:
                self._head = None
            else:
                self._head = self.choice(bp_dir, self.attr.head['list'])

    def makeNeck(self, **kwargs):
        bp_dir = self.base_dir + 'neck/'
        if 'neck' in kwargs:
            self._neck = bp_dir + kwargs['neck'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if self.attr.neck['weight'] < r :
                self._neck = None
            else:
                self._neck = self.choice(bp_dir, self.attr.neck['list'])


    def makeMouth(self, **kwargs):
        bp_dir = self.base_dir + 'mouth/'
        if 'mouth' in kwargs:
            if kwargs['mouth'] is False:
                self._mouth = None
            else:
                self._mouth = bp_dir + kwargs['mouth'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if self.attr.mouth['weight'] < r:
                self._mouth = None
            else:
                self._mouth = self.choice(bp_dir, self.attr.mouth['list']) 

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + 'eyes/'
        if self.face is not None:
            self._eyes = None
        elif 'eyes' in kwargs:
            self._eyes = kwargs['eyes']
        else:
            r = random.randrange(0, 9)
            if self.attr.eyes['weight'] < r:
                self._eyes = None
            else:
                self._eyes = self.choice(bp_dir, self.attr.eyes['list'])

