import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_bold_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])

    def test_italic_delimiter_in_text(self):
        node = TextNode("I'm a textnode with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])