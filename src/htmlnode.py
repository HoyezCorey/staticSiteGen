class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_to_html = ""
        if self.props is None:
            return props_to_html
        for prop in self.props:
            props_to_html += f'{prop}="{self.props[prop]}" '
        return props_to_html.rstrip()
    
    def __eq__(self, other):
        return (isinstance(other, HTMLNode)) and (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props)
    
    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props_to_html}"