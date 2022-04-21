from pixart import abstract


class PugShape(abstract.Shape):
    def __init__(self, **kwargs):
        self.base_dir = "character/blueprints/base/shape/"
        self.make(**kwargs)

    @property
    def edge(self):
        return self._edge

    @property
    def eyes(self):
        return self._eyes

    @property
    def mouth(self):
        return self._mouth

    def make(self, **kwargs):
        self.makeEdge(**kwargs)
        self.makeEyes(**kwargs)
        self.makeMouth(**kwargs)

    def makeEdge(self, **kwargs):
        bp_dir = self.base_dir + "edge/"
        if "edge" in kwargs:
            self._edge = bp_dir + kwargs["edge"] + ".csv"
        else:
            self._edge = bp_dir + "basic.csv"

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + "eyes/"
        if "eyes" in kwargs:
            if kwargs["eyes"]:
                self._eyes = bp_dir + kwargs["eyes"] + ".csv"
            else:
                self._eyes = None
        else:
            self._eyes = bp_dir + "basic.csv"

    def makeMouth(self, **kwargs):
        bp_dir = self.base_dir + "mouth/"
        if "mouth" in kwargs:
            self._mouth = bp_dir + kwargs["mouth"] + ".csv"
        else:
            self._mouth = bp_dir + "basic.csv"
