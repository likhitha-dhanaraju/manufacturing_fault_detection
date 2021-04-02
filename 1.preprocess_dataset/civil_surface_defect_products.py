import os
import shutil
import random
from tqdm import tqdm

dataset = 'archive'

new_dataset = 'civil_surface_defect_dataset'

if not os.path.exists(new_dataset):
	os.mkdir(new_dataset)

if not os.path.exists(os.path.join(new_dataset, 'train')):
	os.mkdir(os.path.join(new_dataset, 'train'))

if not os.path.exists(os.path.join(new_dataset, 'test')):
	os.mkdir(os.path.join(new_dataset, 'test'))


limit = 500

for category in os.listdir(dataset):

	
	files = os.listdir(os.path.join(dataset, category))

	train_dir = os.path.join(new_dataset, 'train', category)
	test_dir = os.path.join(new_dataset, 'test', category)

	if not os.path.exists(train_dir):
		os.mkdir(train_dir)

	if not os.path.exists(test_dir):
		os.mkdir(test_dir)

	for i in range(2):
		random.shuffle(files)

	train_files = files[:limit]
	test_files = files[limit:limit + int(0.1*limit)]

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


