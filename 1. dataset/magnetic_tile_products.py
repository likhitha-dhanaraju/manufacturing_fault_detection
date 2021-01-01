import os
import shutil

main_dir = 'Magnetic-Tile-Defect'

data_dir = 'magnetic_tile_products'

if not os.path.exists(data_dir):
	os.mkdir(data_dir)

categories = [i for i in os.listdir(main_dir) if '.' not in i]

for category in categories:

	if not os.path.exists( os.path.join( data_dir, category) ):
		os.mkdir(os.path.join(data_dir, category))

for category in categories:

	category_path = os.path.join(main_dir, category, 'Imgs')

	files = os.listdir(category_path)

	for file in files:

		source_path = os.path.join(category_path, file)

		destination_path = os.path.join( data_dir, category, file )

		if not os.path.exists(destination_path):
			shutil.copy(source_path, destination_path )