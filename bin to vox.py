import numpy as np
from PIL import Image

def img_frombytes(data):
	size = data.shape[::-1]
	databytes = np.packbits(data, axis=1)
	return Image.frombytes(mode='1', size=size, data=databytes)

with open(r"D:\Users\s-abutler\Downloads\vox.txt", "r") as f:
	content = f.read().split("|")
	y, x, z, string = tuple(content)
	x, y, z = int(x),int(y),int(z)
	string = list(map(lambda x: bool(int(x)), string))
print(x,y,z)
# print(string)

string = np.array(string)
string = list(np.array_split(string, x))
print(string)
# string = np.array_split(string, y)
# string = np.array_split(string, z)
size = 512
string = [string[51]]

for center in string:
	# center = np.full((x, y), True)

	print(center.shape)
	h_pad = int((size-center.shape[1])/2)
	v_pad = int((size-center.shape[0])/2)
	print(h_pad)

	h = np.full((center.shape[0],h_pad),False)

	matrix = np.concatenate((h,center,h), axis=1)

	v = np.full((v_pad,matrix.shape[1]),False)
	matrix = np.concatenate((v,matrix,v), axis=0)

	im = img_frombytes(matrix)
	im.save("D:\\Users\\s-abutler\\Downloads\\vox.png", "PNG")