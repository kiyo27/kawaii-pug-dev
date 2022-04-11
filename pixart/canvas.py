import numpy as np

from pixart import parser

_paretto = {
    255: (0,0,0),
    254: (213,239,255),
    253: (44,96,128),
    252: (255,149,255),
    251: (119,191,201),
    250: (255,255,255),
    249: (0,0,255),
    248: (255,0,0),
    247: (211,211,211),
    246: (169,169,169),
    245: (70,53,177),
    244: (203,192,255),
    243: (128,128,240),
    242: (192,192,192),
    241: (144,128,112),
    240: (220,220,220),
    #-------------------
    239: (47,255,173),
    238: (0,215,255),
    237: (221,160,221),
    236: (225,105,65),
    235: (113,179,60),
    234: (0,255,255),
    233: (0,252,124),
    232: (32,165,218),
    231: (128,128,0),
    230: (255,255,0),
    229: (0,128,128),
    228: (0,165,255),
    227: (0,215,255),
    226: (8,82,149),
    225: (6,57,98),
    224: (25,53,68),
    #-------------------
    223: (250,206,135),
    222: (231,235,235),
    221: (171,169,171),
    220: (72,74,72),
    219: (199,212,212),
    218: (128,0,128),
    217: (211,85,186),
    216: (211,0,148),
    215: (92,92,205),
    214: (255,144,30),
    213: (50,205,50),
    212: (32,165,218),
    211: (11,134,184),
    210: (112,66,29),
    209: (105,105,105),
    208: (50,205,50),
    #-------------------
    207: (13,88,211),
    206: (0,52,153),
    205: (234,234,236),
    204: (181,174,163),
    203: (219,112,147),
    202: (163,43,99),
    201: (172,181,39),
    200: (5,221,247),
    199: (223,84,0),
    198: (202,58,0),
    197: (205,73,0)
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
                        self.canvas[i, j] = self.background
                    elif f.iloc[i][j] != 0:
                        self.canvas[i, j] = self.paretto[f.iloc[i][j]]

    def draw(self, c):
        self.map(c.shape.edge)

        self.map(c.color.base)
        self.map(c.color.eyes)
        self.map(c.attributes.eyes)
        self.map(c.color.ears)
        self.map(c.attributes.ears)

        self.map(c.shape.mouth)

        self.map(c.attributes.neck)
        self.map(c.attributes.nose)
        self.map(c.attributes.face)

        self.map(c.shape.eyes)
        self.map(c.attributes.goggle)
        self.map(c.attributes.head)
        self.map(c.attributes.mouth)
