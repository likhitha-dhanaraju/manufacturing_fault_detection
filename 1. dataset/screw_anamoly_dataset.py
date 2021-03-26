import os
import shutil
from tqdm import tqdm
import pandas as pd
import random

image_dir = 'archive/train'
csv_file = 'archive/train.csv'

dataset = pd.read_csv(csv_file)

destination = 'screw_anamoly_dataset'

if not os.path.exists(destination):
	os.mkdir(destination)

if not os.path.exists(destination + '/train'):
	os.mkdir(destination + '/train')

if not os.path.exists(destination +'/test'):
	os.mkdir(destination +'/test')

positive_images = []
negative_images = []

for i in range(len(dataset)):

	label = dataset.iloc[i]['anomaly']

	if label == 1:

		positive_images.append(dataset.iloc[i]['filename'])

	else:

		negative_images.append(dataset.iloc[i]['filename'])

train_pos_len = int(0.9 * len(positive_images))
train_neg_len = int(0.9 * len(negative_images))

train_positive_images = positive_images[:train_pos_len]
test_positive_images = positive_images[train_pos_len:]

train_negative_images = negative_images[:train_neg_len]
test_negative_images = negative_images[train_neg_len:]


def copy_images(image_dir, destination, split, category, images_list):

	category_path = os.path.join(destination, split, category)

	if not os.path.exists(category_path):

		os.mkdir(category_path)

	for image in tqdm(images_list):

		source = os.path.join(image_dir, image)
		destination = os.path.join(category_path, image)

		shutil.copyfile(source, destination)


copy_images(image_dir, destination, 'train', 'anamoly', train_positive_images)

copy_images(image_dir, destination, 'train', 'good', train_negative_images)

copy_images(image_dir, destination, 'test', 'anamoly', test_positive_images)

copy_images(image_dir, destination, 'test', 'good', test_negative_images)
