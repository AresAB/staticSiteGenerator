import unittest

from textnode import TextNode, textNode_to_HTMLNode
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		node3 = TextNode("This is a text node", "bold", None)
		node4 = TextNode("This is a text node", "italic")
		self.assertEqual(node, node2)
		self.assertEqual(node, node3)
		self.assertEqual(textNode_to_HTMLNode(node), LeafNode("b", "This is a text node"))
		self.assertEqual(textNode_to_HTMLNode(node4), LeafNode("i", "This is a text node"))

	def test_ineq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold", "http://ligma.bll")
		node3 = TextNode("This is another text node", "bold")
		node4 = TextNode("This is a text node", "italic")
		self.assertNotEqual(node, node2)
		self.assertNotEqual(node, node3)
		self.assertNotEqual(node, node4)

if __name__ == "__main__":
    unittest.main()
