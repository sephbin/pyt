import numpy as np
from PIL import Image


im = Image.open('uv2.png')
# dst_grid = griddify(shape_to_rect(im.size), 4, 4)
# src_grid = distort_grid(dst_grid, 50)
# mesh = grid_to_mesh(src_grid, dst_grid)
w, h = im.size
mesh = [(
		(0, 0, 1024, 1024),
		(520,-911,-405,709,990,2090,1931,442),
		# (0,2048,2048,4096,4096,2048,2048,0)
		),
		# (0, 0, 0, h, w, h, w, 0)),
		]

im = im.transform(im.size, Image.MESH, mesh)
im.show()