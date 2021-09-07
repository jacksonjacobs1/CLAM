# %%
import random
import tables
import os
import sys

import torch
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw

<<<<<<< HEAD
# %%
=======
>>>>>>> 244ebd7426895a68d22a3bf95ac240033403166d
seed = random.randrange(sys.maxsize)  # get a random seed so that we can reproducibly do the cross validation setup
random.seed(seed)  # set the seed
print(f"random seed (note down for reproducibility): {seed}")

# meta params
<<<<<<< HEAD
dataname = 'dataset1'
os.mkdir(f"/home/jackson/dp/pearl/datasets/{dataname}")

=======
dataname = ''
>>>>>>> 244ebd7426895a68d22a3bf95ac240033403166d
data_size = 100  # number of total slides produced
classes = [0, 1]
wsi_size = [4000, 4000]
background_color = (255, 255, 255)

# slide params
<<<<<<< HEAD
diameter_min = 15
diameter_max = 25
max_benign_objects = 25000
min_benign_objects = 15000

max_tumors = 5
max_tumor_diameter = 300
min_tumor_diameter = 100


# %%
def draw_random_cell(draw, type, d_min, d_max, x_min, y_min, x_max, y_max):
    d = np.random.randint(d_min, d_max)
    squeeze_constant = np.random.randint(-d / 2, d / 2, 2)  # (x_squeeze, y_squeeze)

    x0 = np.random.randint(x_min, x_max - d_max)
    x1 = x0 + d + squeeze_constant[0]

    y0 = np.random.randint(y_min, y_max - d_max)
    y1 = y0 + d + squeeze_constant[1]

    if type == 'benign':
        variety = np.random.randint(0, 3)
        if variety == 0:  # draw blue circle
            draw.ellipse(list(np.append((x0, y0), (x0 + d, y0 + d))), fill=(0, 0, 255))
        elif variety == 1:  # draw blue ovals
            draw.ellipse(list(np.append((x0, y0), (x1, y1))), fill=(0, 0, 255))
        elif variety == 2:  # draw red circle
            draw.ellipse(list(np.append((x0, y0), (x0 + d, y0 + d))), fill=(255, 0, 0))

    elif type == 'cancerous':
        draw.rectangle(list(np.append((x0, y0), (x1, y1))), fill=(255, 0, 0))
=======
diameter_min = 5
diameter_max = 10
max_tumors = 3
max_benign_objects = 1000
max_tumor_diameter = 100
min_tumor_diameter = 50
tissue_density = 0.5

# %%
img_dtype = tables.UInt8Atom()  # dtype in which the images will be saved
storage = {}
block_shape = np.array((wsi_size[0], wsi_size[1], 3))  # indicates what will be saved into pytable array
filters = tables.Filters(complevel=6,
                         complib='zlib')  # we can also specify filters, such as compression, to improve storage speed

total = 0
hdf5_file = tables.open_file(f"./{dataname}.pytable", mode='w')  # open the respective pytable

storage['imgs'] = hdf5_file.create_earray(hdf5_file.root, "imgs", img_dtype,
                                          shape=np.append([0], block_shape),
                                          chunkshape=np.append([1], block_shape),
                                          filters=filters)
>>>>>>> 244ebd7426895a68d22a3bf95ac240033403166d

storage['labels'] = hdf5_file.create_earray(hdf5_file.root, "labels", img_dtype,
                                            shape=[0],
                                            chunkshape=[1],
                                            filters=filters)

# %% generate single image to test
img = Image.new(mode='RGB', size=(wsi_size[0], wsi_size[1]), color='white')
draw = ImageDraw.Draw(img)

for i in range(np.random.randint(1, high=max_benign_objects)):
    draw_random_cell(draw=draw, type='benign', d_min=diameter_min, d_max=diameter_max,
                     x_min=0, y_min=0, x_max=wsi_size[0], y_max=wsi_size[1])

<<<<<<< HEAD
plt.imshow(img)
plt.show()

=======
>>>>>>> 244ebd7426895a68d22a3bf95ac240033403166d
# %% WSI generation loop
for filei in range(data_size):
    print(filei)
    img = Image.new('RGB', (wsi_size[0], wsi_size[1]), color='white')
    draw = ImageDraw.Draw(img)

<<<<<<< HEAD
    for i in range(np.random.randint(low=min_benign_objects, high=max_benign_objects)):
        draw_random_cell(draw=draw, type='benign', d_min=diameter_min, d_max=diameter_max,
                         x_min=0, y_min=0, x_max=wsi_size[0], y_max=wsi_size[1])

    label = None

    if filei < data_size / 2:
        label = 0
    else:
        label = 1
        for tumor in range(np.random.randint(1, max_tumors + 1)):  # for each tumor
            tumor_diameter = np.random.randint(min_tumor_diameter, max_tumor_diameter)
            tumor_xy = np.random.randint(0, wsi_size[0] - tumor_diameter, 2)

            for i in range(int(tumor_diameter / diameter_max) ** 2):  # draw each cancer cell
                draw_random_cell(draw=draw, type='cancerous', d_min=diameter_min, d_max=diameter_max,
                                 x_min=tumor_xy[0], y_min=tumor_xy[1],
                                 x_max=tumor_xy[0] + tumor_diameter, y_max=tumor_xy[1] + tumor_diameter)

    if filei % 10 == 0:
        plt.imshow(img)
        plt.show()

    filename = f"./datasets/{dataname}/slide_{filei}.tiff"
    img.save(filename, format='TIFF')
=======
    # draw benign objects on image
    for i in range(np.random.randint(1, high=max_benign_objects)):
        d = np.random.randint(diameter_min, diameter_max)
        squeeze_constant = np.random.randint(-d / 2, d / 2)
        ul = np.random.randint(diameter_min, wsi_size[0] - diameter_max, 2)
        point2 = ul + d
        point2[0] = point2[0] + squeeze_constant

        # Three varieties of benign objects
        variety = np.random.randint(0, 3)
        if variety == 0:  # draw blue circle
            draw.ellipse(list(np.append(ul, ul + d)), fill=(0, 0, 255))
        elif variety == 1:  # draw blue ovals
            draw.ellipse(list(np.append(ul, point2)), fill=(0, 0, 255))
        elif variety == 2:  # draw red circle
            draw.ellipse(list(np.append(ul, ul + d)), fill=(255, 0, 0))

    label = None

    if filei < data_size/2:
        label = 0
    else:
        label = 1
        if

>>>>>>> 244ebd7426895a68d22a3bf95ac240033403166d

