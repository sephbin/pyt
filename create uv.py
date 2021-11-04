from PIL import Image  

width = 4096
height = 4096

img  = Image.new( mode = "RGB;32", size = (width, height) )

print(img.getpixel((0,0)))

img.show()

