from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

# handles inline text (stuff inside of blocks, like bolding, italics, links, etc)
# kinda an inbetween between markdown and html
# __repr__ is just default ToString if you somehow forgot
class TextNode:
	def __init__(self, TEXT, TEXT_TYPE, URL=None):
		self.text = TEXT
		self.text_type = TEXT_TYPE
		self.url = URL

	def __eq__(self, textNode2):
		return self.text == textNode2.text and self.text_type == textNode2.text_type and self.url == textNode2.url

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
	
def textNode_to_HTMLNode(node):
	if node.text_type == text_type_text: return LeafNode(None, node.text)
	if node.text_type == text_type_bold: return LeafNode("b", node.text)
	if node.text_type == text_type_italic: return LeafNode("i", node.text)
	if node.text_type == text_type_code: return LeafNode("code", node.text)
	if node.text_type == text_type_link: return LeafNode("a", node.text, {"href": node.url})
	if node.text_type == text_type_image: return LeafNode("img", "", {"src": node.url, "alt": node.text})
	raise Exception(f"Invalid textNode: No HTML tag equivalent for \'{node.text_type}\'")

def textNodes_to_HTMLNodes(nodes):
	return list(map(lambda x: textNode_to_HTMLNode(x), nodes))