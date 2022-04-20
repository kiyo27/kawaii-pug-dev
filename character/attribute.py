import os
import random

import yaml

from pixart import abstract


def get_attr(attr_list, key):
    n = []
    w = []
    for o in attr_list[key]["attribute"]:
        n.append(o["name"])
        w.append(o["weight"])

    d = {"list": attr_list[key]["attribute"], "attr_weights": w}
    d["weight"] = attr_list[key]["weight"]
    return d

def choice(attr):
    target = random.choices(attr["list"], weights=attr["attr_weights"], k=1)[0]
    return target


class AttributeYaml:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.singleton == None:
            cls.singleton = super().__new__(cls)

            with open("character/attributes.yaml") as f:
                attr_list = yaml.safe_load(f)

            cls.head = get_attr(attr_list, "head")
            cls.neck = get_attr(attr_list, "neck")
            cls.mouth = get_attr(attr_list, "mouth")
            cls.eyes = get_attr(attr_list, "eyes")
            cls.glasses = get_attr(attr_list, "glasses")
            cls.nose = get_attr(attr_list, "nose")
            cls.ears = get_attr(attr_list, "ears")

        return cls.singleton


class PugAttribute:
    def __init__(self, obj, **kwargs):
        self.base_dir = "character/blueprints/attributes/"
        self._obj = obj
        self.attr_yml = AttributeYaml()
        self.make(**kwargs)

    def __eq__(self, other):
        if (
            self.mask == other.mask
            and self.head == other.head
            and self.neck == other.neck
            and self.mouth == other.mouth
            and self.eyes == other.eyes
            and self.glasses == other.glasses
            and self.nose == other.nose
            and self.ears == other.ears
        ):
            return True
        return False

    @property
    def mask(self):
        return self._mask

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
    def glasses(self):
        return self._glasses

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
        self.makeGlasses(**kwargs)
        self.makeNose(**kwargs)
        self.makeEars(**kwargs)

    def makeFace(self, **kwargs):
        if "mask" in kwargs:
            self.set_attr("mask", **kwargs)
        else:
            self._mask = None

    def makeHead(self, **kwargs):
        self.set_attr("head", **kwargs)

    def makeNeck(self, **kwargs):
        self.set_attr("neck", **kwargs)

    def makeMouth(self, **kwargs):
        self.set_attr("mouth", **kwargs)

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + "eyes/"
        if self.mask is not None:
            self._eyes = None
        else:
            self.set_attr("eyes", **kwargs)

    def makeGlasses(self, **kwargs):
        self.set_attr("glasses", **kwargs)

    def makeNose(self, **kwargs):
        self.set_attr("nose", **kwargs)

    def makeEars(self, **kwargs):
        self.set_attr("ears", **kwargs)

    def set_attr(self, attr, **kwargs):
        bp_dir = self.base_dir + attr + "/"
        if attr in kwargs:
            if kwargs[attr] is False:
                setattr(self, "_" + attr, None)
            else:
                setattr(self, "_" + attr, bp_dir + kwargs[attr] + ".csv")
                target = self._get_attr_by_name(attr, kwargs[attr])
                self._optional_attr(target)
        else:
            r = random.randrange(0, 1000)
            weight = getattr(self.attr_yml, attr)["weight"]
            if weight < r:
                setattr(self, "_" + attr, None)
            else:
                l = getattr(self.attr_yml, attr)
                target = choice(l)
                setattr(self, "_" + attr, bp_dir + target["name"] + ".csv")
                self._optional_attr(target)

    def _get_attr_by_name(self, key, name):
        attr_list = getattr(self.attr_yml, key)["list"]
        for attr in attr_list:
            if name == attr["name"]:
                return attr

    def _optional_attr(self, target):
        if 'options' in target:
            if self._obj.ctype == 'Pug':
                self._recursive_set(self._obj, 'basic', target['options'], "character/blueprints")
            elif self._obj.ctype == 'SleepingPug':
                self._recursive_set(self._obj, 'sleeping', target['options'], "character/blueprints")

    def _recursive_set(self, obj, key, value, path):
        if type(value[key]) is not dict:
            bp_path = path + "/" + value[key] + ".csv"
            setattr(obj, key, bp_path)

        else:
            for opt in value[key].keys():
                path = path + "/" + opt
                if hasattr(obj, opt):
                    _obj = getattr(obj, opt)
                    if _obj:
                        self._recursive_set(_obj, opt, value[key], path) 
                    else:
                        self._recursive_set(obj, opt, value[key], path)
                else:
                    self._recursive_set(obj, opt, value[key], path) 
