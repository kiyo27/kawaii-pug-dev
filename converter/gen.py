import cv2 as cv
import numpy as np
import pandas as pd
import csv
from PIL import Image

import edge
import hair
import sub_hair
import eye
import mouth
import wrinkles

height = 24
width = 24
canvas = np.zeros((height, width, 3))
canvas += 255

# generate image
canvas = edge.generate(canvas, height, width)
canvas = hair.generate(canvas, height, width)
canvas = sub_hair.generate(canvas, height, width)
canvas = eye.generate(canvas, height, width)
canvas = mouth.generate(canvas, height, width)
canvas = wrinkles.generate(canvas, height, width)



interpolation = cv.INTER_AREA
canvas = cv.resize(canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()

