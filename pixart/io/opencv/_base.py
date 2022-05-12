import cv2 as cv


def generate(canvas, filename):
    interpolation = cv.INTER_AREA
    canvas = cv.resize(canvas, None, 0, 13,13,interpolation)
    cv.imwrite(filename, canvas)

