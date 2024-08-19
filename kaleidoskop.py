from PIL import Image, ImageOps
import numpy as np
import math
import sys

from numpy.core.fromnumeric import size

# parameters
s = 10
# error if no argument provided:
if not(len(sys.argv) == 2):
    print("no size given. Please provide number! \nfor example: ''python3 kaleidoskop.py 5''")
else:
    s = int(sys.argv[1])
    # functions


def row(back, i0, i1, i2, i3, i4, i5, x, y):
    back.paste(i0, (int(x), int(y)), i0)
    back.paste(i1, (int(x+w/2), int(y-r)), i1)
    back.paste(i2, (int(x+w), int(y)), i2)
    back.paste(i3, (int(x+3/2*w), int(y-r)), i3)
    back.paste(i4, (int(x+2*w), int(y)), i4)
    back.paste(i5, (int(x+5/2*w), int(y-r)), i5)


# load image data
im = Image.open("input/img.png", 'r')
pix = np.array(im)
img = Image.fromarray(pix, "RGBA")
img_mirr = ImageOps.mirror(img)
w = im.size[0]*0.75
h = im.size[1]*0.75*(math.sqrt(3)/2)
bw = s*w
bh = s*h
r = h/3

# create empty image
back = Image.new('RGBA', (int(bw), int(bh)), color='white')

# create tiles
img0 = img
img1 = img_mirr.rotate(60)
img2 = img.rotate(-120)
img3 = img_mirr.rotate(180)
img4 = img.rotate(120)
img5 = img_mirr.rotate(-60)

for y in range(s):
    for x in range(-s, s):
        row(back, img0, img1, img2, img3, img4, img5, 3*w*x+y*1.5*w, y*h-r/3)


back.save("output/img.png", "PNG")
