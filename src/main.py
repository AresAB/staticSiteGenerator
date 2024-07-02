import os
import shutil
from copytree import cp_dir

o_path = os.path.expanduser("~/workspace/github.com/AresAB/staticSiteGenerator/src")
n_path = os.path.expanduser("~/workspace/github.com/AresAB/staticSiteGenerator/new_deleteme")

def main():
	if os.path.exists(n_path) and os.path.exists(o_path): shutil.rmtree()
	cp_dir(o_path, n_path)

main()