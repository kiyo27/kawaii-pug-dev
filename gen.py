import cv2 as cv
from PIL import Image
from pixart import canvas, parser
from pixart.helper import factory

f = factory.Multiple()
f.create(['Pug', 'SleepingPug'], 'character')
c = f.created[1]
print(c.ctype)

height = 24
width = 24

#painter = canvas.Painter(width, height)
#painter.drawColor(p)
#painter.drawShape(p)
#painter.drawAttributes(p)
#
#interpolation = cv.INTER_AREA
#canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
#cv.imwrite('output.png', canvas)
#
#img = Image.open('output.png')
#img.show()

