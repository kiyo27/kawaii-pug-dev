import numpy as np
import os
import random
from abc import ABCMeta, abstractmethod


_bp_base_dir = 'blueprints/'

def scan(path):
    target = []
    with os.scandir(path) as it:
        for d in it:
            if d.name.endswith('.csv') and d.is_file():
                target.append(d.name)
    return target 

def choice(path, name=None):
    if name is not None:
        return path + name + '.csv' 

    target = scan(path)
    r = random.randrange(0, len(target))    
    return path + target[r]
    
def eyes(name=None):
    blueprint_dir = _bp_base_dir + 'attributes/eyes/'
    return choice(blueprint_dir)

def mouth(name=None):
    bp_dir = _bp_base_dir + 'attributes/mouth/'
    return choice(bp_dir)

def face(name=None):
    bp_dir = _bp_base_dir + 'attributes/face/'
    return choice(bp_dir)

def head(name=None):
    bp_dir = _bp_base_dir + 'attributes/face/'
    return choice(blueprint_dir)


_component = [
    'color',
    'shape',
]

_attribute_list = [
    'face',
    'head',
    'mouth'
]


class BlueprintManager:
    def __init__(self):
        self.bps = []
        self.component = {'shape':{},'color':{}}
        self.attributes = {k:{} for k in _attribute_list}

    def register_base(self, category, **kwargs):
        self.register(_component, category, **kwargs)        

    def register_attribute(self, category, **kwargs):
        self.register(_attribute_list, category, **kwargs)        

    def register(self, l, category, **kwargs):

        def append(category, elem, key, name):
            bp_dir = 'blueprints/' +  category + '/' + key
            self.bps.append(
                bp_dir + '/' + name + '.csv'
            )

            if category == 'base':
                self.component[elem][key] = name

            if category == 'attribute':
                self.attributes[elem][key] = name

        for elem in l:
            if elem in kwargs:
                for key, name in kwargs[elem].items():
                    append(category, elem, key, name)


class Character(metaclass=ABCMeta):
    
    def __init__(self):
        self.shape = {}
        self.color = {}
        self._manager = BlueprintManager()
        self.shuffle()
        self.register()

    @property
    def blueprints(self):
        return self._manager.bps
    
    @property
    def attributes(self):
        return self._manager.attributes

    @abstractmethod
    def shuffle(self):
        pass

    def register(self):
        self._manager.register_base(
            'base',
            shape=self.shape,
            color=self.color
        )

    def add_attribute(self, category, name=None):
        x = globals()[category]()
        self._manager.register(**x)


class Pug(Character):
    """
    Register pug's blueprints.

    """
    def shuffle(self):
        """
        毛の色にバリエーションを持たせる
        """
        self.shape = {
          'edge':'basic',
          'eyes':'basic',
          'mouth': 'basic'
        }
        self.color = { 'base': 'basic' }


class AndroidPug(Character):
    """
    Register AndroidPug's blueprints.
    """
    def shuffle(self):
        self.shape = { 'edge':'basic', 'eyes': 'basic' }
        self.color = { 'base': 'androidpug' }


class AnonyPug(Pug):
    """
    Register AnonyPug's blueprints.
    """
    def __init__(self):
        super().__init__()
    
