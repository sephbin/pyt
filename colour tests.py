import colorsys
import numpy as np
pointColour = np.array(colorsys.hsv_to_rgb(.5,1,1))*(256**2)
print(pointColour)