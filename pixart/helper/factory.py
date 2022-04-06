import random
import os
import csv
from  pixart import abstract


class Multiple:

    def __init__(self):
          self.created = []

    def create(self, types, mod, total=50):
        self. _header()
        count = 0

        while count < total:
            c = random.choice(types)
            p = abstract.Character.get_factory(mod, c)
            p.create()

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
        l = [character.ctype,
            self._name(character.color.base),
            self._name(character.attributes.face),
            self._name(character.attributes.head),
            self._name(character.attributes.neck),
            self._name(character.attributes.mouth),
            self._name(character.attributes.eyes)
        ]

        with open('result.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(l)

    def _header(self):
        l = ['type',
            'attributes_face',
            'attributes_head',
            'attributes_neck',
            'attributes_mouth',
            'attributes_eyes'
        ]

        with open('result.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(l)

    def _name(self, path):
        if path is None:
            return
        return  os.path.splitext(
              os.path.basename(path))[0]

