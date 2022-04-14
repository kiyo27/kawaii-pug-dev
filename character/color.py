from pixart import abstract


class PugColor(abstract.Color):
    def __init__(self, **kwargs):
        self.base_dir = "character/blueprints/base/color/"
        self.make(**kwargs)

    @property
    def base(self):
        return self._base

    def make(self, **kwargs):
        if 'color' in kwargs:
            self._base = self.base_dir + kwargs['color'] + '.csv'
        else:
            self._base = self.base_dir + "basic.csv"
