import unittest
from htmlnode import HTMLnode

class TestTextNode(unittest.TestCase):
    def test_props(self):
        node1 = HTMLnode("h1", "Hello World", None, {"href": "haatps://www.google.com", "target": "_blank"})
        node2 = HTMLnode("a", "good morning", None, {"downlaod": "haatps://www.google.com/image", "target": "_blank"})
        print("test props:")
        print(node1.props_to_html())
        print(node2.props_to_html())
        print("--------------------------------")
    
    def test_repr(self):
        node1 = HTMLnode("h1", "Hello World", None, {"href": "haatps://www.google.com", "target": "_blank"})
        print("test print self:")
        print(node1)
        print("--------------------------------")

    def test_children(self):
        node1 = HTMLnode("h1", "Hello World", None, {"href": "haatps://www.google.com", "target": "_blank"})
        node2 = HTMLnode("a", "good morning", [node1], {"downlaod": "haatps://www.google.com/image", "target": "_blank"})
        print("test children:")
        print(node2)
        print(node1.props_to_html())
        print("--------------------------------")
        


if __name__ == "__main__":
    unittest.main()