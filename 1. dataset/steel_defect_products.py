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

		categories = [os.path.join(data_dir, "Class_"+str(i)) for i in list(set(data['ClassId']))]

		for category in categories:
			if not os.path.exists(category):
				os.mkdir(category)

		for i in tqdm(range(len(data))):

			image_name = data['ImageId'][i]
			class_name = 'Class_'+ str(data['ClassId'][i])

			source_image = os.path.join(images_dir, image_name)
			destination_image = os.path.join(data_dir, class_name, image_name)

			if not os.path.exists(destination_image):
				shutil.copy(source_image, destination_image)


extract_data(cls=True)