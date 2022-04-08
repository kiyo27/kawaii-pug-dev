import os
import random
from pixart import abstract


class PugAttribute:
    def __init__(self, obj, **kwargs):
        self.base_dir = 'character/blueprints/attributes/'
        self._obj = obj
        self.make(**kwargs)

    def __eq__(self, other):
        if (self.face == other.face
              and self.head == other.head
              and self.neck == other.neck
              and self.mouth == other.mouth):
            return True
        return False

    @property
    def face(self):
        return self._face

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

    def make(self, **kwargs):
        self.makeFace(**kwargs)
        self.makeHead(**kwargs)
        self.makeNeck(**kwargs)
        self.makeMouth(**kwargs)
        self.makeEyes(**kwargs)

    def choice(self, path):
        target = []
        with os.scandir(path) as it:
            for d in it:
                if d.name.endswith('.csv') and d.is_file():
                    target.append(d.name)
        return path + random.choice(target) 

    def makeFace(self, **kwargs):
        bp_dir = self.base_dir + 'face/'
        if 'face' in kwargs:
            self._face = bp_dir + kwargs['face'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._face = None
            else:
                self._face = self.choice(bp_dir) 

    def makeHead(self, **kwargs):
        bp_dir = self.base_dir + 'head/'
        if 'head' in kwargs:
            self._head = bp_dir + kwargs['head'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._head = None
            else:
                self._head = self.choice(bp_dir) 

    def makeNeck(self, **kwargs):
        bp_dir = self.base_dir + 'neck/'
        if 'neck' in kwargs:
            self._neck = bp_dir + kwargs['neck'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._neck = None
            else:
                self._neck = self.choice(bp_dir) 

    def makeMouth(self, **kwargs):
        bp_dir = self.base_dir + 'mouth/'
        if 'mouth' in kwargs:
            if kwargs['mouth'] is False:
                self._mouth = None
            else:
                self._mouth = bp_dir + kwargs['mouth'] + '.csv'
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._mouth = None
            else:
                self._mouth = self.choice(bp_dir) 

    def makeEyes(self, **kwargs):
        bp_dir = self.base_dir + 'eyes/'
        if self.face is not None:
            self._eyes = None
        elif 'eyes' in kwargs:
            self._eyes = kwargs['eyes']
        else:
            r = random.randrange(0, 9)
            if r <= 7:
                self._eyes = None
            else:
                self._eyes = self.choice(bp_dir) 
