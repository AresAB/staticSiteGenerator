import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_props(self):
        node = ParentNode("div", [], {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'class="greeting" href="https://boot.dev"')

    def test_ineq(self):
        leafNode = LeafNode("p", "This is a Leaf node")
        leafNode2 = LeafNode("a", "This is a Leaf node")
        leafNode3 = LeafNode("a", "This is a Leaf node", {"href": "https://ligma.bll"})
        leafNode4 = LeafNode("a", "This is a Leaf node", {"href": "http://slugma.bll"})
        node = ParentNode("p", [leafNode])
        node2 = ParentNode("p", [leafNode], {"href": "https://ligma.bll"})
        node3 = ParentNode("p", [leafNode, leafNode])
        node4 = ParentNode("a", [leafNode, leafNode])
        node5 = ParentNode("a", [leafNode, leafNode2])
        node6 = ParentNode("a", [leafNode, leafNode2, node])
        node7 = ParentNode("a", [leafNode, leafNode2, node, node])
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node6, node7)

    def test_to_html(self):
        leafNode1 = LeafNode("a", "This is a Leaf node")
        leafNode2 = LeafNode("a", "This is a Leaf node", {"href": "https://ligma.bll"})
        leafNode3 = LeafNode("a", "This is a Leaf node", {"href": "https://ligma.bll", "href2": "http://slugma.bll"})
        node = ParentNode("p", [leafNode1, leafNode2])
        node2 = ParentNode("p", [node, leafNode3], {"href": "https://gulpin.dyz"})
        node3 = ParentNode("p", [node2, node, leafNode3], {"href": "https://dragma.bll"})
        node4 = ParentNode(None, [leafNode1])
        node5 = ParentNode("p", None)
        self.assertEqual(node.to_html(), "<p><a>This is a Leaf node</a><a href=\"https://ligma.bll\">This is a Leaf node</a></p>")
        self.assertEqual(node2.to_html(), "<p href=\"https://gulpin.dyz\"><p><a>This is a Leaf node</a><a href=\"https://ligma.bll\">This is a Leaf node</a></p><a href=\"https://ligma.bll\" href2=\"http://slugma.bll\">This is a Leaf node</a></p>")
        self.assertEqual(node3.to_html(), "<p href=\"https://dragma.bll\"><p href=\"https://gulpin.dyz\"><p><a>This is a Leaf node</a><a href=\"https://ligma.bll\">This is a Leaf node</a></p><a href=\"https://ligma.bll\" href2=\"http://slugma.bll\">This is a Leaf node</a></p><p><a>This is a Leaf node</a><a href=\"https://ligma.bll\">This is a Leaf node</a></p><a href=\"https://ligma.bll\" href2=\"http://slugma.bll\">This is a Leaf node</a></p>")
        self.assertRaises(ValueError, node4.to_html)
        self.assertRaises(ValueError, node5.to_html)


if __name__ == "__main__":
    unittest.main()
