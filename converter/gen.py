import cv2 as cv
from PIL import Image
from pug import Pug

height = 24
width = 24

# generate image
p = Pug(width, height)
p.glasses()
p.cigarret()
canvas = p.get_canvas()

interpolation = cv.INTER_AREA
canvas = cv.resize(canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()

