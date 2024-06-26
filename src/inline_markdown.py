# a module with the findall function, which returns a list of text matching given regex/text
import re

from textnode import TextNode, text_type_text, text_type_image, text_type_link, text_type_bold, text_type_code, text_type_italic

# a delimiter appears to be the seperators in a sense. 
# Ex: split_nodes_delimiter([TextNode("This is a text with a `code block` word", "text")], "`", "code")
# --> [TextNode("This is a text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text")]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	result = []
	for node in old_nodes:
		if node.text_type != text_type_text:
			result.append(node)
			continue
		split_node = node.text.split(delimiter)
		if len(split_node) % 2 == 0:
			raise Exception(f"Invalid markdown: Uneven amount of delimiters in {node}")
		new_nodes = []
		for i in range(0, len(split_node)):
			if i % 2 == 0 and split_node[i] != "":
				new_nodes.append(TextNode(split_node[i], text_type_text))
			elif split_node[i] != "":
				new_nodes.append(TextNode(split_node[i], text_type))
		result.extend(new_nodes)
	return result

def extract_markdown_images(text):
	return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
	return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
	result = []
	for node in old_nodes:
		image_tuples = extract_markdown_images(node.text)
		if node.text_type != text_type_text or image_tuples == []:
			result.append(node)
			continue
		new_nodes = []
		current_text = node.text
		for image_tuple in image_tuples:
			text_list = current_text.split(f"![{image_tuple[0]}]({image_tuple[1]})", 1)
			current_text = text_list[1]
			if text_list[0] != "":
				new_nodes.append(TextNode(text_list[0], text_type_text))
			if image_tuple[0] != "":
				new_nodes.append(TextNode(image_tuple[0], text_type_image, image_tuple[1]))
		if current_text != "":
			new_nodes.append(TextNode(current_text, text_type_text))
		result.extend(new_nodes)
	return result

def split_nodes_link(old_nodes):
	result = []
	for node in old_nodes:
		link_tuples = extract_markdown_links(node.text)
		if node.text_type != text_type_text or link_tuples == []:
			result.append(node)
			continue
		new_nodes = []
		current_text = node.text
		for link_tuple in link_tuples:
			text_list = current_text.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
			current_text = text_list[1]
			if text_list[0] != "":
				new_nodes.append(TextNode(text_list[0], text_type_text))
			if link_tuple[0] != "":
				new_nodes.append(TextNode(link_tuple[0], text_type_link, link_tuple[1]))
		if current_text != "":
			new_nodes.append(TextNode(current_text, text_type_text))
		result.extend(new_nodes)
	return result

def text_to_textnodes(text):
	result = split_nodes_image([TextNode(text, text_type_text)])
	result = split_nodes_link(result)
	result = split_nodes_delimiter(result, "**", text_type_bold)
	result = split_nodes_delimiter(result, "*", text_type_italic)
	result = split_nodes_delimiter(result, "`", text_type_code)
	return result