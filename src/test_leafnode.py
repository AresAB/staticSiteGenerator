import unittest

from htmlnode import HTMLNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_props(self):
        node = LeafNode("div", "Hello, world!", {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'class="greeting" href="https://boot.dev"')

    def test_ineq(self):
        node = LeafNode("p", "This is a Leaf node")
        node2 = LeafNode("a", "This is a Leaf node")
        node3 = LeafNode("a", "This is a Leaf node", {"href": "https://ligma.bll"})
        node4 = LeafNode("a", "This is a Leaf node", {"href": "https://ligma.bll", "href": "http://slugma.bll"})
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)

    def test_to_html(self):
        node = LeafNode("a", "This is a Leaf node")
        node2 = LeafNode("a", "This is a Leaf node link", {"href": "https://ligma.bll"})
        node3 = LeafNode("a", None)
        node4 = LeafNode("a", None, {"href": "https://ligma.bll"})
        self.assertEqual(node.to_html(), "<a>This is a Leaf node</a>")
        self.assertEqual(node2.to_html(), "<a href=\"https://ligma.bll\">This is a Leaf node link</a>")
        self.assertRaises(ValueError, node3.to_html)
        self.assertRaises(ValueError, node4.to_html)


if __name__ == "__main__":
    unittest.main()
