import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
	def test_to_html_props(self):
		node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
		self.assertEqual(node.props_to_html(), 'class="greeting" href="https://boot.dev"')

	def test_ineq(self):
		node = HTMLNode("p", "This is a HTML node")
		node2 = HTMLNode("p", "This is a HTML node", [node])
		node3 = HTMLNode("p", "This is a HTML node", [node], {"href": "https://ligma.bll", "href": "http://slugma.bll"})
		self.assertNotEqual(node, node2)
		self.assertNotEqual(node2, node3)

if __name__ == "__main__":
    unittest.main()
