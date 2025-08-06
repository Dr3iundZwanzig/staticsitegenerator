import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i,imgur.com/hund.png)"
        )
        matches2 = extract_markdown_images(
            "This is text with an [image](https://i,imgur.com/hund.png)"
        )
        self.assertEqual([("image", "https://i,imgur.com/hund.png")], matches)
        self.assertNotEqual([("image", "https://i,imgur.com/hund.png")], matches2)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i,imgur.com/cat.png)"
        )
        matches2 = extract_markdown_links(
            "This is text with a ![link](https://i,imgur.com/cat.png)"
        )
        self.assertEqual([("link", "https://i,imgur.com/cat.png")], matches)
        self.assertNotEqual([("link", "https://i,imgur.com/cat.png")], matches2)
    
    def test_extract_markdown_nothing(self):
        matches = extract_markdown_images("!Nothing")
        self.assertEqual([], matches)
