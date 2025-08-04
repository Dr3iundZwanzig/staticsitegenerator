import unittest
from htmlnode import HTMLnode

class TestTextNode(unittest.TestCase):
    def test_props(self):
        node = HTMLnode("div", "divine orb", None, {"href": "https://google.de", "class": "moin"})

        self.assertEqual(node.props_to_html(), 'href="https://google.de" class="moin"')
    
    def test_values(self):
        node = HTMLnode("div", "divine orb", None, {"href": "https://google.de"})

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "divine orb")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://google.de"})
    
    def test_repr(self):
        node = HTMLnode("a", "Sacred orb", None,{"href": "https://google.de", "class": "moin"})
        self.assertEqual(node.__repr__(), "HTMLnode(tag=a, value=Sacred orb, children=None, props={'href': 'https://google.de', 'class': 'moin'})")
        


if __name__ == "__main__":
    unittest.main()