import numpy as np
from pixart import parser

_paretto = {
    227: (0, 215, 255),
    228: (0, 165, 255),
    229: (0, 128, 128),
    230: (255, 255, 0),
    231: (128, 128, 0),
    232: (32, 165, 218),
    233: (0, 252, 124),
    234: (0, 255, 255),
    235: (113, 179, 60),
    236: (225, 105, 65),
    237: (221, 160, 221),
    238: (0, 215, 255),
    239: (47, 255, 173),
    240: (220, 220, 220),
    241: (144, 128, 112),
    242: (192, 192, 192),
    243: (128, 128, 240),
    244: (203, 192, 255),
    245: (70, 53, 177),
    246: (169, 169, 169),
    247: (211, 211, 211),
    248: (255, 0, 0),
    249: (0, 0, 255),
    250: (255, 255, 255),
    251: (119, 191, 201),
    252: (255, 149, 255),
    253: (44, 96, 128),
    254: (213, 239, 255),
    255: (0, 0, 0)
}


class Painter:
    def __init__(self, width, height, paretto=None):
        self.width = width
        self.height = height
        if paretto is None:
            self.paretto = _paretto
        else:
            self.paretto = paretto
        self.canvas = np.zeros((height, width, 3))
        self.background = (144, 128, 112)
        self.canvas += self.background

    def draw(self, blueprint):
        if blueprint is not None:
            f = parser.parse(blueprint)

            for i in range(self.height):
                for j in range(self.width):
                    if f.iloc[i][j] == 1:
                        self.canvas[i,j] = self.background
                    elif f.iloc[i][j] != 0:
                        self.canvas[i,j] = self.paretto[f.iloc[i][j]]
      
    def drawShape(self, c):
        self.draw(c.shape.edge)
        self.draw(c.shape.eyes)
        self.draw(c.shape.mouth)

    def drawColor(self, c):
        self.draw(c.color.base)
        self.draw(c.color.eyes)
        self.draw(c.color.ears)

    def drawAttributes(self, c):
        self.draw(c.attributes.face)
        self.draw(c.attributes.head)
        self.draw(c.attributes.neck)
        self.draw(c.attributes.mouth)
        self.draw(c.attributes.eyes)

