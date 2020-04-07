import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from PIL.Image import *

""" import the picture """

file = 'picture_path.png'
picture = open(file)


""" plot the picture """

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

def plot_gray(file):
    img = mpimg.imread(file)
    gray = rgb2gray(img)
    plt.imshow(gray, cmap = plt.get_cmap('gray'))
    plt.show()

def plot_color(file):
    imgpil = mpimg.imread(file)
    img = np.array(imgpil)
    plt.imshow(img)
    plt.show()


#picture size
def width_Height(picture):
    return(picture.size)

#convert the x,y pixel in gray
def turn_pixel_to_gray(x,y,picture):
    s = 0.21*picture.getpixel((x,y))[0]+0.71*picture.getpixel((x,y))[1]+0.07*picture.getpixel((x,y))[2]
    return(s/3)

#pixel value
def array_gray_pixels(picture): 
    l=[]
    (width,Height)=width_Height(picture)
    for x in range(Height):
        for y in range(width):
            l.append((turn_pixel_to_gray(y,x,picture)))
    return(l)

def array_coloured_pixels(picture):
    l=[]
    (width,Height)=width_Height(picture)
    for x in range(Height):
        for y in range(width):
            l.append((picture.getpixel((y,x))))
    return(l)


""" summary of all algorithms """ 

def pixels(x,y,file): #(x=0 gray) or (x=1 color); (y=0 plot) or (y=1 no plot)
    picture=open(file)
    if x==0:
        print(array_gray_pixels(picture))
        if y==0:
            plot_gray(file)
        elif y!=1 :
            print('WARNING! y must be 0 or 1 ')
    elif x==1:
        print(array_coloured_pixels(picture))
        if y==0:
            plot_color(file)
        elif y!=1 :
            print('WARNING! y must be 0 or 1 ')
    else:
        print('WARNING! x and y must be 0 or 1 ')





