"""
Tis is a dataset for imbalanced classification of welding defects.

The dataset can be downloaded from : https://www.kaggle.com/danielbacioiu/tig-aluminium-5083 

"""
import os
import json
import shutil

# path of the original dataset
main_dir = 'welding-defect/al5083'

# path of the new pre-processed dataset
data_dir = 'welding_defect_products'

# if path of the new data folder does not exist, create folder
if not os.path.exists(data_dir):
	os.mkdir(data_dir)

# list of splits of data present
data_splits = ['train', 'test']

# iterating through the data split folders
for split in data_splits:

	# read the annotations file
	f = open(os.path.join(main_dir, split, split+'.json'), 'r' )
	data = json.load(f)
	f.close()

	# list of the unique categories of defects
	categories = list(set(data.values()))

	# creating category folders if they dont exist.
	for category in categories:
		if not os.path.exists( os.path.join(data_dir, 'Class_'+str(category)) ):
			os.mkdir(os.path.join(data_dir, 'Class_'+str(category)) )

	# list of the object folders in the data split
	folders = [i for i in os.listdir( os.path.join(main_dir, split)) if '.' not in i]
	
	# list of file names in the data split.
	files = [os.path.join(folder, img) for folder in folders 
									   for img in os.listdir( os.path.join(main_dir, split, folder))]	

	# iterating through all the images
	for file in files:

		# class name from  the annotations
		class_name = 'Class_' + str(data[file])

		# destination image name
		image_name = file.split('/')[0] + '_' + file.split('/')[1]

		source_image = os.path.join(main_dir, split, file)

		destination_image = os.path.join(data_dir, class_name, image_name )

		# copying the image from source to 
		if not os.path.exists(destination_image):
			shutil.copy(source_image, destination_image)