import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_prop(self):
        node = LeafNode("img", "image", {"src": "url/of/img.png", "alt": "Description of image"})
        self.assertEqual(node.to_html(), '<img src="url/of/img.png" alt="Description of image" />')

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev" target="_blank">Click me!</a>')
    
    def test_leaf_to_html_none_prop(self):
        node = LeafNode("code", "This is code")
        self.assertEqual(node.to_html(), '<code>This is code</code>')
    
    def test_leaf_children(self): 
        with self.assertRaises(TypeError): node = LeafNode("i", "italic", None, {"style": "color:red;"})

if __name__ == "__main__":
    unittest.main()