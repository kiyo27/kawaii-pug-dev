import cv2 as cv
from PIL import Image
from pixart import canvas, parser
from pixart.helper import factory
from pixart.io import sqlite

#f = factory.Multiple()
#face_types = ['Pug', 'SleepingPug']
#f.create(face_types, 'character', total=1000)
#c = f.created[1]

from character import types

p = types.KabukiPug()
attr = {}
p.create(1, **attr)
#
height = 24
width = 24

painter = canvas.Painter(width, height)

painter.draw(p)

interpolation = cv.INTER_AREA
canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
cv.imwrite('img/output.png', canvas)
img = Image.open('img/output.png')
img.show()

#sqlite.export_csv()

#for p in f.created:
#    painter.drawColor(p)
#    painter.drawShape(p)
#    painter.drawAttributes(p)
#
#    interpolation = cv.INTER_AREA
#    canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
#    cv.imwrite('output.png', canvas)

#img = Image.open('img/output.png')
#img.show()

