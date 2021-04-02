import os
import shutil
import random
from tqdm import tqdm

folder = os.path.join(os.getcwd(), 'casting_products')

####### 
#### ABOUT ####

# The dataset contains front view images of the finished casting products.
# It is a classification problem.

# There are two folders in the casting_products folder

# def_front - contains the defective fron view of the images
# ok_front - contains the non-defective front view of the iamges

## casting_512x512 - contains the images in the size 512x512
# contains 781 defective images and 519 non-defective images

## casting_data - contains the images in the size 300x300 

# divided to train and test data. The split ratio is 0.1
# train data contains 3758 defective images and 2875 non-defective images
# test data contains 453 defective images and 262 non-defective images

#######



def casting_preprocessing(split_ratio, img_split):

	if img_split == '512x512':


		casting_datapath = os.path.join(folder, 'casting_512x512', 'casting_512x512')

		# creating folders for the pre-processed 
		new_datapath = 'casting_dataset'

		if not os.path.exists(new_datapath):
			os.mkdir(new_datapath)

		train_path = os.path.join(new_datapath, 'train')
		test_path = os.path.join(new_datapath, 'test')

		if not os.path.exists(train_path):
			os.mkdir(train_path)

		if not os.path.exists(test_path):
			os.mkdir(test_path)


		# paths of the folders containing the defective and non-defective parts
		defective_file_paths =  os.path.join(casting_datapath, 'def_front')
			
		non_defective_file_paths = os.path.join(casting_datapath, 'ok_front')

		# listing out the files
		defective_files = [ os.path.join(defective_file_paths, _file_) for _file_ in os.listdir(defective_file_paths)]

		non_defective_files = [ os.path.join(non_defective_file_paths, _file_) for _file_ in os.listdir(non_defective_file_paths)]

		# splitting the dataset
		train_defective_files = defective_files[ : int(split_ratio * len(defective_files))]
		test_defective_files = defective_files[ int(split_ratio * len(defective_files)) : ]

		train_non_defective_files = non_defective_files[ : int(split_ratio * len(non_defective_files))]
		test_non_defective_files = non_defective_files[ int(split_ratio * len(non_defective_files)) : ]

		train_defective_path = os.path.join(train_path, 'def_front')

		if not os.path.exists(train_defective_path):
			os.mkdir(train_defective_path)

		train_non_defective_path = os.path.join(train_path, 'ok_front')

		if not os.path.exists(train_non_defective_path):
			os.mkdir(train_non_defective_path)

		test_defective_path = os.path.join(test_path, 'def_front')

		if not os.path.exists(test_defective_path):
			os.mkdir(test_defective_path)

		test_non_defective_path = os.path.join(test_path, 'ok_front')

		if not os.path.exists(test_non_defective_path):
			os.mkdir(test_non_defective_path)

		# copy images
		def preprocessing_imgs(final_path, files):

			for img in tqdm(files):

				img_name = img.split('/')[-1]
				shutil.copy(img, os.path.join(final_path, img_name))


		preprocessing_imgs(train_defective_path, train_defective_files)
		preprocessing_imgs(train_non_defective_path, train_non_defective_files)

		preprocessing_imgs(test_defective_path, test_defective_files)
		preprocessing_imgs(test_non_defective_path, test_non_defective_files)

		##############################



	if img_split == '300x300':


		################

		casting_datapath = os.path.join(folder, 'casting_data', 'casting_data')

		# creating folders for the pre-processed 
		new_datapath = 'casting_dataset'

		if not os.path.exists(new_datapath):
			os.mkdir(new_datapath)

		train_path = os.path.join(new_datapath, 'train')
		test_path = os.path.join(new_datapath, 'test')

		if not os.path.exists(train_path):
			os.mkdir(train_path)

		if not os.path.exists(test_path):
			os.mkdir(test_path)

		# paths of the folders containing the defective and non-defective parts
		defective_file_paths = [  
								os.path.join(casting_datapath, 'train', 'def_front'),
								os.path.join(casting_datapath, 'test', 'def_front')
								]
		non_defective_file_paths = [  
								os.path.join(casting_datapath, 'train', 'ok_front'),
								os.path.join(casting_datapath, 'test', 'ok_front')
								]

		# listing out the files
		defective_files = [ os.path.join(folder, _file_) for folder in defective_file_paths for _file_ in os.listdir(folder)]

		non_defective_files = [ os.path.join(folder, _file_) for folder in non_defective_file_paths for _file_ in os.listdir(folder)]

		# splitting the dataset
		train_defective_files = defective_files[ int(split_ratio * len(defective_files)) : ]
		test_defective_files = defective_files[ : int(split_ratio * len(defective_files)) ]

		train_non_defective_files = non_defective_files[ : int(split_ratio * len(non_defective_files))]
		test_non_defective_files = non_defective_files[ int(split_ratio * len(non_defective_files)) : ]

		train_defective_path = os.path.join(train_path, 'def_front')

		if not os.path.exists(train_defective_path):
			os.mkdir(train_defective_path)

		train_non_defective_path = os.path.join(train_path, 'ok_front')

		if not os.path.exists(train_non_defective_path):
			os.mkdir(train_non_defective_path)

		test_defective_path = os.path.join(test_path, 'def_front')

		if not os.path.exists(test_defective_path):
			os.mkdir(test_defective_path)

		test_non_defective_path = os.path.join(test_path, 'ok_front')

		if not os.path.exists(test_non_defective_path):
			os.mkdir(test_non_defective_path)

		# copy images
		def preprocessing_imgs(final_path, files):

			for img in tqdm(files):

				img_name = img.split('/')[-1]
				shutil.copy(img, os.path.join(final_path, img_name))


		print("\n\n Pre-processing train defective data \n")
		preprocessing_imgs(train_defective_path, train_defective_files)

		print("\n\n Pre-processing train non-defective data \n")
		preprocessing_imgs(train_non_defective_path, train_non_defective_files)

		print("\n\n Pre-processing test defective data \n")
		preprocessing_imgs(test_defective_path, test_defective_files)

		print("\n\n Pre-processing test non-defective data \n")
		preprocessing_imgs(test_non_defective_path, test_non_defective_files)


casting_preprocessing(split_ratio=0.1, img_split='300x300')