import unittest
from split_delimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_bold_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])

    def test_italic_delimiter_in_text(self):
        node = TextNode("I'm a textnode with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ])
        
    def test_code_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a `code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ])
        
    def test_unknown_delimiter_in_text(self):
        node = TextNode("I'm a textnode with an *_unknown*_ delimiter", TextType.TEXT)
        with self.assertRaises(Exception): new_nodes = split_nodes_delimiter([node],"*_", "unknown")
        
    def test_node_not_texttype_text(self):
        node = TextNode("I'm a bold texttype textnode", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("I'm a bold texttype textnode", TextType.TEXT)])
        
    def test_multiple_node_with_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a `code` word", TextType.TEXT)
        node2 = TextNode("I'm another textnode with a `code` word too", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2],"`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("I'm another textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word too", TextType.TEXT)
        ])
        
    def test_multiple_node_with_one_just_text(self):
        node = TextNode("I'm not an italic textnode", TextType.TEXT)
        node2 = TextNode("I'm another textnode with a `code` word too", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2],"`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("I'm not an italic textnode", TextType.TEXT),
            TextNode("I'm another textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word too", TextType.TEXT)
        ])
        
    def test_multiple_delimiter_in_text(self):
        node = TextNode("I'm a textnode with two `code` `word`!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with two ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" `word`!", TextType.TEXT)
        ])
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to youtube","https://www.youtube.com/@bootdotdev")], matches)