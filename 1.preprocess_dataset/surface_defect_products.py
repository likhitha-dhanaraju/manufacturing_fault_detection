"""
ABOUT THE DATASET:
 
In the Northeastern University (NEU) surface defect database, 
six kinds of typical surface defects of the hot-rolled steel strip 
are collected, i.e., 
rolled-in scale (RS), 
patches (Pa), 
crazing (Cr),
pitted surface (PS), 
inclusion (In)
scratches (Sc). 

The database includes 1,800 grayscale images: 300 samples 
of size 200x200 each of six different kinds of typical surface defects.

NEU-CLS.rar : contains the defects from the above 
six categories, wih 300 images each. Can be used
for classification purpose

NEU-CLAS-64.zip : contains the mixed defects as well.
Thus contain 9 categories.Can be used for classification 
purposes.

NEU-DET : contains the defects from the above 
six categories, wih 300 images each with bounding box 
annotations given around the defect region. Can be used for 
detection purposes.


The final dataset structure:

- surface_det_dataset
	- rs
		- rs_1.jpg
		- rs_1.txt
		- rs_2.jpg
		- rs_2.txt
	- ca
		- ca_1.jpg
		- ca_1.txt
		- ca_2.jpg
		- ca_2.txt

Annotations file - ".txt" is of the format - 
xmin, ymin, xmax, ymax

"""

import os
import shutil
from lxml import etree
from tqdm import tqdm


def create_data(files, folder, datapath, source_path):

	# full path of the destination folder
	destination_path = os.path.join(datapath, folder)

	# if the destination category folder does not exists, create a new folder
	if not os.path.exists(destination_path):
		os.mkdir(destination_path)

	# iterating through the files in the category folder.
	for _file_ in tqdm(files):

		# full path of the source image file
		source = os.path.join( source_path, _file_ )

		# full path of the destination image file
		destination = os.path.join( destination_path, _file_ )

		if not os.path.exists(destination):
			# copying the image to the pre-processed dataset folder
			shutil.copy(source, destination)
	


def extract_data(cls=False, det=False):
	"""
	function to extract dataset for
	object detection (det) or classification (cls) purpose.

	cls : boolean
		Set True for classification purpose

	det : boolean
		Set True for object detection purpose

	""" 

	if cls and det:
		# raising error if arguments show both classification and detection
		raise ValueError("Choose either Classification or Object Detection")

	# if classification dataset pre-processing is required.
	if cls:

		# the folder names and the categories of the defects in the classification dataset
		folders = [ 'rs' , 'pa' , 'cr' , 'ps' , 'in' , 'sc']

		path = 'NEU-CLS-64'

		# path of the pre-processed dataset to be created.
		datapath = 'surface_cls_dataset'

		# if the path does not exist,creating the new data folder.
		if not os.path.exists(datapath):
			os.mkdir(datapath)

		train_datapath = os.path.join(datapath, 'train')

		if not os.path.exists(train_datapath):
			os.mkdir(train_datapath)

		test_datapath = os.path.join(datapath, 'test')
		
		if not os.path.exists(test_datapath):
			os.mkdir(test_datapath)

		# iterating through all the category folders.
		for folder in sorted(folders):


			# full path of the source folder
			source_path = os.path.join(path, folder)

			files = sorted(os.listdir(source_path))

			train_len = int(0.9 * len(files))

			train_files = files[:train_len]

			test_files = files[train_len:]


			create_data(train_files, folder, train_datapath, source_path)

			create_data(test_files, folder, test_datapath, source_path)

			
	# if object detection dataset needs to be pre-processed.
	if det:

		# the folder names and the categories of the defects in the detection dataset
		folders = [ 'crazing', 'inclusion', 'patches',
						'pitted_surface', 'rolled-in_scale', 'scratches']

		path = 'NEU-DET'

		# path of the pre-processed dataset to be created.
		datapath = 'surface_det_dataset'

		# if the path already exists, overwriting the data.
		if os.path.exists(datapath):
			print( "Dataset already exists, overwriting it!" )

		# if the path does not exist,creating the new data folder.
		if not os.path.exists(datapath):
			os.mkdir(datapath)

		# full path of the images folder
		images_path = os.path.join(path, 'IMAGES')

		# full path of the annotations folder
		annotations_path = os.path.join(path, 'ANNOTATIONS')

		# get the filenames without the file extension.
		raw_files = [i.split('.')[0] for i in os.listdir(images_path)]

		# iterating through the category folders
		for cls_id,folder in enumerate(folders):

			# full path of the category folder
			main_path = os.path.join(datapath, folder)

			# if destination category folder doesn't exits, create new one.
			if not os.path.exists(main_path):
				os.mkdir(main_path)

			# list of the files of the category - folder
			files = [i for i in raw_files if folder in i]

			class_id = str(cls_id)
			for file in files:

				# full path of the annotation file
				ann_path = os.path.join(annotations_path, file+'.xml')

				# parsing xml file to extract bounding box co-ordinates.
				tree = etree.parse(ann_path)
				root = tree.getroot()

				xmin = root.xpath('.//bndbox/xmin')[0].text
				ymin = root.xpath('.//bndbox/ymin')[0].text
				xmax = root.xpath('.//bndbox/xmax')[0].text
				ymax = root.xpath('.//bndbox/ymax')[0].text

				# forming a string of the bounding box
				data = ','.join([xmin, ymin, xmax, ymax, class_id])

				# writing the data to a text file
				f = open(os.path.join(main_path, file+'.txt'), 'w' )
				f.write(data)
				f.close()

				# full path of the source of the image
				source_image = os.path.join( images_path, file+'.jpg' )
				
				# full path of the destination of the image
				destination_image = os.path.join( main_path, file+'.jpg' )

				# copying the image 
				shutil.copy(source_image, destination_image)


extract_data( cls=True )
