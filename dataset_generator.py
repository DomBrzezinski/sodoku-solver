import matplotlib.pyplot as plt
import numpy as np
import pickle
from os import listdir
from os.path import join, isfile
from PIL import Image
import cv2
import csv


global coords
coords = []

path = r".\\dataset\images"
image_paths = []
for filename in listdir(path):  # iterates over all the files in 'path'
    full_path = join(path, filename)  # joins the path with the filename
    if isfile(full_path):  # validate that it is a file
        image_paths.append(full_path)  # appends the full path to the list


def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    ix, iy = event.xdata, event.ydata
    coords.append([ix, iy])

    if len(coords) == 4:
        fig.canvas.mpl_disconnect(cid)
        plt.close()
    return coords



with open('dataset\index.csv', mode='w', newline='') as dataset:
    writer = csv.writer(dataset)#, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for full_path in image_paths:

        img = Image.open(full_path)

        img_array = np.asarray(img)
        grayscale = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        image = grayscale
        image = image/255
        # images.append([image, grayscale])


        coords = []
        print(grayscale.shape)
        fig, ax = plt.subplots()
        ax.imshow(grayscale, cmap='gray')
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        plt.show()
        writer.writerow([full_path] + coords)



