import csv
import os
import random

from pixart import abstract


class Multiple:
    def __init__(self):
        self.created = []

    def create(self, types, mod, total=50):
        self._header()
        count = 0

        while count < total:
            c = random.choice(types)
            p = abstract.Character.get_factory(mod, c)
            p.create(count + 1)

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
        with open("result.csv", "a") as f:
            writer = csv.writer(f)
            for l in self._pivot(character):
                writer.writerow(l)

    def _pivot(self, character):
        l = []
        l.append(
            [
                character.num,
                character.ctype,
                self._name(character.color.base),
                self._name(character.attributes.face),
            ]
        )

        l.append(
            [
                character.num,
                character.ctype,
                self._name(character.color.base),
                self._name(character.attributes.head),
            ]
        )

        l.append(
            [
                character.num,
                character.ctype,
                self._name(character.color.base),
                self._name(character.attributes.neck),
            ]
        )

        l.append(
            [
                character.num,
                character.ctype,
                self._name(character.color.base),
                self._name(character.attributes.mouth),
            ]
        )

        l.append(
            [
                character.num,
                character.ctype,
                self._name(character.color.base),
                self._name(character.attributes.eyes),
            ]
        )

        return l

    def _header(self):
        l = ["#", "type", "color", "attribute"]

        with open("result.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(l)

    def _name(self, path):
        if path is None:
            return None
        return os.path.splitext(os.path.basename(path))[0]
