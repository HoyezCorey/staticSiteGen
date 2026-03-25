from enum import Enum
import leafnode

class TextType(Enum):
    TEXT = ""
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return leafnode.LeafNode(None, text_node.text)
            case TextType.BOLD:
                return leafnode.LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return leafnode.LeafNode("i", text_node.text)
            case TextType.CODE:
                return leafnode.LeafNode("code", text_node.text)
            case TextType.LINK:
                return leafnode.LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return leafnode.LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                return leafnode.LeafNode(None, text_node.text)

    def __eq__(self, other):
        return (isinstance(other, TextNode)) and (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f'{type(self).__name__}({self.text}, {self.text_type}, {self.url})'
    

