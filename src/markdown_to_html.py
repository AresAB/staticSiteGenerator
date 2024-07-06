import os

from block_markdown import markdown_to_htmlnode

def extract_heading(markdown):
    block = markdown.lstrip(" \n")
    if block[:2] != "# ": raise Exception("Invalid Markdown: Markdown input doesn't start with a h1")
    return block.split("\n\n", 1)[0][2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f: from_text = f.read()
    with open(template_path) as f: template_text = f.read()
    raw_html_title = extract_heading(from_text)
    raw_html = markdown_to_htmlnode(from_text).to_html()
    html_page = template_text.replace(r"{{ Title }}", raw_html_title).replace(r"{{ Content }}", raw_html)

    dest_path_split = dest_path.split("/")
    dest_path_dir = "/".join(dest_path_split[:-1])

    if os.path.isdir(dest_path_dir) == False: os.makedirs(dest_path_dir)
    with open(dest_path, "w") as f: f.write(html_page)
    print(f"All complete, file '{dest_path}' created")

def generate_page_recursive(from_dir_path, template_path, dest_dir_path):
    if os.path.exists(from_dir_path) == False: raise Exception(f"path \'{from_dir_path}\' is either not an existing path or requires higher permissions")
    if os.path.exists(dest_dir_path) == False: os.mkdir(dest_dir_path)
    from_paths = os.listdir(from_dir_path)
    for item in from_paths:
        from_item_path = os.path.join(from_dir_path, item)
        if os.path.isfile(from_item_path):
            dest_item = item.split(".")
            dest_item[-1] = "html"
            dest_item = ".".join(dest_item)
            dest_item_path = os.path.join(dest_dir_path, dest_item)
            generate_page(from_item_path, template_path, dest_item_path)
        else:
            dest_item_path = os.path.join(dest_dir_path, item)
            generate_page_recursive(from_item_path, template_path, dest_item_path)
