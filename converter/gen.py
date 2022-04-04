import cv2 as cv
from PIL import Image
import random
import csv
import os
import blueprint as bp
import canvas

height = 24
width = 24


def write(character):
    l = [get_filename_without_ext(character.shape.edge),
        get_filename_without_ext(character.shape.eyes),
       get_filename_without_ext(character.shape.mouth),
       get_filename_without_ext(character.color.base),
       get_filename_without_ext(character.color.eyes),
       get_filename_without_ext(character.color.ears),
       get_filename_without_ext(character.attributes.face),
       get_filename_without_ext(character.attributes.head),
       get_filename_without_ext(character.attributes.neck),
       get_filename_without_ext(character.attributes.mouth),
       get_filename_without_ext(character.attributes.eyes)]

    with open('result.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(l)

def header():
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

def get_filename_without_ext(path):
    if path is None:
        return
    return  os.path.splitext(
          os.path.basename(path))[0]


created = []
total = 100
count = 0
# generate image
header()
while count < total:
    l = ['Pug', 'SleepingPug']
    c = random.choice(l)
    p = bp.Character.get_factory(c)
    p.create()
    # compare to alredy created character instances.
    if not created:
        print('instance created first time.')
        created.append(p) 
        write(p)
        count += 1
        continue

    new = []
    for _, ins in enumerate(created):
        if p != ins:  
            created.append(ins)
            write(p)
            count += 1
            break


painter = canvas.Painter(width, height)
painter.drawColor(p)
painter.drawShape(p)
painter.drawAttributes(p)

interpolation = cv.INTER_AREA
canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()
#
