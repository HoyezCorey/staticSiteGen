from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    markdownType = ["","**","_","`"]
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if (delimiter in markdownType) and (node.text.count(delimiter) % 2) == 0:
                if node.text.count(delimiter) != 0:
                    node_split = node.text.split(delimiter, 2)
                    for i in range(0, len(node_split)):
                        match i:
                            case 0 | 2:
                                new_nodes.append(TextNode(node_split[i], TextType.TEXT))
                            case 1:
                                new_nodes.append(TextNode(node_split[i], text_type))
                else:
                    new_nodes.append(node)
            else:
                raise Exception("Invalid Markdown Syntax")
    return new_nodes

def extract_markdown_images(text):
    alts = list(re.findall(r"!\[\w+\]", text))
    alts = list(map(lambda s: s.replace("![", "").replace("]", ""), alts))
    urls = list(re.findall(r"\(https?:\/\/.*?\)", text))
    urls = list(map(lambda s: s.replace("(", "").replace(")", ""), urls))
    matches = list(zip(alts, urls))
    return matches

def extract_markdown_links(text):
    anchors = list(re.findall(r"(?<!!)\[.*?\]", text))
    anchors = list(map(lambda s: s.replace("[", "").replace("]", ""), anchors))
    urls = list(re.findall(r"\(https?:\/\/.*?\)", text))
    urls = list(map(lambda s: s.replace("(", "").replace(")", ""), urls))
    matches = list(zip(anchors, urls))
    return matches