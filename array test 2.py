import numpy as np
from PIL import Image

a = np.array([[[4,0],[6,2]],[[5,1],[7,3]]])
a = np.flip(a, (2))
a = a.transpose((2,1,0))
print(a)
