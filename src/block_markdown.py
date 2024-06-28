
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
    if block[0] == "#" and ((len(heading_block_list) > 1 and len(heading_block_list[0]) < 6) or block[:2] == "# "):
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