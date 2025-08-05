import unittest
from htmlnode import HTMLnode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_props(self):
        node = HTMLnode("div", "divine orb", None, {"href": "https://google.de", "class": "moin"})

        self.assertEqual(node.props_to_html(), ' href="https://google.de" class="moin"')
    
    def test_values(self):
        node = HTMLnode("div", "divine orb", None, {"href": "https://google.de"})

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "divine orb")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://google.de"})
    
    def test_repr(self):
        node = HTMLnode("a", "Sacred orb", None,{"href": "https://google.de", "class": "moin"})
        self.assertEqual(node.__repr__(), "HTMLnode(tag=a, value=Sacred orb, children=None, props={'href': 'https://google.de', 'class': 'moin'})")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.de", "class": "moin"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.de" class="moin">Hello, world!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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
    
    def test_to_html_with_grandchildren_with_props(self):
        grandchild_node = LeafNode("a", "google", {"href": "https://www.google.de", "class": "moin"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"class": "moin"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="moin"><span><a href="https://www.google.de" class="moin">google</a></span></div>',
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()