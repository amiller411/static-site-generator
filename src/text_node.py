from enum import Enum
from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.NORMAL:
        return LeafNode(value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    
    elif text_node.text_type == TextType.LINKS:
        if not text_node.url:
            raise Exception("Links must have a URL")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGES:
        if not text_node.url:
            raise Exception("Images must have a source URL")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Not mapped")
    
    return


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False  # Return False if the objects are not of the same type
        return vars(self) == vars(other)  # Compare all attributes in __dict__


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
