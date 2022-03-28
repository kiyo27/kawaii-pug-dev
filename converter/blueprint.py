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


_types = [
    'color',
    'shape',
]

class BlueprintManager:
    def __init__(self):
        self.bps = []
        self.attributes = {'shape':{},'color':{}}

    def register(self, base_dir, **kwargs):
        bp_dir = 'blueprints/' +  base_dir + '/'

        def add(attr, category, value):
            self.attributes[attr][category] = value
            self.bps.append(
                bp_dir + attr + '/' + category + '/' + value + '.csv'
            )

        for attr in _types:
            if attr in kwargs:
                for category, value in kwargs[attr].items():
                    add(attr, category, value)


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
        self._manager.register(
            'types',
            shape=self.shape,
            color=self.color
        )

    def add_attribute(self, category, name=None):
        self._bps[category] = globals()[category]()


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
        pass
    
