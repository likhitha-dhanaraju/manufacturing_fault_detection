"""
DeepPCB: a dataset contains 1,500 image pairs, 
each of which consists of a defect-free template image
and an aligned tested image with annotations including 
positions of 6 most common types of PCB defects: 

open, short, mousebite, spur, pin hole and spurious copper.

"""

import os
import shutil
from tqdm import tqdm

# path of the original dataset
main_dir = 'DeepPCB/PCBData'

# folder name of the pre-processed dataset directory
data_dir = 'pcb_defect_products'

# if path does not exists, create folder
if not os.path.exists(data_dir):
	os.mkdir(data_dir)

# list of the product names 
objects = [i for i in os.listdir(main_dir) if '.' not in i]

print("Iterating through the products...")
# iterating through the products
for obj in tqdm(objects):

	# full path of the product name
	obj_path = os.path.join(main_dir, obj)

	folders = os.listdir(obj_path)

	# directory containing the images
	images_dir = [os.path.join(obj_path, i) for i in folders if '_' not in i][0]
	
	# directory containing the annotations
	annotations_dir = [os.path.join(obj_path, i) for i in folders if '_' in i][0]

	# list of the damaged pcb images
	damaged_images = [i for i in os.listdir(images_dir) if 'test' in i]
	
	# list of the undamaged pcb images
	undamaged_images = [i for i in os.listdir(images_dir) if 'temp' in i]

	# copying all the undamaged images

	for image in undamaged_images:

		img_name = image.replace('temp', 'proper')
		
		source_image = os.path.join(images_dir, image)

		destination_image = os.path.join(data_dir, img_name)

		shutil.copy(source_image, destination_image)


	# copying all the damaged products images with annotations

	for image in damaged_images:

		# name of the image
		img_name = image.replace('_test', '')

		# name of the annotation file
		ann_name = img_name.replace('.jpg', '.txt')

		source_image = os.path.join( images_dir, image )

		destination_image = os.path.join( data_dir, img_name )

		# copying the image
		shutil.copy(source_image, destination_image)


		source_ann = os.path.join( annotations_dir, ann_name)

		destination_ann = os.path.join(data_dir, ann_name)

		# copying the annotation file
		shutil.copy(source_ann, destination_ann)


