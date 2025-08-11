from enum import Enum
import re

class BlockType(Enum):
    __order__= "PARAGRAPH HEADING CODE QUOTE UNORDERED_LIST ORDERED_LIST"
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    final_list = []
    for section in sections:
        section = section.strip()
        if section == "":
            continue
        final_list.append(section)
    return final_list

def block_to_block_type(text):
    split_newline = text.split("\n")
    quote = True
    unordered_list = True
    ordered_list = True
    i = 1
    for line in split_newline:
        if not line.startswith(">"):
            quote = False
        if not line.startswith("- "):
            unordered_list = False
        if not line.startswith(f"{i}. "):
            ordered_list = False
        i += 1
    if quote == True:
        return BlockType.QUOTE
    if text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    if unordered_list == True:
        return BlockType.UNORDERED_LIST
    if ordered_list == True:
        return BlockType.ORDERED_LIST
    matches = re.findall(r"^#{1,6} ", text)
    if len(matches) != 0:
        return BlockType.HEADING
    return BlockType.PARAGRAPH
    