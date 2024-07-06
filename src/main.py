import os
import shutil
from copytree import cp_dir
from markdown_to_html import generate_page_recursive

cp_origin_path = "./static"
cp_new_path = "./public"
gp_origin_path = "./content"
gp_template_path = "./template.html"
gp_new_path = "./public"

def main():
	if os.path.exists(cp_new_path) and os.path.exists(cp_origin_path): shutil.rmtree(cp_new_path)
	cp_dir(cp_origin_path, cp_new_path)
	generate_page_recursive(gp_origin_path, gp_template_path, gp_new_path)

main()