import png

import numpy as np

# The following import is just for creating an interesting array
# of data.  It is not necessary for writing a PNG file with PyPNG.
from scipy.ndimage import gaussian_filter


# Make an image in a numpy array for this demonstration.
size = 4096

nrows = size
ncols = size
# np.random.seed(12345)
# x = np.random.randn(nrows, ncols, 3)
array = np.zeros((size,size,3), dtype=int)

y_array = []
for y_i, y in enumerate(array):
	x_array = []
	for x_i, x in enumerate(y):
		# x = x + [x_i/nrows, y_i/ncols, 0]
		x_array.append([x_i/size, 1-y_i/size, 0])
	y_array.append(x_array)

array = np.add(array,y_array)
print(array)
# y is our floating point demonstration data.
# y = gaussian_filter(x, (16, 16, 0))

# Convert y to 16 bit unsigned integers.
z = (65535*(array)).astype(np.uint16)
# Use pypng to write z as a color PNG.
with open('pillow test.png', 'wb') as f:
	writer = png.Writer(width=z.shape[1], height=z.shape[0], bitdepth=16 , greyscale=False)
	# Convert z to the Python list of lists expected by
	# the png writer.
	z2list = z.reshape(-1, z.shape[1]*z.shape[2]).tolist()
	writer.write(f, z2list)