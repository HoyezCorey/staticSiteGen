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

    def test_to_html_with_multiple_grandchildrens(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node_i = LeafNode("i", "grandchild_i")
        child_node = ParentNode("span", [grandchild_node, grandchild_node_i])
        parent_node = ParentNode("div", [child_node, child_node, grandchild_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><i>grandchild_i</i></span><span><b>grandchild</b><i>grandchild_i</i></span><b>grandchild</b></div>",
        )

    def test_to_html_with_multiple_parents_and_grandchilds(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node_i = LeafNode("i", "grandchild_i")
        child_node = ParentNode("span", [grandchild_node, grandchild_node_i])
        parent_node = ParentNode("div", [child_node, child_node, grandchild_node])
        grandparent_node = ParentNode("div", [parent_node])
        self.assertEqual(
            grandparent_node.to_html(),
            "<div><div><span><b>grandchild</b><i>grandchild_i</i></span><span><b>grandchild</b><i>grandchild_i</i></span><b>grandchild</b></div></div>",
        )

    def test_parentnode_without_children(self):
        with self.assertRaises(TypeError): parent_node = ParentNode("div")

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError): parent_node.to_html()

    def test_to_html_with_none_child(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError): parent_node.to_html()

    def test_to_html_without_tag(self):
        child_node = LeafNode("code","i'm code")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError): parent_node.to_html()

    def test_to_html_with_empty_tag(self):
        child_node = LeafNode("p","i'm a paragraph")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError): parent_node.to_html()

if __name__ == "__main__":
    unittest.main()