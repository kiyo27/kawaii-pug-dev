import cv2 as cv
from PIL import Image
import blueprint
import painter

height = 24
width = 24

# generate image
#p = blueprint.Pug()
p = blueprint.AndroidPug()
p.add_attribute('eyes')
canvas = painter.draw(width, height, p.blueprints, painter.PARETTO)

interpolation = cv.INTER_AREA
canvas = cv.resize(canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()

