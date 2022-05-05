import click
from pixart import canvas
from pixart.io import sqlite, opencv
from PIL import Image


@click.command("build")
def cli():
    from character import types
    p = types.SleepingPug()
    attr = {"attributes":{"glasses":"horned-rim-glasses"}}
    p.create(1, **attr)
    painter = canvas.Painter()
    painter.draw(p)
    out_file = "img/output.png"
    opencv.generate(painter.canvas, out_file)
    img = Image.open(out_file)
    img.show()