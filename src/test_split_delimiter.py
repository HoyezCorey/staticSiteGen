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
        
    def test_code_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a `code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ])
        
    def test_unknown_delimiter_in_text(self):
        node = TextNode("I'm a textnode with an unknown delimiter", TextType.TEXT)
        with self.assertRaises(Exception): new_nodes = split_nodes_delimiter([node],"*_", TextType.TEXT)
        
    def test_node_not_texttype_text(self):
        node = TextNode("I'm a bold texttype textnode", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node],"`", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a bold texttype textnode", TextType.BOLD)
        ])
        
    def test_multiple_node_with_delimiter_in_text(self):
        node = TextNode("I'm a textnode with a `code` word", TextType.TEXT)
        node2 = TextNode("I'm another textnode with a `code` word too", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2],"`", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("I'm another textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word too", TextType.TEXT)
        ])
        
    def test_multiple_node_with_one_not_text(self):
        node = TextNode("I'm an italic textnode", TextType.ITALIC)
        node2 = TextNode("I'm another textnode with a `code` word too", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2],"`", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm an italic textnode", TextType.ITALIC),
            TextNode("I'm another textnode with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word too", TextType.TEXT)
        ])
        
    def test_multiple_delimiter_in_text(self):
        node = TextNode("I'm a textnode with two `code` `word`!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("I'm a textnode with two ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" `word`!", TextType.TEXT)
        ])
        