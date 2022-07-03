import click
import random
import concurrent.futures
from pixart import canvas, abstract
from pixart.helper import factory, director
from pixart.io import opencv, sqlite
from PIL import Image


@click.command("create")
@click.option("--multiple", type=int)
@click.option("--no-preview", is_flag=True)
@click.option("--from-db", is_flag=True)
def cli(multiple, no_preview, from_db):

    if from_db:
        data = sqlite.select()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(director.construct,[data[0:200]])

    face_types = ["Pug", "SleepingPug", "AnonyPug", "KabukiPug", "PhantomPug"]
    if multiple:
        p = factory.Multiple()
        p.create(face_types, "character", total=multiple)
    else:
        c = random.choice(face_types)
        p = abstract.Character.get_factory("character", c)
        p.create(1)
        painter = canvas.Painter()
        painter.draw(p)
        out_file = "img/output.png"
        opencv.generate(painter.canvas, out_file)
        if not no_preview:
            img = Image.open(out_file)
            img.show()