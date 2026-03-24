from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=[], props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if not self.accepted_tag():
            return self.value
        else:
            match self.tag:
                case "p"|"a"|"b"|"i"|"code":
                    return f'<{self.tag}{" " + self.props_to_html() if self.props else ""}>{self.value}</{self.tag}>'
                case "img":
                    return f'<{self.tag}{" "+ self.props_to_html() if self.props else ""} />'
                case _:
                    return f'<{self.tag}>{self.value}</{self.tag}>'
            
    def accepted_tag(self):
        tags = set(item.value for item in TextType)
        return self.tag in tags
            
    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.props_to_html()}"