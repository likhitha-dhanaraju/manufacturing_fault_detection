"""
Usage of the Solar PV dataset

1. Download the github repository: https://github.com/zae-bayern/elpv-dataset
2. Extract the zip file elpv-dataset-master.zip
3. Make sure the utils folder and this script are outside the extracted folder.
4. Run this file.

"""


from utils.elpv_reader import load_dataset
import cv2
import numpy as np
import shutil
from tqdm import tqdm
import os

destination_folder = 'solar_panels_products'

if not os.path.exists(destination_folder):
	os.mkdir(destination_folder)


# datafolder is the relative path for the contents in the elpv dataset

images, _, types = load_dataset(datafolder = 'elpv_dataset')


for (idx, (image ,type_)) in tqdm(enumerate(zip(images, types))):

	image = cv2.resize(image, (300, 300)).reshape( image.shape[0] * image.shape[1])

	category_folder = os.path.join(destination_folder, type_)

	if not os.path.exists(category_folder):
		os.mkdir(category_folder)

	image_name = os.path.join( category_folder, 'elpv_' + str(idx) + '.jpg')

	if not os.path.exists(image_name):

		cv2.imwrite( image_name, image )
	
