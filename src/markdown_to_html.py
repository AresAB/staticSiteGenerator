from block_markdown import markdown_to_blocks

def extract_heading(markdown):
    markdown.lstrip()
    blocks = markdown_to_blocks(markdown)
    h1_block = blocks[0].lstrip()
    if h1_block[:2] != "# ": raise Exception("Invalid Markdown: Markdown input doesn't start with a h1")
    return h1_block[2:]