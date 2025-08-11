import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestExtractMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_type_heading(self):
        text1 = "### this is a heading"
        text2 = "##### also heading"
        blocktype1 = block_to_block_type(text1)
        blocktype2 = block_to_block_type(text2)

        self.assertEqual(BlockType.HEADING, blocktype1)
        self.assertEqual(BlockType.HEADING, blocktype2)

    def test_block_type_code(self):
        text = "``` this is code ```"
        blocktype = block_to_block_type(text)
        
        self.assertEqual(BlockType.CODE, blocktype)

    def test_block_type_quote(self):
        text = "> hund\n> katze\n> vogel"
        blocktype = block_to_block_type(text)
        
        self.assertEqual(BlockType.QUOTE, blocktype)
    
    def test_block_type_unordered_list(self):
        text = "- hund\n- katze\n- vogel"
        blocktype = block_to_block_type(text)
        
        self.assertEqual(BlockType.UNORDERED_LIST, blocktype)

    def test_block_type_ordered_list(self):
        text = "1. hund\n2. katze\n3. vogel"
        blocktype = block_to_block_type(text)
        
        self.assertEqual(BlockType.ORDERED_LIST, blocktype)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()