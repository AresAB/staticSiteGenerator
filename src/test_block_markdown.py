import unittest

from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type, 
    block_to_html_paragraph, 
    block_to_html_heading, 
    block_to_html_code, 
    block_to_html_quote, 
    block_to_html_unordered_list, 
    block_to_html_ordered_list,
    markdown_to_htmlnode
)
from htmlnode import ParentNode, LeafNode

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text1 = "Paragraph 1\n\nParagraph 2\n\nParagraph 3"
        text2 = "This is a paragraph\n\nThis is another\n\nThis is even more \n\n And this is the most"
        text3 = "Paragraph 1\n\n\n\nParagraph 2\n\n\n\nParagraph 3"
        self.assertEqual(markdown_to_blocks(text1), ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(markdown_to_blocks(text2), ["This is a paragraph", "This is another", "This is even more ", " And this is the most"])
        self.assertEqual(markdown_to_blocks(text3), markdown_to_blocks(text1))

    def test_block_to_html_paragraph(self):
        text1 = "This is **bolded**"
        text2 = "This is `code`"
        text3 = "She **bolded** on my [link](https://dragma.bll) till I *italic*"
        self.assertEqual(block_to_html_paragraph(text1), ParentNode("p", [LeafNode(None, "This is "), LeafNode("b", "bolded")]))
        self.assertEqual(block_to_html_paragraph(text2), ParentNode("p", [LeafNode(None, "This is "), LeafNode("code", "code")]))
        self.assertEqual(block_to_html_paragraph(text3), ParentNode("p", [LeafNode(None, "She "), LeafNode("b", "bolded"), LeafNode(None, " on my "), LeafNode("a", "link", {"href": "https://dragma.bll"}), LeafNode(None, " till I "), LeafNode("i", "italic")]))

    def test_block_to_html_heading(self):
        text1 = "# This is a heading1"
        text2 = "## This is a heading2"
        text3 = "### This is a heading3"
        text4 = "#### This is a heading4"
        text5 = "##### This is a heading5"
        text6 = "###### This is a heading6"
        text7 = "#### This is **bolded**"
        text8 = "## This is a **bolded** *italic* [link](https://gulpin.dyz)"
        self.assertEqual(block_to_html_heading(text1), ParentNode("h1", [LeafNode(None, "This is a heading1")]))
        self.assertEqual(block_to_html_heading(text2), ParentNode("h2", [LeafNode(None, "This is a heading2")]))
        self.assertEqual(block_to_html_heading(text3), ParentNode("h3", [LeafNode(None, "This is a heading3")]))
        self.assertEqual(block_to_html_heading(text4), ParentNode("h4", [LeafNode(None, "This is a heading4")]))
        self.assertEqual(block_to_html_heading(text5), ParentNode("h5", [LeafNode(None, "This is a heading5")]))
        self.assertEqual(block_to_html_heading(text6), ParentNode("h6", [LeafNode(None, "This is a heading6")]))
        self.assertEqual(block_to_html_heading(text7), ParentNode("h4", [LeafNode(None, "This is "), LeafNode("b", "bolded")]))
        self.assertEqual(block_to_html_heading(text8), ParentNode("h2", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " "), LeafNode("i", "italic"), LeafNode(None, " "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})]))

    def test_block_to_html_code(self):
        text1 = "```This is a code block```"
        text2 = "```This is a `code` block```"
        text3 = "```This is a **bolded** *italic* [link](https://gulpin.dyz)```"
        self.assertEqual(block_to_html_code(text1), ParentNode("pre", [ParentNode("code", [LeafNode(None, "This is a code block")])]))
        self.assertEqual(block_to_html_code(text2), ParentNode("pre", [ParentNode("code", [LeafNode(None, "This is a "), LeafNode("code", "code"), LeafNode(None, " block")])]))
        self.assertEqual(block_to_html_code(text3).to_html(), ParentNode("pre", [ParentNode("code", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " "), LeafNode("i", "italic"), LeafNode(None, " "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})])]).to_html())

    def test_block_to_html_quote(self):
        text1 = ">This is a quote\n>w/ not 1, not 2,\n>but 3 whole lines"
        text2 = ">This is a quote\n>w/ a `code` inline\n>in the middle"
        text3 = ">This is a **bold**\n>w/ an *italic*\n>and a [link](https://gulpin.dyz)"
        self.assertEqual(block_to_html_quote(text1), ParentNode("blockquote", [LeafNode(None, "This is a quote\nw/ not 1, not 2,\nbut 3 whole lines")]))
        self.assertEqual(block_to_html_quote(text2), ParentNode("blockquote", [LeafNode(None, "This is a quote\nw/ a "), LeafNode("code", "code"), LeafNode(None, " inline\nin the middle")]))
        self.assertEqual(block_to_html_quote(text3), ParentNode("blockquote", [LeafNode(None, "This is a "), LeafNode("b", "bold"), LeafNode(None, "\nw/ an "), LeafNode("i", "italic"), LeafNode(None, "\nand a "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})]))

    def test_block_to_html_unordered_list(self):
        text1 = "* This is a list\n- that has\n* 3 lines"
        text2 = "- This is a list\n* with some `code`\n* in it"
        text3 = "* This is a **bolded** and `coded` list\n* that has *italics*\n- and a [link](https://gulpin.dyz)"
        self.assertEqual(block_to_html_unordered_list(text1), ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is a list")]), ParentNode("li", [LeafNode(None, "that has")]), ParentNode("li", [LeafNode(None, "3 lines")])]))
        self.assertEqual(block_to_html_unordered_list(text2), ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is a list")]), ParentNode("li", [LeafNode(None, "with some "), LeafNode("code", "code")]), ParentNode("li", [LeafNode(None, "in it")])]))
        self.assertEqual(block_to_html_unordered_list(text3), ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " and "), LeafNode("code", "coded"), LeafNode(None, " list")]), ParentNode("li", [LeafNode(None, "that has "), LeafNode("i", "italics")]), ParentNode("li", [LeafNode(None, "and a "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})])]))

    def test_block_to_html_ordered_list(self):
        text1 = "1. This is a list\n2. that has\n3. 3 lines"
        text2 = "1. This is a list\n2. with some `code`\n3. in it"
        text3 = "1. This is a **bolded** and `coded` list\n2. that has *italics*\n3. and a [link](https://gulpin.dyz)"
        self.assertEqual(block_to_html_ordered_list(text1), ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is a list")]), ParentNode("li", [LeafNode(None, "that has")]), ParentNode("li", [LeafNode(None, "3 lines")])]))
        self.assertEqual(block_to_html_ordered_list(text2), ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is a list")]), ParentNode("li", [LeafNode(None, "with some "), LeafNode("code", "code")]), ParentNode("li", [LeafNode(None, "in it")])]))
        self.assertEqual(block_to_html_ordered_list(text3), ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " and "), LeafNode("code", "coded"), LeafNode(None, " list")]), ParentNode("li", [LeafNode(None, "that has "), LeafNode("i", "italics")]), ParentNode("li", [LeafNode(None, "and a "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})])]))

    def test_markdown_to_htmlnode(self):
        text1 = "# This is a heading"
        text2 = " ###### This is a heading"
        text3 = "###This is a paragraph"
        text4 = "```This is a code block```"
        text5 = "```This is a``` paragraph"
        text6 = "``This is a paragraph``"
        text7 = ">This is a quote\n>This is another"
        text8 = ">This is a paragraph\nThis is another\n>This is once more"
        text9 = "* This is an unordered list\n* This is another\n- This is yet another"
        text10 = "- This is a paragraph\nThis is another\n- This is yet another"
        text11 = "1. This is an ordered list\n2. This is another"
        text12 = "1. This is an ordered list\n2. This is another\n3. This is yet another"
        text13 = "1. This is a paragraph\nThis is another\n3. This is yet another"
        text14 = "```This is a **bolded** *italic* [link](https://gulpin.dyz)```"
        text15 = "## This is a **bolded** *italic* [link](https://gulpin.dyz)"
        self.assertEqual(markdown_to_htmlnode(f"{text1}\n\n{text3}\n\n{text2}"), ParentNode("div", [ParentNode("h1", [LeafNode(None, "This is a heading")]), ParentNode("p", [LeafNode(None, "###This is a paragraph")]), ParentNode("h6", [LeafNode(None, "This is a heading")])]))
        self.assertEqual(markdown_to_htmlnode(f"{text5}\n\n{text4}\n\n{text6}"), ParentNode("div", [ParentNode("p", [LeafNode("code", "This is a"), LeafNode(None, " paragraph")]), ParentNode("pre", [ParentNode("code", [LeafNode(None, "This is a code block")])]), ParentNode("p", [LeafNode(None, "This is a paragraph")])]))
        self.assertEqual(markdown_to_htmlnode(f"{text7}\n\n{text8}"), ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "This is a quote\nThis is another")]), ParentNode("p", [LeafNode(None, ">This is a paragraph\nThis is another\n>This is once more")])]))
        self.assertEqual(markdown_to_htmlnode(f"{text9}\n\n{text10}"), ParentNode("div", [ParentNode("ul", [ParentNode("li", [LeafNode(None, "This is an unordered list")]), ParentNode("li", [LeafNode(None, "This is another")]), ParentNode("li", [LeafNode(None, "This is yet another")])]), ParentNode("p", [LeafNode(None, "- This is a paragraph\nThis is another\n- This is yet another")])]))
        self.assertEqual(markdown_to_htmlnode(f"{text11}\n\n{text13}\n\n{text12}"), ParentNode("div", [ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is an ordered list")]), ParentNode("li", [LeafNode(None, "This is another")])]), ParentNode("p", [LeafNode(None, "1. This is a paragraph\nThis is another\n3. This is yet another")]), ParentNode("ol", [ParentNode("li", [LeafNode(None, "This is an ordered list")]), ParentNode("li", [LeafNode(None, "This is another")]), ParentNode("li", [LeafNode(None, "This is yet another")])])]))
        self.assertEqual(markdown_to_htmlnode(f"{text14}\n\n{text15}"), ParentNode("div", [ParentNode("pre", [ParentNode("code", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " "), LeafNode("i", "italic"), LeafNode(None, " "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})])]), ParentNode("h2", [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " "), LeafNode("i", "italic"), LeafNode(None, " "), LeafNode("a", "link", {"href": "https://gulpin.dyz"})])]))

    def test_block_to_block_type(self):
        text1 = "This is a paragraph"
        text2 = "#This is a paragraph"
        text3 = "###This is a paragraph"
        text4 = "######This is a paragraph"
        text5 = "# This is a heading"
        text6 = " ### This is a heading"
        text7 = " ###### This is a heading"
        text8 = " ####### This is a paragraph"
        text9 = "```This is a code block```"
        text10 = " ``` This is a code block``` "
        text11 = "```This is a paragraph"
        text12 = "This is a paragraph```"
        text13 = "```This is a``` paragraph"
        text14 = "``This is a paragraph``"
        text15 = ">This is a quote"
        text16 = ">This is a quote\n>This is another"
        text17 = ">This is a quote\n>This is another\n> This is yet another"
        text18 = ">This is a paragraph\nThis is another"
        text19 = ">This is a paragraph\nThis is another\n>This is yet another"
        text20 = ">This is a paragraph\n>This is another\nThis is yet another"
        text21 = "- This is an unordered list"
        text22 = "- This is an unordered list\n- This is another"
        text23 = "- This is an unordered list\n- This is another\n- This is yet another"
        text24 = "- This is a paragraph\nThis is another"
        text25 = "- This is a paragraph\nThis is another\n- This is yet another"
        text26 = "- This is a paragraph\n-This is another\n- This is yet another"
        text27 = "* This is an unordered list"
        text28 = "* This is an unordered list\n* This is another"
        text29 = "* This is an unordered list\n* This is another\n- This is yet another"
        text30 = "* This is a paragraph\nThis is another"
        text31 = "* This is a paragraph\nThis is another\n* This is yet another"
        text32 = "* This is a paragraph\n*This is another\n* This is yet another"
        text33 = "1. This is an ordered list"
        text34 = "1. This is an ordered list\n2. This is another"
        text35 = "1. This is an ordered list\n2. This is another\n3. This is yet another"
        text36 = "1. This is a paragraph\nThis is another"
        text37 = "1. This is a paragraph\nThis is another\n3. This is yet another"
        text38 = "1. This is a paragraph\n2. This is another\nThis is yet another"
        text39 = "1. This is a paragraph\n2.This is another\n3. This is yet another"
        text40 = "2. This is a paragraph\n3. This is another\n4. This is yet another"
        self.assertEqual(block_to_block_type(text1), "paragraph")
        self.assertEqual(block_to_block_type(text2), "paragraph")
        self.assertEqual(block_to_block_type(text3), "paragraph")
        self.assertEqual(block_to_block_type(text4), "paragraph")
        self.assertEqual(block_to_block_type(text5), "heading")
        self.assertEqual(block_to_block_type(text6), "heading")
        self.assertEqual(block_to_block_type(text7), "heading")
        self.assertEqual(block_to_block_type(text8), "paragraph")
        self.assertEqual(block_to_block_type(text9), "code")
        self.assertEqual(block_to_block_type(text10), "code")
        self.assertEqual(block_to_block_type(text11), "paragraph")
        self.assertEqual(block_to_block_type(text12), "paragraph")
        self.assertEqual(block_to_block_type(text13), "paragraph")
        self.assertEqual(block_to_block_type(text14), "paragraph")
        self.assertEqual(block_to_block_type(text15), "quote")
        self.assertEqual(block_to_block_type(text16), "quote")
        self.assertEqual(block_to_block_type(text17), "quote")
        self.assertEqual(block_to_block_type(text18), "paragraph")
        self.assertEqual(block_to_block_type(text19), "paragraph")
        self.assertEqual(block_to_block_type(text20), "paragraph")
        self.assertEqual(block_to_block_type(text21), "unordered list")
        self.assertEqual(block_to_block_type(text22), "unordered list")
        self.assertEqual(block_to_block_type(text23), "unordered list")
        self.assertEqual(block_to_block_type(text24), "paragraph")
        self.assertEqual(block_to_block_type(text25), "paragraph")
        self.assertEqual(block_to_block_type(text26), "paragraph")
        self.assertEqual(block_to_block_type(text27), "unordered list")
        self.assertEqual(block_to_block_type(text28), "unordered list")
        self.assertEqual(block_to_block_type(text29), "unordered list")
        self.assertEqual(block_to_block_type(text30), "paragraph")
        self.assertEqual(block_to_block_type(text31), "paragraph")
        self.assertEqual(block_to_block_type(text32), "paragraph")
        self.assertEqual(block_to_block_type(text33), "ordered list")
        self.assertEqual(block_to_block_type(text34), "ordered list")
        self.assertEqual(block_to_block_type(text35), "ordered list")
        self.assertEqual(block_to_block_type(text36), "paragraph")
        self.assertEqual(block_to_block_type(text37), "paragraph")
        self.assertEqual(block_to_block_type(text38), "paragraph")
        self.assertEqual(block_to_block_type(text39), "paragraph")
        self.assertEqual(block_to_block_type(text40), "paragraph")

if __name__ == "__main__":
    unittest.main()