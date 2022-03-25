import parser

input_file = 'hair.dt3'
color = (213, 239, 255)
target = 1

def generate(canvas, height, width):
 
    f = parser.parse(input_file)

    for i in range(height):
      for j in range(width):
       if f.iloc[i][j] == target:
         canvas[i,j] = color
    
    return canvas

