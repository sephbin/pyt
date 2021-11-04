import numpy as np
from PIL import Image

finalMatrix = None
matrixes = {
	"xy" : [],
	"xz" : [],
	"yz" : [],
}
full = 512
steps = 2**2
index = 0
for plane in matrixes:
	for r in range(steps):
		try:
			position = int(r*(full/steps))
			print(position)
			image = image = Image.open(r'D:\Users\s-abutler\Documents\GitHub\media\gorgon\b0\0\png\resize\%s%s-%s.png'%(plane,position,int(steps)))
			image = image.convert("1")
			voxSlice = np.asarray(image)
			print("vx",voxSlice)
			matrixes[plane].append(voxSlice)
		except Exception as e:
			print("e",e)
			matrixes[plane].append(np.zeros((steps,steps)))
	matrixes[plane] = np.array(matrixes[plane])
	if plane =="xz":
		print(matrixes[plane])
		matrixes[plane] = matrixes[plane].transpose((1,0,2))
		matrixes[plane] = np.flip(matrixes[plane], (1))
		matrixes[plane] = np.flip(matrixes[plane], (0))
	if plane =="yz":
		matrixes[plane] = np.flip(matrixes[plane], (2))
		matrixes[plane] = matrixes[plane].transpose((1,2,0))
		matrixes[plane] = np.flip(matrixes[plane], (0))
	try:
		if not finalMatrix:
			finalMatrix = matrixes[plane]
	except:
		finalMatrix = finalMatrix+matrixes[plane]
for n, cut in enumerate(finalMatrix):
	cut = np.array(cut, dtype=bool)
	size = cut.shape[::-1]
	databytes = np.packbits(cut, axis=1)
	nm = Image.frombytes(mode='1', size=size, data=databytes)
	nm.save('%s.png'%(n))
