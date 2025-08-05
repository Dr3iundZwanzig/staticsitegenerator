import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Test node", TextType.BOLD)
        node2 = TextNode("Test node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("Test node", TextType.BOLD)
        node2 = TextNode("Different node", TextType.TEXT)
        self.assertNotEqual(node1, node2)
    
    def test_text_type(self):
        node1 = TextNode("Test node", TextType.ITALIC)
        node2 = TextNode("Test node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_link_node(self):
        node1 = TextNode("Link", TextType.LINK, "http://example.com")
        node2 = TextNode("Link", TextType.LINK, "http://example.com")
        self.assertEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_props(self):
        node = TextNode("google", TextType.LINK, "google.de")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "google")
        self.assertEqual(html_node.props, {"href": "google.de"})

if __name__ == "__main__":
    unittest.main()