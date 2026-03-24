from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children:
            raise ValueError("Missing children")
        else:
            return f'<{self.tag}>{self.children.to_html()}<{self.tag}/>'