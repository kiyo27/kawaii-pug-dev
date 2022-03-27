import parser
import numpy as np


_BLUEPRINT_DIR = 'blueprints/'

# Blueprints
def glasses():
    blueprint_dir = _BLUEPRINT_DIR + 'attributes/eyes/'
    return blueprint_dir + 'vr.csv'    

def mouth():
    pass

def face():
    pass

def head():
    pass

def background():
    pass


class Pug:
    def __init__(self):
        blueprint_dir = _BLUEPRINT_DIR + 'types/pug/'

        self.__blueprints = {
            'color_eye_right': blueprint_dir + 'color/eye_right.csv',
            'color_eye_left': blueprint_dir + 'color/eye_left.csv',
            'color_ear_right': blueprint_dir + 'color/ear_right.csv',
            'color_ear_left': blueprint_dir + 'color/ear_left.csv',
            'color_mouth': blueprint_dir + 'color/mouth.csv',
            'color_face': blueprint_dir + 'color/face.csv',
            'color_body': blueprint_dir + 'color/body.csv',
            'shape_shape': blueprint_dir + 'shape/shape.csv',
            'shape_eye': blueprint_dir + 'shape/eye.csv'      
            #shapeからmouthの輪郭を取り除く
            #shapeからeyeの輪郭を取り除く
            #'shape_mouth': blueprint_dir + 'shape/mouth.csv'
        }

    @property
    def blueprints(self):
        return self.__blueprints

    def add_blueprint(self, key, blueprint):
        self.blueprints[key] = blueprint


class AndroidPug(Pug):
    def __init__(self):
        super().__init__()
        blueprint_dir = _BLUEPRINT_DIR + 'types/androidpug/'
        self.blueprints.clear()
        """
        TODO:
          - colorを作成する
            - face, body, mouth, ear, eye, てかり
        """
        self.add_blueprint('face', blueprint_dir + 'androidpug.csv')
        
    def add_blueprint(self, key, blueprint):
        super().add_blueprint(key, blueprint)

