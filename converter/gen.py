import cv2 as cv
from PIL import Image
import blueprint
import canvas

height = 24
width = 24

# generate image
p = blueprint.Pug()
#p = blueprint.AndroidPug()
#p.add_attribute('eyes')
painter = canvas.Painter(width, height)
painter.drawColor(p)
painter.drawShape(p)
painter.drawAttributes(p)

interpolation = cv.INTER_AREA
canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()

