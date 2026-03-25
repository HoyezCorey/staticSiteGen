import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notEqText(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_notEqTextType(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_notEqUrl(self):
        node = TextNode("I'm a text node", TextType.LINK, "[link](https:boot.dev)")
        node2 = TextNode("I'm another one text node", TextType.IMAGE, "![image](url/to/image.png)")
        self.assertNotEqual(node, node2)

    def test_urlIsNone(self):
        node = TextNode("I'm a text node", TextType.CODE)
        self.assertIsNone(node.url)

    def test_urlNotNone(self):
        node = TextNode("I'm a text node", TextType.TEXT, "Plain text")
        self.assertIsNotNone(node.url)

    def test_falseProperty(self):
        node = TextNode("I'm a strange text node", "Very strange")
        self.assertNotIsInstance(node.text_type, TextType)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "url/of/img.png")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "url/of/img.png", "alt": "This is an image text node"})

    def test_wrong_text_type(self):
        node = TextNode("This is a bad text node", "BAD")
        with self.assertRaises(ValueError): html_node = TextNode.text_node_to_html_node(node)
        
                                 
if __name__ == "__main__":
    unittest.main()