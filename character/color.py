from pixart import abstract

class PugColor(abstract.Color):
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
