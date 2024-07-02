from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import textNodes_to_HTMLNodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

# this function seperates text into blocks, with the delimiter being a whitespace line. Might be worth messing with different delimiters for different markdown standards
def markdown_to_blocks(markdown):
    return list(filter(lambda x: x != "", markdown.split("\n\n")))

def block_to_block_type(input_block):
    block = input_block.strip()
    heading_block_list = block.split("# ", 1)
    if block[0] == "#" and ((len(heading_block_list) > 1 and len(heading_block_list[0]) < 6) or block[:2] == "# "): # I don't think this needs to account for single value arrays like I thought
        return block_type_heading
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    block_list = block.split("\n")
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    for i in range(0, len(block_list)):
        list = block_list[i]
        if list[:1] != ">": is_quote = False
        if list[:2] != "* " and list[:2] != "- ": is_unordered_list = False
        if list[:3] != f"{i + 1}. ": is_ordered_list = False
    if is_quote: return block_type_quote
    if is_unordered_list: return block_type_unordered_list
    if is_ordered_list: return block_type_ordered_list
    return block_type_paragraph

def block_to_html_paragraph(block):
    return ParentNode("p", textNodes_to_HTMLNodes(text_to_textnodes(block)))

def block_to_html_heading(block):
    heading_block_list = block.lstrip().split("# ", 1)
    return ParentNode(f"h{len(heading_block_list[0]) + 1}", textNodes_to_HTMLNodes(text_to_textnodes(heading_block_list[1])))

def block_to_html_code(block):
    return ParentNode("pre", [ParentNode("code", textNodes_to_HTMLNodes(text_to_textnodes(block[3:-3])))])

def block_to_html_quote(block):
    stripped_block = "\n".join(list(map(lambda x: x.lstrip(">"), block.split("\n"))))
    return ParentNode("blockquote", textNodes_to_HTMLNodes(text_to_textnodes(stripped_block)))

def block_to_html_unordered_list(block):
    split_block = block.split("\n")
    list_components = []
    for line in split_block:
        list_components.append(ParentNode("li", textNodes_to_HTMLNodes(text_to_textnodes(line[2:]))))
    return ParentNode("ul", list_components)

def block_to_html_ordered_list(block):
    split_block = block.split("\n")
    list_components = []
    for line in split_block:
        list_components.append(ParentNode("li", textNodes_to_HTMLNodes(text_to_textnodes(line[3:]))))
    return ParentNode("ol", list_components)

def markdown_to_htmlnode(text):
    blocks = markdown_to_blocks(text)
    parentNodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            parentNodes.append(block_to_html_paragraph(block))
            continue
        if block_type == block_type_heading:
            parentNodes.append(block_to_html_heading(block))
            continue
        if block_type == block_type_code:
            parentNodes.append(block_to_html_code(block))
            continue
        if block_type == block_type_quote:
            parentNodes.append(block_to_html_quote(block))
            continue
        if block_type == block_type_unordered_list:
            parentNodes.append(block_to_html_unordered_list(block))
            continue
        if block_type == block_type_ordered_list:
            parentNodes.append(block_to_html_ordered_list(block))
    return ParentNode("div", parentNodes)