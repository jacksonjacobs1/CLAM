#%%
import random
import tables
import sys

import torch
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw

seed = random.randrange(sys.maxsize) #get a random seed so that we can reproducibly do the cross validation setup
random.seed(seed) # set the seed
print(f"random seed (note down for reproducibility): {seed}")

# meta params
dataname = ''
data_size = 100 # number of total slides produced
classes = [0,1]
wsi_size = [4000,4000]
background_color = (255,255,255)

# slide params
diameter_min=5
diameter_max=10
max_tumors=3
max_tumor_diameter=100
min_tumor_diameter=50
tissue_density=0.5


#%%
img_dtype = tables.UInt8Atom() # dtype in which the images will be saved
storage = {}
block_shape = np.array((wsi_size[0], wsi_size[1], 3)) # indicates what will be saved into pytable array
filters=tables.Filters(complevel=6, complib='zlib') #we can also specify filters, such as compression, to improve storage speed

total=0
hdf5_file = tables.open_file(f"./{dataname}.pytable", mode='w') #open the respective pytable

storage['imgs'] = hdf5_file.create_earray(hdf5_file.root, "imgs", img_dtype,  
										shape=np.append([0],block_shape), 
										chunkshape=np.append([1],block_shape),
										filters=filters)

storage['labels'] = hdf5_file.create_earray(hdf5_file.root, "labels", img_dtype,  
											shape=[0], 
											chunkshape=[1],
											filters=filters)


#%% generate single image to test
img = Image.new(mode='RGB', size=(wsi_size[0], wsi_size[1]), color='white')
draw = ImageDraw.Draw(img)

for i in range():
    d = np.random.randint(diameter_min, diameter_max)
    squeeze_constant = np.random.randint(-d/2, d/2)
    ul=np.random
plt.imshow(img)


# %% WSI generation loop
for filei in range(data_size):
    print(filei)
    img = Image.new('rgb', (wsi_size[0], wsi_size[1]), color='white')
    draw = ImageDraw.Draw(img)

    # draw benign objects on image
    for i in range():
        