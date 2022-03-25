import parser
import numpy as np

class Pug:
    def __init__(self, width, height):
        self.canvas = np.zeros((height, width, 3))
        self.canvas += (144, 128, 112)
        self.width = width
        self.height = height

        self.draw('edge.dt3')
        self.draw('hair.dt3')
        self.draw('ears.dt3')
        self.draw('eyes.dt3')
        self.draw('mouth.dt3')
        self.draw('wrinkles.dt3')

        self.attributes = {
            'glasses': None
        }

    def draw(self, doc):
        f = parser.parse(doc)
        paretto = self.__paretto()

        for i in range(self.height):
            for j in range(self.width):
                if f.iloc[i][j] != 0:
                    self.canvas[i,j] = paretto[f.iloc[i][j]]
        print(doc)

    def glasses(self):
        #self.draw('3d-glasses.dt3')
        self.draw('vr.dt3')
        self.attributes['glasses'] = '3d glasses'

    def cigarret(self):
        self.draw('cigarette.dt3')
        self.attributes['cigarret'] = 'cigarette'

    def get_canvas(self):
        return self.canvas 

    def __paretto(self):
        return {
            245: (70, 53, 177),
            246: (169, 169, 169),
            247: (211, 211, 211),
            248: (255, 0, 0),
            249: (0, 0, 255),
            250: (255, 255, 255),
            253: (44, 96, 128),
            254: (213, 239, 255),
            255: (0, 0, 0)
        }


