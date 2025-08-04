import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()