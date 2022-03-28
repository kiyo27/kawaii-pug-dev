import numpy as np
import parser

PARETTO = {
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

# Painter
def draw(width, height, blueprints, paretto):
    canvas = np.zeros((height, width, 3))
    canvas += (144, 128, 112)

    for blueprint in blueprints:
        f = parser.parse(blueprint)

        for i in range(height):
            for j in range(width):
                if f.iloc[i][j] != 0:
                    canvas[i,j] = paretto[f.iloc[i][j]]
    return canvas

