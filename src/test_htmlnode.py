import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = HTMLNode("<a>")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_empty_node(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(None,None,None,{"target" : "_blank", "href" : "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'target="_blank" href="https://boot.dev"')

if __name__ == "__main__":
    unittest.main()