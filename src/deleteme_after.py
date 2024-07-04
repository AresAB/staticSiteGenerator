from markdown_to_html import extract_heading

text1 = "# This is a heading\n\nalongside another\n\nand oncemore"
text2 = "         # This is a heading\n\nalongside another\n\nand oncemore"
text3 = " \n\n\n # This is a heading\n\nalongside another\n\nand oncemore"
text4 = "## This is a failure\n\nalongside another\n\nand oncemore"
text5 = "#This is a failure\n\nalongside another\n\nand oncemore"
text6 = "This is a failure\n\nalongside another\n\nand oncemore"
print(extract_heading(text6))