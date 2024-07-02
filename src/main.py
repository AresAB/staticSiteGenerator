import os
import shutil
from copytree import cp_dir

origin_path = os.path.expanduser("~/workspace/github.com/AresAB/staticSiteGenerator/static")
new_path = os.path.expanduser("~/workspace/github.com/AresAB/staticSiteGenerator/public")

def main():
	if os.path.exists(new_path) and os.path.exists(origin_path): shutil.rmtree(new_path)
	cp_dir(origin_path, new_path)

main()