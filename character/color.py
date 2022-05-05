from pixart import abstract
from character import attribute


class PugColor(abstract.Color):
    def __init__(self, **kwargs):
        self.base_dir = "character/blueprints/base/color/"
        self.make(**kwargs)

    @property
    def skin(self):
        return self._skin

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, eyes):
        self._eyes = eyes

    def make(self, **kwargs):
        self._eyes = None

        if "skin" in kwargs:
            self._skin = self.base_dir + kwargs["skin"] + ".csv"
        else:
            n = ["rainbow", "metallic", "basic", "green", "blue-red"]
            w = [1, 5, 10, 1, 1]
            attr = {"list": n, "attr_weights": w}
            bp = attribute.choice(attr)
            self._skin = self.base_dir + bp + ".csv"
