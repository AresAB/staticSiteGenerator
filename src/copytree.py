import os
import shutil

def cp_dir(origin_path, new_path):
	if os.path.exists(origin_path) == False: raise Exception(f"path \'{origin_path}\' is either not an existing path or requires higher permissions")
	if os.path.exists(new_path) == False: os.mkdir(new_path)
	contents = os.listdir(origin_path)
	for item in contents:
		item_path = os.path.join(origin_path, item)
		if os.path.isfile(item_path):
			shutil.copy(item_path, new_path)
		else:
			subdir_path = os.path.join(new_path, item)
			os.mkdir(subdir_path)
			cp_dir(item_path, subdir_path)