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
            cls.goggle = get_attr(attr_list, 'goggle')
            cls.nose = get_attr(attr_list, 'nose')
            cls.ears = get_attr(attr_list, 'ears')

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
              and self.mouth == other.mouth
              and self.eyes == other.eyes
              and self.goggle == other.goggle
              and self.nose == other.nose
              and self.ears == other.ears):
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

    @property
    def goggle(self):
        return self._goggle

    @property
    def nose(self):
        return self._nose

    @property
    def ears(self):
        return self._ears

    def make(self, **kwargs):
        self.makeFace(**kwargs)
        self.makeHead(**kwargs)
        self.makeNeck(**kwargs)
        self.makeMouth(**kwargs)
        self.makeEyes(**kwargs)
        self.makeGoggles(**kwargs)
        self.makeNose(**kwargs)
        self.makeEars(**kwargs)

    def makeFace(self, **kwargs):
        self.set_attr('face', **kwargs)

    def makeHead(self, **kwargs):
        self.set_attr('head', **kwargs)

    def makeNeck(self, **kwargs):
        self.set_attr('neck', **kwargs)

    def makeMouth(self, **kwargs):
        self.set_attr('mouth', **kwargs)

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + 'eyes/'
        if self.face is not None:
            self._eyes = None
        else:
            self.set_attr('eyes', **kwargs)

    def makeGoggles(self, **kwargs):
        self.set_attr('goggle', **kwargs)

    def makeNose(self, **kwargs):
        self.set_attr('nose', **kwargs)

    def makeEars(self, **kwargs):
        self.set_attr('ears', **kwargs)

    def choice(self, path, attr):
        target = random.choices(attr['names'], weights=attr['weights'], k=1)[0]
        return path + target + '.csv'

    def set_attr(self, attr, **kwargs):
        if attr in kwargs:
            if kwargs[attr] is False:
                setattr(self, '_' + attr, None)
            else:
                setattr(self, '_' + attr, bp_dir + kwargs[attr] + '.csv')
        else:
            r = random.randrange(0, 1000)
            weight = getattr(self.attr, attr)['weight']
            if weight < r:
                setattr(self, '_' + attr, None)
            else:
                bp_dir = self.base_dir + attr + '/'
                l = getattr(self.attr, attr)['list']
                setattr(self, '_' + attr, self.choice(bp_dir, l))

