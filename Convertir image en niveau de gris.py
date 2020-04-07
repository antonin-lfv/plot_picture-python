import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from PIL.Image import *

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

""" le chemin des fichiers """

file1 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image1-ConvertImage.png'
image1 = open(file1)

file2 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image2-ConvertImage.png'
image2 = open(file2)

file3 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image3-ConvertImage.png'
image3 = open(file3)

file4 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image4-ConvertImage.png'
image4 = open(file4)

file5 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image5-ConvertImage.png'
image5 = open(file5)

file6 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image6-ConvertImage.png'
image6 = open(file6)

file7 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image7-ConvertImage.png'
image7 = open(file7)

file8 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image8-ConvertImage.png'
image8 = open(file8)

file9 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image9-ConvertImage.png'
image9 = open(file9)

file10 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image10-ConvertImage.png'
image10 = open(file10)

file11 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image11-ConvertImage.png'
image11 = open(file11)

file12 = '/Users/antoninlefevre/Downloads/langages informatiques/Intelligence artificielle/Traitement image python/IA reconnaissance de chiffres 1/image 1 png compressées/train/image12-ConvertImage.png'
image12 = open(file12)



"""afficher l'image en gris"""



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


#on calcule la taille de l'image

def largeur_hauteur(image):
    return(image.size)

#mise au gris du pixel à la position x,y de image
def mise_au_gris_pixel(x,y,image):
    s = 0.21*image.getpixel((x,y))[0]+0.71*image.getpixel((x,y))[1]+0.07*image.getpixel((x,y))[2]
    return(s/3)

#valeur des pixels
def tableau_pixels_gris(image): 
    l=[]
    (largeur,hauteur)=largeur_hauteur(image)
    for x in range(hauteur):
        for y in range(largeur):
            l.append((mise_au_gris(y,x,image)))
    return(l)

def tableau_pixels(image):
    l=[]
    (largeur,hauteur)=largeur_hauteur(image)
    for x in range(hauteur):
        for y in range(largeur):
            l.append((image.getpixel((y,x))))
    return(l)

def pixels(x,y,file): #(x=0 gray) or (x=1 color); (y=0 plot) or (y=1 no plot)
    image=open(file)
    if x==0:
        print(tableau_pixels_gris(image))
        if y==0:
            plot_gray(file)
        elif y!=1 :
            print('WARNING! y must be 0 or 1 ')
    elif x==1:
        print(tableau_pixels(image))
        if y==0:
            plot_color(file)
        elif y!=1 :
            print('WARNING! y must be 0 or 1 ')
    else:
        print('WARNING! x and y must be 0 or 1 ')
        

""" base de données """





