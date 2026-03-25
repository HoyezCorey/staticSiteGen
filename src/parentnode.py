from htmlnode import HTMLNode
import functools

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag or self.tag is None:
            raise ValueError(f"Missing tag : {self.tag}")
        if not self.children or self.children is None:
            raise ValueError(f"Missing children : {self.children}")
        else:
            return f'<{self.tag}>{"".join(str(child.to_html()) for child in self.children)}</{self.tag}>'