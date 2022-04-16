import cv2 as cv
from PIL import Image
import argparse
from pixart import canvas, parser
from pixart.helper import factory
from pixart.io import sqlite, opencv


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", action="store_true", help="multiple create")
group.add_argument("-c", action="store_true", help="create at once")
group.add_argument("--from-db", dest="db", action="store_true", help="create from db")


def multiple():
    f = factory.Multiple()
    face_types = ['Pug', 'SleepingPug', 'KabukiPug']
    f.create(face_types, 'character', 1, total=1000)
    #c = f.created[1]
    height = 24
    width = 24
    painter = canvas.Painter(width, height)
    for p in f.created:
        painter.drawColor(p)
        painter.drawShape(p)
        painter.drawAttributes(p)
        opencv.generate(painter.canvas, out_file)


def create():
    from character import types
    p = types.KabukiPug()
    attr = {}
    p.create(1, **attr)

    height = 24
    width = 24

    painter = canvas.Painter(width, height)

    painter.draw(p)
    out_file = 'img/output.png'
    opencv.generate(painter.canvas, out_file)
    img = Image.open(out_file)
    img.show()

#sqlite.export_csv()


#img = Image.open('img/output.png')
#img.show()


def create_from_db():
    from pixart.helper import factory
    data = sqlite.select()
    for row in data:
        p = factory.factory('character', row['type'])
        p.create(1, **{'attributes':row['attributes']})
        painter = canvas.Painter(24, 24)
        painter.draw(p)
        out_file = 'img/output.png'
        opencv.generate(painter.canvas, out_file)
        img = Image.open(out_file)
        img.show()


if __name__ == '__main__':
    args = parser.parse_args()
    if args.m:
        multiple()
    elif args.c:
        create()
    elif args.db:
        create_from_db()
