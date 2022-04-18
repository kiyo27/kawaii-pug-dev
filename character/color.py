from pixart import abstract
from character import attribute


class PugColor(abstract.Color):
    def __init__(self, **kwargs):
        self.base_dir = "character/blueprints/base/color/"
        self.make(**kwargs)

    @property
    def skin(self):
        return self._skin

    def make(self, **kwargs):
        if "skin" in kwargs:
            self._skin = self.base_dir + kwargs["skin"] + ".csv"
        else:
            n = ['rainbow', 'metallic', 'basic']
            w = [1, 5, 10]
            attr = {'names': n, 'weights': w}
            bp = attribute.choice(self.base_dir, attr)
            self._skin = bp
