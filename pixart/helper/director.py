from pixart.helper import factory
from pixart import canvas
from pixart.io import opencv


def construct(data, preview=False):
    for row in data:
        p = factory.factory("character", row["type"])
        p.create(row['id'], attributes=row["attributes"], skin=row["skin"])
        painter = canvas.Painter(24, 24)
        painter.draw(p)
        out_file = f"img/{row['id']}.png"
        opencv.generate(painter.canvas, out_file)
        if preview:
            img = Image.open(out_file)
            img.show()

