import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text1 = "Paragraph 1\n\nParagraph 2\n\nParagraph 3"
        text2 = "This is a paragraph\n\nThis is another\n\nThis is even more \n\n And this is the most"
        text3 = "Paragraph 1\n\n\n\nParagraph 2\n\n\n\nParagraph 3"
        self.assertEqual(markdown_to_blocks(text1), ["Paragraph 1", "Paragraph 2", "Paragraph 3"])
        self.assertEqual(markdown_to_blocks(text2), ["This is a paragraph", "This is another", "This is even more ", " And this is the most"])
        self.assertEqual(markdown_to_blocks(text3), markdown_to_blocks(text1))

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
        text18 = ">This is a paragraph\nThis is a another"
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