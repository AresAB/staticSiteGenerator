import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode

class TestLeafNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node3 = TextNode("This is a `bad markdown text node", "text")
        node4 = TextNode("This is a text node", "bold")
        node5 = TextNode("This is a **bolded text** with some *italic font* and some `code blocks` to go in text node format", "text")
        node6 = TextNode("This is a **bolder text** with **bolder words**", "text")
        self.assertEqual(split_nodes_delimiter([node5], "`", "code"), [TextNode("This is a **bolded text** with some *italic font* and some ", "text"), TextNode("code blocks", "code"), TextNode(" to go in text node format", "text")])
        self.assertEqual(split_nodes_delimiter([node5], "**", "bold"), [TextNode("This is a ", "text"), TextNode("bolded text", "bold"), TextNode(" with some *italic font* and some `code blocks` to go in text node format", "text")])
        self.assertEqual(split_nodes_delimiter([node5], "*", "italic"), [TextNode("This is a ", "text" ), TextNode("bolded text", "text"), TextNode(" with some ", "text"), TextNode("italic font", "italic"), TextNode(" and some `code blocks` to go in text node format", "text")])
        self.assertEqual(split_nodes_delimiter([node5, node6], "**", "bold"), [TextNode("This is a ", "text"), TextNode("bolded text", "bold"), TextNode(" with some *italic font* and some `code blocks` to go in text node format", "text"), TextNode("This is a ", "text"), TextNode("bolder text", "bold"), TextNode(" with ", "text"), TextNode("bolder words", "bold")])
        self.assertEqual(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node5], "`", "code"), "**", "bold"), "*", "italic"), [TextNode("This is a ", "text"), TextNode("bolded text", "bold"), TextNode(" with some ", "text"), TextNode("italic font", "italic"), TextNode(" and some ", "text"), TextNode("code blocks", "code"), TextNode(" to go in text node format", "text")])
        self.assertEqual(split_nodes_delimiter([node4], "*", "italic"), [node4])
        self.assertRaises(Exception, split_nodes_delimiter, [node3], "`", "code")

    def test_extract_markdown_images(self):
        text1 = "This is an ![image](https://ligma.bll)"
        text2 = "This is an ![image](https://ligma.bll) that ![imaged](http://slugma.bll)"
        text3 = "This is the ![picture](https://gulpin.dyz) with an ![image](https://ligma.bll) that ![imaged](http://slugma.bll)"
        text4 = "This is the ![picture](https://gulpin.dyz) with an ![image](https://ligma.bll) that ![imaged](http://slugma.bll) without this [fake image](https://dragma.bll)"
        self.assertEqual(extract_markdown_images(text1), [("image", "https://ligma.bll")])
        self.assertEqual(extract_markdown_images(text2), [("image", "https://ligma.bll"), ("imaged", "http://slugma.bll")])
        self.assertEqual(extract_markdown_images(text3), [("picture", "https://gulpin.dyz"), ("image", "https://ligma.bll"), ("imaged", "http://slugma.bll")])
        self.assertEqual(extract_markdown_images(text3), extract_markdown_images(text4))

    def test_extract_markdown_links(self):
        text1 = "This is a [link](https://ligma.bll)"
        text2 = "This is a [link](https://ligma.bll) that [linked](http://slugma.bll)"
        text3 = "This is the [anchor](https://gulpin.dyz) with a [link](https://ligma.bll) that [linked](http://slugma.bll)"
        text4 = "This is the [anchor](https://gulpin.dyz) with a [link](https://ligma.bll) that [linked](http://slugma.bll) without this [fake link] (https://dragma.bll)"
        self.assertEqual(extract_markdown_links(text1), [("link", "https://ligma.bll")])
        self.assertEqual(extract_markdown_links(text2), [("link", "https://ligma.bll"), ("linked", "http://slugma.bll")])
        self.assertEqual(extract_markdown_links(text3), [("anchor", "https://gulpin.dyz"), ("link", "https://ligma.bll"), ("linked", "http://slugma.bll")])
        self.assertEqual(extract_markdown_links(text3), extract_markdown_links(text4))

    def test_split_nodes_image(self):
        node1 = TextNode("This is an ![image](https://ligma.bll)", "text")
        node2 = TextNode("This is an ![image](https://ligma.bll) that ![imaged](http://slugma.bll)", "text")
        node3 = TextNode("This is an ![image](https://ligma.bll)", "bold")
        node4 = TextNode("This is a text node without an image", "text")
        node5 = TextNode("This is an ![](https://ligma.bll)", "text")
        node6 = TextNode("![image](https://ligma.bll)", "text")
        node7 = TextNode("![image](https://ligma.bll)![imaged](https://slugma.bll)", "text")
        self.assertEqual(split_nodes_image([node1]), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll")])
        self.assertEqual(split_nodes_image([node2]), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("imaged", "image", "http://slugma.bll")])
        self.assertEqual(split_nodes_image([node1, node2]), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("imaged", "image", "http://slugma.bll")])
        self.assertEqual(split_nodes_image([node3]), [node3])
        self.assertEqual(split_nodes_image([node4]), [node4])
        self.assertEqual(split_nodes_image([node5]), [TextNode("This is an ", "text")])
        self.assertEqual(split_nodes_image([node6]), [TextNode("image", "image", "https://ligma.bll")])
        self.assertEqual(split_nodes_image([node7]), [TextNode("image", "image", "https://ligma.bll"), TextNode("imaged", "image", "https://slugma.bll")])

    def test_split_nodes_link(self):
        node1 = TextNode("This is a [link](https://ligma.bll)", "text")
        node2 = TextNode("This is a [link](https://ligma.bll) that [linked](http://slugma.bll)", "text")
        node3 = TextNode("This is a [link](https://ligma.bll)", "bold")
        node4 = TextNode("This is a text node without a link", "text")
        node5 = TextNode("This is a [](https://ligma.bll)", "text")
        node6 = TextNode("[link](https://ligma.bll)", "text")
        node7 = TextNode("[link](https://ligma.bll)[linked](https://slugma.bll)", "text")
        self.assertEqual(split_nodes_link([node1]), [TextNode("This is a ", "text"), TextNode("link", "link", "https://ligma.bll")])
        self.assertEqual(split_nodes_link([node2]), [TextNode("This is a ", "text"), TextNode("link", "link", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("linked", "link", "http://slugma.bll")])
        self.assertEqual(split_nodes_link([node1, node2]), [TextNode("This is a ", "text"), TextNode("link", "link", "https://ligma.bll"), TextNode("This is a ", "text"), TextNode("link", "link", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("linked", "link", "http://slugma.bll")])
        self.assertEqual(split_nodes_link([node3]), [node3])
        self.assertEqual(split_nodes_link([node4]), [node4])
        self.assertEqual(split_nodes_link([node5]), [TextNode("This is a ", "text")])
        self.assertEqual(split_nodes_link([node6]), [TextNode("link", "link", "https://ligma.bll")])
        self.assertEqual(split_nodes_link([node7]), [TextNode("link", "link", "https://ligma.bll"), TextNode("linked", "link", "https://slugma.bll")])

    def test_text_to_textnodes(self):
        text1 = "This is an ![image](https://ligma.bll)"
        text2 = "This is a [link](https://gulpin.dyz)"
        text3 = "This is a **bold** statement"
        text4 = "This is an *italic* statement"
        text5 = "This is a world of `code`"
        text6 = f"{text1} that ![imaged](http://slugma.bll)"
        text7 = f"{text2} that [linked](https://dragma.bll)"
        text8 = f"{text3} with **bolder** claims"
        text9 = f"{text4} with *italicer* ideas"
        text10 = f"{text5} that has been `coded`"
        self.assertEqual(text_to_textnodes(text1), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll")])
        self.assertEqual(text_to_textnodes(text2), [TextNode("This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz")])
        self.assertEqual(text_to_textnodes(text3), [TextNode("This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement", "text")])
        self.assertEqual(text_to_textnodes(text4), [TextNode("This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement", "text")])
        self.assertEqual(text_to_textnodes(text5), [TextNode("This is a world of ", "text"), TextNode("code", "code")])
        self.assertEqual(text_to_textnodes(text6), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("imaged", "image", "http://slugma.bll")])
        self.assertEqual(text_to_textnodes(text7), [TextNode("This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz"), TextNode(" that ", "text"), TextNode("linked", "link", "https://dragma.bll")])
        self.assertEqual(text_to_textnodes(text8), [TextNode("This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement with ", "text"), TextNode("bolder", "bold"), TextNode(" claims", "text")])
        self.assertEqual(text_to_textnodes(text9), [TextNode("This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement with ", "text"), TextNode("italicer", "italic"), TextNode(" ideas", "text")])
        self.assertEqual(text_to_textnodes(text10), [TextNode("This is a world of ", "text"), TextNode("code", "code"), TextNode(" that has been ", "text"), TextNode("coded", "code")])
        self.assertEqual(text_to_textnodes(f"{text1} {text2}"), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz")])
        self.assertEqual(text_to_textnodes(f"{text2} {text3}"), [TextNode("This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz"), TextNode(" This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement", "text")])
        self.assertEqual(text_to_textnodes(f"{text3} {text4}"), [TextNode("This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement", "text")])
        self.assertEqual(text_to_textnodes(f"{text4} {text5}"), [TextNode("This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement This is a world of ", "text"), TextNode("code", "code")])
        self.assertEqual(text_to_textnodes(f"{text1} {text2} {text3}"), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz"), TextNode(" This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement", "text")])
        self.assertEqual(text_to_textnodes(f"{text1} {text2} {text3} {text4} {text5}"), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz"), TextNode(" This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement This is a world of ", "text"), TextNode("code", "code")])
        self.assertEqual(text_to_textnodes(f"{text6} {text7} {text8} {text9} {text10}"), [TextNode("This is an ", "text"), TextNode("image", "image", "https://ligma.bll"), TextNode(" that ", "text"), TextNode("imaged", "image", "http://slugma.bll"), TextNode(" This is a ", "text"), TextNode("link", "link", "https://gulpin.dyz"), TextNode(" that ", "text"), TextNode("linked", "link", "https://dragma.bll"), TextNode(" This is a ", "text"), TextNode("bold", "bold"), TextNode(" statement with ", "text"), TextNode("bolder", "bold"), TextNode(" claims This is an ", "text"), TextNode("italic", "italic"), TextNode(" statement with ", "text"), TextNode("italicer", "italic"), TextNode(" ideas This is a world of ", "text"), TextNode("code", "code"), TextNode(" that has been ", "text"), TextNode("coded", "code")])

if __name__ == "__main__":
    unittest.main()