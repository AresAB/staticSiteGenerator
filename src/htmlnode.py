# html representation of inline text
# the props var is a dictionary representation of html attributes, ex: {"href": "https://www.ligma.bls"}
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def props_to_html(self):
		result = ""
		for key in self.props:
			result += f"{key}=\"{self.props[key]}\" "
		return result.rstrip()

	def __repr__(self):
		print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

# LeafNodes are industry standard, and are just HTMLNodes that have one tag and no children
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value == None:
			raise ValueError("Invalid HTML: no value")
		if self.tag != None:
			if self.props != None:
				return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
			return f"<{self.tag}>{self.value}</{self.tag}>"
		return self.value
	
class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)
	
	def to_html(self):
		if self.tag == None: raise ValueError("Invalid HTML: no tag")
		if self.children == None: raise ValueError("Invalid HTML: no children")
		
		result = f"<{self.tag}"
		if self.props != None: result += f" {super().props_to_html()}"
		result += ">"
		for node in self.children:
			result += node.to_html()
		return f"{result}</{self.tag}>"