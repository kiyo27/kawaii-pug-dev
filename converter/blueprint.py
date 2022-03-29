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
        self.bp_dir = 'blueprints/'
        self.bps = []
        self.component = {'shape':{},'color':{}}
        self._bps = {'shape': {}, 'color': {}, 'attributes': {}}

    def register_base(self, category, **kwargs):
        self.register(_component, category, **kwargs)        

    def register_attribute(self, category, element, path):
        target_path = self.bp_dir + '/' + path + '.csv'
        self._bps[category][element] = target_path
        print(self._bps)

    def register(self, l, category, **kwargs):

        def append(category, elem, key, name):
            target_dir = self.bp_dir +  category + '/' + key
            self.bps.append(
                target_dir + name + '.csv'
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
        self.attributes = AttributeManager(self._manager)

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


class Attribute(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def part(self):
        pass

    @property
    @abstractmethod
    def group(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def path(self):
        return f"attributes/{self.part}/{self.group}/{self.name}"


class Face(Attribute):
    def __init__(self, **kwargs):
        """口に属性を追加する"""
        self._group = None
        self._name = None
        self.register(**kwargs)

    @property
    def part(self):
        return 'face' 

    @property
    def group(self):
        return self._group

    @property
    def name(self):
        return self._name

    def shuffle(self):
        """シャッフルする"""
        self.register()

    def register(self, **kwargs):
        """属性の追加"""
        if 'face' in kwargs:
          self._group = kwargs['face']['group']
          self._name = kwargs['face']['name']
        else:
          # ランダムに選択する
          self.facemask()

    def facemask(self):
        """フェイスマスクの属性を登録する"""
        self._group = "facemask"
        # ランダムに選択する
        self._name = "anonymous"

    def cigarette(self):
        """属性にタバコを追加する"""
        pass


class AttributeManager:
    def __init__(self, blueprint_manager,  **kwargs):
        self.category = 'attributes'
        self._manager = blueprint_manager

        self.list = []
        self.create(**kwargs)
        #self.register_blueprint()

    def create(self, **kwargs):
        """各部位の属性を生成する"""
        self.list.append(Face(**kwargs))

    def recreate(self):
        """各部位の属性を再生成する"""
        self.create()
        self.register_blueprint()

    def register_blueprint(self):
        for attr in self.list:
            if attr.path is not None:
                self._manager.register_attribute(
                    self.category, attr.part, attr.path
                )



