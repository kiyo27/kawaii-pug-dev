import random
import os
import csv
from  pixart import abstract


class Multiple:

    def __init__(self, types=None, total=None):
          self.total = 50
          self.created = []

    def create(self):
        self. _header()

        count = 0

        while count < self.total:
            types = ['Pug', 'SleepingPug']
            c = random.choice(types)
            p = abstract.Character.get_factory('character', c)
            p.create()
            # compare to alredy created character instances.
            if not self.created:
                self.created.append(p) 
                self._write(p)
                count += 1
                continue

            new = []
            l = len(self.created)
            for i, ins in enumerate(self.created):
                if p == ins:
                    break

                if i == l - 1:
                    self.created.append(p)
                    self._write(p)
                    count += 1
                    break

    def _write(self, character):
        l = [self._name(character.shape.edge),
            self._name(character.shape.eyes),
           self._name(character.shape.mouth),
           self._name(character.color.base),
           self._name(character.color.eyes),
           self._name(character.color.ears),
           self._name(character.attributes.face),
           self._name(character.attributes.head),
           self._name(character.attributes.neck),
           self._name(character.attributes.mouth),
           self._name(character.attributes.eyes)]

        with open('result.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(l)

    def _header(self):
        l = ['shape_edge',
            'shape_eyes',
            'shape_mouth',
            'color_base',
            'color_eyes',
            'color_ears',
            'attributes_face',
            'attributes_head',
            'attributes_neck',
            'attributes_mouth',
            'attributes_eyes']

        with open('result.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(l)

    def _name(self, path):
        if path is None:
            return
        return  os.path.splitext(
              os.path.basename(path))[0]


