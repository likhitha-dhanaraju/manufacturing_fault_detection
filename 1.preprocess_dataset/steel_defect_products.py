"""
You can download the dataset from : https://www.kaggle.com/c/severstal-steel-defect-detection
The given dataset contains the defects on flat steel sheets by Severstal.

The given dataset can be used for Classification and Segmentation models
Can be modified for the object detection purpose

"""
import os
import pandas as pd 
import shutil
from tqdm import tqdm
from collections import Counter
import numpy as np

# directory name of the data
main_dir = 'severstal-steel-defect-detection'

# directory of teh train images
images_dir = os.path.join(main_dir, 'train_images')

# full path of the annotation file
annotation_file = os.path.join(main_dir,'train.csv' )

# reading the annotation file
data = pd.read_csv(annotation_file)


def extract_data(cls=False, seg=False):
	"""
	function to extract data based on the purpose - Classification, Segmentation

	Parameters
	-------------

	cls: boolean
		Set True for getting classification dataset

	seg: boolean
		Set true for getting segmentation dataset
	"""
	
	if cls and seg:
		raise ValueError("Select either classification or segmentation.")

	if cls:

		# directory name of the classification dataset
		data_dir = 'steel_defect_cls_products'

		# yeah 
		if not os.path.exists(data_dir):
			os.mkdir(data_dir)

		all_classes =  ["Class_"+str(i) for i in list(data['ClassId'])]

		categories = set(all_classes)

		categories_count = Counter(all_classes)

		print(categories_count)

		median = int(0.9 * np.median(list(categories_count.values())))

		#median = int(np.median(list(categories_count.values())))

		print("Median:", median)

		train_len = int(0.9 * len(data))

		train_data = data.iloc[:train_len]

		test_data = data.iloc[train_len:]

		train_dir = os.path.join(data_dir, 'train')
		
		if not os.path.exists(train_dir):
			os.mkdir(train_dir)

		for category in categories:

			category_path = os.path.join(train_dir, category)

			if not os.path.exists(category_path):
				os.mkdir(category_path)


		train_counter_check = {key:0 for key in categories}

		for i in tqdm(range(len(train_data))):

			image_name = train_data['ImageId'][i]
			class_name = 'Class_'+ str(train_data['ClassId'][i])
			
			if train_counter_check[class_name] <= median:

				train_counter_check[class_name] += 1

				source_image = os.path.join(images_dir, image_name)
				destination_image = os.path.join(train_dir, class_name, image_name)

				if not os.path.exists(destination_image):
					shutil.copy(source_image, destination_image)

		print(train_counter_check)

		test_dir = os.path.join(data_dir, 'test')
		
		if not os.path.exists(test_dir):
			os.mkdir(test_dir)

		for category in categories:

			category_path = os.path.join(test_dir, category)
			
			if not os.path.exists(category_path):
				os.mkdir(category_path)

		test_counter_check = {key:0 for key in categories}

		for i in tqdm(range(train_len, len(data))):

			image_name = test_data['ImageId'][i]
			class_name = 'Class_'+ str(test_data['ClassId'][i])
		
			if test_counter_check[class_name] <= int(median/10):

				test_counter_check[class_name] += 1

				source_image = os.path.join(images_dir, image_name)
				destination_image = os.path.join(test_dir, class_name, image_name)

				if not os.path.exists(destination_image):
					shutil.copy(source_image, destination_image)

		print(test_counter_check)

extract_data(cls=True)