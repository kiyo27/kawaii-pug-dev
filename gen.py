import cv2 as cv
from PIL import Image
import argparse
from pixart import canvas
from pixart.helper import factory
from pixart.io import sqlite, opencv


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", action="store_true", help="multiple create")
group.add_argument("-c", action="store_true", help="create at once")
group.add_argument("--from-db", dest="db", action="store_true", help="create from db")


def multiple():
    f = factory.Multiple()
    face_types = ["Pug", "SleepingPug", "AnonyPug",  "KabukiPug"]
    f.create(face_types, "character", 1, total=1000)
    #painter = canvas.Painter()
    #for p in f.created:
    #    painter.draw(p)
    #    out_file = 'img/output.png'
    #    opencv.generate(painter.canvas, out_file)


def create():
    from character import types
    p = types.KabukiPug()
    attr = {}
    p.create(1, **attr)
    painter = canvas.Painter()
    painter.draw(p)
    out_file = "img/output.png"
    opencv.generate(painter.canvas, out_file)
    img = Image.open(out_file)
    img.show()


# sqlite.export_csv()


def create_from_db():
    from pixart.helper import director
    import concurrent.futures
    data = sqlite.select(1)
    director.construct(data[0:10])
    
    #with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #    executor.map(director.construct,[data[0:100],data[100:200]])
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(director.construct,data[0:10])
        print(future)
        for f in concurrent.futures.as_completed([future]):
            print(f)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.m:
        multiple()
    elif args.c:
        create()
    elif args.db:
        create_from_db()
