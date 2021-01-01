"""
Usage of the Solar PV dataset

1. Download the github repository: https://github.com/zae-bayern/elpv-dataset
2. Extract the zip file elpv-dataset-master.zip
3. Move the contents - doc, images, utils in the same direcotry as this script.
4. Run this file.

"""


from utils.elpv_reader import load_dataset
import cv2
import numpy as np
images, probabilities, types = load_dataset()

categories = ['mono','poly']

data = []
for image,proba,type_ in zip(images, probabilities, types):
	
	image = cv2.resize(image, (300, 300)).reshape( image.shape[0] * image.shape[1])
	proba = np.array([proba])
	type_ = np.array([categories.index(type_)], dtype='float')
	temp = [image, proba, type_]
	data.append( np.array(temp) )

data = np.array(data)

f = open('solar_panels_data.npy','wb')	
np.save(f, data)
f.close()