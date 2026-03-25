import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_more_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node_i = LeafNode("i", "grandchild_i")
        child_node = ParentNode("span", [grandchild_node, grandchild_node_i])
        parent_node = ParentNode("div", [child_node, child_node, grandchild_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><i>grandchild_i</i></span><span><b>grandchild</b><i>grandchild_i</i></span><b>grandchild</b></div>",
        )

if __name__ == "__main__":
    unittest.main()