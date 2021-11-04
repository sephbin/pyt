import cv2 
import numpy as np
# from matplotlib import pyplot as plt

img_plan = cv2.imread('test.png')
template = cv2.imread('template.png')

w = template.shape[1]
h = template.shape[0]

img_grey = cv2.cvtColor(img_plan,cv2.COLOR_BGR2GRAY)
cont_nz = cv2.countNonZero(img_grey)

result = cv2.matchTemplate(img_plan,template,cv2.TM_CCOEFF_NORMED)
# print(col_px)
for x in range(w):
	for y in range(h):
		x_col = x
		y_col = y
		tx = img_plan[x_col,y_col]
		if tx[0] != 0:
			print(tx)
###min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
threshold = 0.99

yloc, xloc = np.where( result >= threshold)
###rect = cv2.rectangle(img_plan, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,0,255), 1)
###print(rect)
loc_pt = []
rect_loc =[]
for (x,y) in zip(xloc, yloc):
	rect = cv2.rectangle(img_plan, (x,y), (x+ w, y + h), (0,0,255), 1)
	loc_pt.append((int(x),int(y),int(w),int(h)))
	rect_loc.append(rect)
	print(x,y)

with open("matrix/test.txt", "w") as txt:
	txt.write(str(loc_pt))

with open("matrix/test2.txt", "w") as txt:
	txt.write(str(rect_loc))

print(f"number of detection: {len(loc_pt)}")
print(f"number of non-black pixels: {cont_nz}")
cv2.imwrite('test2.png',img_plan)
cv2.imshow('plan',img_plan)
cv2.waitKey(0)