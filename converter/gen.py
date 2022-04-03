import cv2 as cv
from PIL import Image
import random
import blueprint as bp
import canvas

height = 24
width = 24

created = []
total = 100
# generate image
for _ in range(total):
    l = ['Pug', 'SleepingPug']
    c = random.choice(l)
    p = bp.Character.get_factory(c)
    p.create()
    # compare to alredy created character instances.
    if not created:
        print('instance created first time.')
        created.append(p) 

    new = []
    for _, ins in enumerate(created):
        if p != ins:  
            new.append(ins) 
            break

    created.extend(new)
print(len(created) / total)

#painter = canvas.Painter(width, height)
#painter.drawColor(p)
#painter.drawShape(p)
#painter.drawAttributes(p)
#
#interpolation = cv.INTER_AREA
#canvas = cv.resize(painter.canvas, None, 0, 10,10,interpolation)
#cv.imwrite('output.png', canvas)
#
#img = Image.open('output.png')
#img.show()
#
