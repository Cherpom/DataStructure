import os
import shutil
import time
import numpy as np
import cv2 as cv
import PIL as pil

def convert_BWimage(pathname):
    image = pil.Image.open(pathname)
    return image.convert(mode="1", dither=Image.NONE)

#get image form directory
#open 2 image files

#use opencv (cv2) to compare images

#return 1-20 int as image
print("hhlle")