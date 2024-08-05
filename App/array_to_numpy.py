import numpy as np
from PIL import Image

data=np.zeros((5, 4, 3), dtype=np.uint8)
data[:]=[255, 255, 0]
print(data)

data[1:3]=[255, 0, 0]  # change the colour of the rows
data[0:1, 1:3]=[0, 255, 0]  # change the colour of the columns

img=Image.fromarray(data, 'RGB')
img.save('canvas.png')