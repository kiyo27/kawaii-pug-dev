import cv2 as cv
import numpy as np
import pandas as pd
import csv
from PIL import Image

height = 24
width = 24
canvas = np.zeros((height, width, 3))
canvas += 255

f = pd.read_csv('output_edge.csv', header=None)

for i in range(height):
  for j in range(width):
   if f.iloc[i,j] == 255:
     canvas[i,j] = (0,0,0)


interpolation = cv.INTER_AREA
canvas = cv.resize(canvas, None, 0, 10,10,interpolation)
cv.imwrite('output.png', canvas)

img = Image.open('output.png')
img.show()
