import parser
import numpy as np

class Pug:
    def __init__(self, width, height):
        self.canvas = np.zeros((height, width, 3))
        self.canvas += (144, 128, 112)
        self.width = width
        self.height = height

        self.draw('templates/edge.csv')
        self.draw('templates/hair.csv')
        self.draw('templates/ears.csv')
        self.draw('templates/eyes.csv')
        self.draw('templates/mouth.csv')
        self.draw('templates/wrinkles.csv')

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

    def add_attribute(self, tmplate):
        pass

    def glasses(self):
        #self.draw('3d-glasses.dt3')
        self.draw('templates/vr.csv')
        self.attributes['glasses'] = '3d glasses'

    def cigarret(self):
        self.draw('templates/cigarette.csv')
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


