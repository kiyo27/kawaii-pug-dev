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


class Character(metaclass=ABCMeta):
    
    def __init__(self):
        self._bps = {}
        self._attributes = {}
        self.register()

    @property
    def blueprints(self):
        return self._bps
    
    @property
    def attributes(self):
        return self._attributes

    @abstractmethod
    def register(self):
        pass

    def add_attribute(self, category, name=None):
        self._bps[category] = globals()[category]()


_pug_bp_dir = _bp_base_dir + 'types/pug/'
_pug_bp = {
    'color_eye_right': _pug_bp_dir + 'color_eye_right.csv',
    'color_eye_left': _pug_bp_dir + 'color_eye_left.csv',
    'color_ear_right': _pug_bp_dir + 'color_ear_right.csv',
    'color_ear_left': _pug_bp_dir + 'color_ear_left.csv',
    'color_mouth': _pug_bp_dir + 'color_mouth.csv',
    'color_face': _pug_bp_dir + 'color_face.csv',
    'color_body': _pug_bp_dir + 'color_body.csv',
    'shape_shape': _pug_bp_dir + 'shape_shape.csv',
    'shape_eye': _pug_bp_dir + 'shape_eye.csv',
    'shape_mouth': _pug_bp_dir + 'shape_mouth.csv'
}

class Pug(Character):
    """
    Register pug's blueprints.
    """
    def register(self):
        self._bps['color_eye_right'] = _pug_bp['color_eye_right']  
        self._bps['color_eye_left'] = _pug_bp['color_eye_left']  
        self._bps['color_ear_right'] = _pug_bp['color_ear_right']  
        self._bps['color_ear_left'] = _pug_bp['color_ear_left']  
        self._bps['color_mouth'] = _pug_bp['color_mouth']  
        self._bps['color_face'] = _pug_bp['color_face']  
        self._bps['color_body'] = _pug_bp['color_body']  
        self._bps['shape_shape'] = _pug_bp['shape_shape']  
        self._bps['shape_eye'] = _pug_bp['shape_eye']  
        self._bps['shape_mouth'] = _pug_bp['shape_mouth']  


_androidpug_bp_dir = _bp_base_dir + 'types/androidpug/'
_androidpug_bp = {
    'face': _androidpug_bp_dir + 'androidpug.csv'
}

class AndroidPug(Character):
    """
    Register AndroidPug's blueprints.
    """
    def register(self):
        self._bps['face'] = _androidpug_bp['face']
        self._bps['shape_mouth'] = _pug_bp['shape_mouth']
        self._bps['shape_eye'] = _pug_bp['shape_eye']
        

_anonypug_bp_dir = _bp_base_dir + 'types/anonypug/'
_anonypug_bp = {
    'face': _androidpug_bp_dir + 'anonypug.csv'
}

class AnonyPug(Pug):
    """
    Register AnonyPug's blueprints.
    """
    def register(self):
        super().register()
        self._bps['face'] = _anonypug_bp['face']

