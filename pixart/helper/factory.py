import csv
import os
import random

from pixart import abstract
from pixart.io.sqlite import write_sqlite, delete_table


def factory(modname, cname):
    return abstract.Character.get_factory(modname, cname)
    

class Multiple:
    def __init__(self):
        self.created = []
        delete_table()

    def create(self, types, mod, total=50):
        count = 0

        while count < total:
            c = random.choice(types)
            p = abstract.Character.get_factory(mod, c)
            p.create(count + 1)

            if not self.created:
                self.created.append(p)
                write_sqlite(p)
                count += 1
                continue

            l = len(self.created)
            for i, ins in enumerate(self.created):
                if p == ins:
                    break

                if i == l - 1:
                    self.created.append(p)
                    write_sqlite(p)
                    count += 1
                    break

