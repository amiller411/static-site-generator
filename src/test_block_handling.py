import unittest
from block_handling import *

class TestBlocks(unittest.TestCase):
    def test_md_to_block(self):
        txt =  """ # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        block = markdown_to_blocks(txt)
        self.assertListEqual(
            [ "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
            block,
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("## Heading 2"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")
        self.assertNotEqual(block_to_block_type("#HeadingWithoutSpace"), "heading")
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello, world!')\n```"), "code")
        self.assertEqual(block_to_block_type("```\nCode block\n```"), "code")
        self.assertNotEqual(block_to_block_type("```Code without closing"), "code")
    
    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2\n> Line 3"), "quote")
        self.assertNotEqual(block_to_block_type(">Mixed lines\nNormal text"), "quote")
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), "unordered list")
        self.assertEqual(block_to_block_type("* Item A\n* Item B\n* Item C"), "unordered list")
        self.assertNotEqual(block_to_block_type("-ItemWithoutSpace\n- AnotherItem"), "unordered list")
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item\n3. Third item"), "ordered list")
        self.assertEqual(block_to_block_type("1. Alpha\n2. Beta\n3. Gamma"), "ordered list")
        self.assertNotEqual(block_to_block_type("1. Misnumbered\n3. Another"), "ordered list")
    
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), "paragraph")
        self.assertEqual(block_to_block_type("Another line of text."), "paragraph")
        self.assertNotEqual(block_to_block_type("1. Numbered but not an ordered list"), "paragraph")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()