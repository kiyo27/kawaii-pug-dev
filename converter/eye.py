import parser

input_file = 'eye.dt3'
pallet = {
  253: (44, 96, 128),
  255: (0, 0, 0)
}

def generate(canvas, height, width):
 
    f = parser.parse(input_file)

    for i in range(height):
      for j in range(width):
       if f.iloc[i][j] != 0:
         canvas[i,j] = pallet[f.iloc[i][j]]
    
    return canvas

