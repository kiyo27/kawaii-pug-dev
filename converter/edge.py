import parser

input_file = 'edge.dt3'
edge_color = (0, 0, 0)
target = 255

def generate(canvas, height, width):
 
    f = parser.parse(input_file)

    for i in range(height):
      for j in range(width):
       if f.iloc[i][j] == target:
         canvas[i,j] = edge_color
    
    return canvas

