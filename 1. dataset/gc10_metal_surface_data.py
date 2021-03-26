import os
import shutil
import random
from tqdm import tqdm
import numpy as np

dataset = 'archive/images/images'

new_dataset = 'gc10_metal_defect_dataset'

if not os.path.exists(new_dataset):
	os.mkdir(new_dataset)

if not os.path.exists(os.path.join(new_dataset, 'train')):
	os.mkdir(os.path.join(new_dataset, 'train'))

if not os.path.exists(os.path.join(new_dataset, 'test')):
	os.mkdir(os.path.join(new_dataset, 'test'))

lengths = []

for category in os.listdir(dataset):

	lengths.append(len(os.listdir(os.path.join(dataset, category))))

cutoff = int(np.median(lengths))

for category in os.listdir(dataset):

	print("*********", category, "*********")

	files = os.listdir(os.path.join(dataset, category))

	train_dir = os.path.join(new_dataset, 'train', category)
	test_dir = os.path.join(new_dataset, 'test', category)

	if not os.path.exists(train_dir):
		os.mkdir(train_dir)

	if not os.path.exists(test_dir):
		os.mkdir(test_dir)

	for i in range(2):
		random.shuffle(files)

	if len(files) >= cutoff:
		train_files = files[:cutoff]
		test_files = files[cutoff:]

	else:

		train_len = int(0.9 * len(files))
		train_files = files[:train_len]
		test_files = files[train_len:]

	print("Train data..")

	for file in tqdm(train_files):

		source = os.path.join(dataset, category, file)
		destination = os.path.join(train_dir, file)

		shutil.copyfile(source, destination)

	print("Test data..")

	for file in tqdm(test_files):

		source = os.path.join(dataset, category, file)
		destination = os.path.join(test_dir, file)

		shutil.copyfile(source, destination)


