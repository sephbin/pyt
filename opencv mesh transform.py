import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
# Read input image and convert to float

imgS = cv2.imread("uv2.png")

# recenter resultant image
T_pos1000 = np.array([
    [1, 0, 1000],
    [0, 1, 1000],
    [0, 0, 1]])
# rotate - opposite angle
T_rotate = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]])
# scale
T_scale = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 1]])
# center original to 0,0
T_neg500 = np.array([
    [1, 0, -500],
    [0, 1, -500],
    [0, 0, 1]])
T = T_pos1000 @ T_rotate @ T_scale @ T_neg500
print(T)
T_inv = np.linalg.inv(T)


T_opencv = np.float32(T.flatten()[:6].reshape(2,3))
img_transformed = cv2.warpAffine(imgS, T_opencv, (4096, 4096 ))


img = cv2.cvtColor(img_transformed, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img, 'RGB')
img.show()

