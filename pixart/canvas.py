import numpy as np
from pixart import parser

_paretto = {
    185: (205, 73, 0),
    186: (202, 58, 0),
    187: (223, 84, 0),
    189: (5, 221, 247),
    190: (172, 181, 39),
    191: (163, 43, 99),
    192: (219, 112, 147),
    193: (181, 174, 163),
    194: (234, 234, 236),
    195: (0, 52, 153),
    196: (13, 88, 211),
    197: (50, 205, 50),
    198: (105, 105, 105),
    199: (112, 66, 29),
    200: (11, 134, 184),
    201: (32, 165, 218),
    202: (50, 205, 50),
    203: (255, 144, 30),
    204: (92, 92, 205),
    205: (211, 0, 148),
    206: (211, 85, 186),
    207: (128, 0, 128),
    208: (199, 212, 212),
    209: (72, 74, 72),
    210: (171, 169, 171),
    211: (231, 235, 235),
    212: (250, 206, 135),
    213: (25, 53, 68),
    214: (6, 57, 98),
    215: (8, 82, 149),
    216: (0, 215, 255),
    217: (0, 165, 255),
    218: (0, 128, 128),
    219: (255, 255, 0),
    220: (128, 128, 0),
    221: (32, 165, 218),
    222: (0, 252, 124),
    223: (0, 255, 255),
    224: (113, 179, 60),
    225: (225, 105, 65),
    226: (221, 160, 221),
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

    def map(self, blueprint):
        if blueprint is not None:
            f = parser.parse(blueprint)

            for i in range(self.height):
                for j in range(self.width):
                    if f.iloc[i][j] == 1:
                        self.canvas[i,j] = self.background
                    elif f.iloc[i][j] != 0:
                        self.canvas[i,j] = self.paretto[f.iloc[i][j]]

    def draw(self, c):
        self.map(c.shape.edge)

        self.map(c.color.base)
        self.map(c.color.eyes)
        self.map(c.color.ears)

        self.map(c.shape.mouth)

        self.map(c.attributes.head)
        self.map(c.attributes.neck)
        self.map(c.attributes.nose)
        self.map(c.attributes.mouth)
        self.map(c.attributes.eyes)
        self.map(c.attributes.face)

        self.map(c.shape.eyes)
        self.map(c.attributes.goggle)

