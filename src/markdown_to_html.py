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