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
import os
from sklearn.model_selection import train_test_split


destination_folder = 'solar_panels_products'

if not os.path.exists(destination_folder):
	os.mkdir(destination_folder)


# datafolder is the relative path for the contents in the elpv dataset

images, _, types = load_dataset(datafolder = 'elpv_dataset')

train_images, test_images, train_types, test_types = train_test_split(images, types, test_size= 0.1)


def create_dataset(images, types, split):

	data_folder = os.path.join(destination_folder, split)

	if not os.path.exists(data_folder):
		os.mkdir(data_folder)

	idx = 0

	for image ,type_ in zip(images, types):


		image = cv2.resize(image, (300, 300)).reshape(300,300,1)

		category_folder = os.path.join(data_folder, type_)

		if not os.path.exists(category_folder):
			os.mkdir(category_folder)

		image_name = os.path.join( category_folder, 'elpv_' + str(idx) + '.jpg')


		if not os.path.exists(image_name):

			cv2.imwrite(image_name, image )

		idx += 1
		

create_dataset(train_images, train_types, "train")
create_dataset(test_images, test_types, "test")

