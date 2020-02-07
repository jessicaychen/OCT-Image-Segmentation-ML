#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:01:38 2020

@author: JessicaChen
"""

from IPython import get_ipython
get_ipython().magic('reset -sf')

import os
from PIL import Image
#import numpy as np
#import cv2 
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg


#save_dir = r'/Users/JessicaChen/Desktop/ML Data/Processed-input/' 
save_dir = r'/Users/JessicaChen/Desktop/ML Data/Processed-mask/' 
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

#path = "/Users/JessicaChen/Desktop/ML Data/Original cSLOs/"
path = "/Users/JessicaChen/Desktop/ML Data/Masked cSLOs/"
dirs = os.listdir(path)

# resize images to 256x256
def process():
    for item in dirs:
        if not item.startswith('.')  and os.path.isfile(os.path.join(path, item)):
             im = Image.open(path + item).convert("L")         #grayscale
             f = os.path.splitext(item)[0]
             new_dir = str(save_dir) + str(f)
             imResize = im.resize((256,256), Image.ANTIALIAS)  #resize
             imResize.save(new_dir + '.jpg', 'JPEG', quality=90)
process()



# Check
#import matplotlib.pyplot as plt

#img = plt.imread('/Users/JessicaChen/Desktop/ML Data/Processed/cSLO00.jpg')
#plt.imshow(img,cmap = "gray")
#print(img.shape) # (256,256) - 1 channel/grayscaled




