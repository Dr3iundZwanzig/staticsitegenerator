from enum import Enum
from htmlnode import HTMLnode, LeafNode
from extract_markdown import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    __order__= "TEXT BOLD ITALIC CODE LINK IMAGE"
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
        
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError(f"unknown text type: {text_node.text_type}")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text,{"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            return "no case found"
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []           
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue
        if (node.text.count(delimiter) % 2) != 0:
            raise Exception("delimiter not closed")
        split_list = node.text.split(delimiter)
        for i in range(len(split_list)):
            if split_list[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_list[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_list[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):            
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_list = extract_markdown_images(node.text)
        if len(extracted_list) == 0:
            new_nodes.append(node)
            continue
        og_text = node.text
        image_text = extracted_list[0][0]
        image_link = extracted_list[0][1]
        section = og_text.split(f"![{image_text}]({image_link})",1)

        for i in range(len(extracted_list)):
                image_text = extracted_list[i][0]
                image_link = extracted_list[i][1]
                if section[0] == "":
                    new_nodes.append(TextNode(image_text, TextType.IMAGE, image_link))
                else:
                    new_nodes.append(TextNode(section[0], TextType.TEXT))
                    new_nodes.append(TextNode(image_text, TextType.IMAGE, image_link))
                if i+1 == len(extracted_list):
                    if section[1] != "":
                        new_nodes.append(TextNode(section[1], TextType.TEXT))
                    continue
                image_text = extracted_list[i+1][0]
                image_link = extracted_list[i+1][1]
                section = section[1].split(f"![{image_text}]({image_link})",1)

    return new_nodes

def split_nodes_link(old_nodes):            
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_list = extract_markdown_links(node.text)
        if len(extracted_list) == 0:
            new_nodes.append(node)
            continue
        og_text = node.text
        link_text = extracted_list[0][0]
        link = extracted_list[0][1]
        section = og_text.split(f"[{link_text}]({link})",1)

        for i in range(len(extracted_list)):
                link_text = extracted_list[i][0]
                link = extracted_list[i][1]
                if section[0] == "":
                    new_nodes.append(TextNode(link_text, TextType.LINK, link))
                else:
                    new_nodes.append(TextNode(section[0], TextType.TEXT))
                    new_nodes.append(TextNode(link_text, TextType.LINK, link))
                if i+1 == len(extracted_list):
                    if section[1] != "":
                        new_nodes.append(TextNode(section[1], TextType.TEXT))
                    continue
                link_text = extracted_list[i+1][0]
                link = extracted_list[i+1][1]
                section = section[1].split(f"[{link_text}]({link})",1)

    return new_nodes

