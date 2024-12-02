import unittest
from enum import Enum
from htmlnode import LeafNode
from text_node import TextType, TextNode, text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_normal(self):
        text_node = TextNode(text="Normal text", text_type=TextType.NORMAL)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Normal text")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_bold(self):
        text_node = TextNode(text="Bold text", text_type=TextType.BOLD)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="b", value="Bold text")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_italic(self):
        text_node = TextNode(text="Italic text", text_type=TextType.ITALIC)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="i", value="Italic text")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_code(self):
        text_node = TextNode(text="Code snippet", text_type=TextType.CODE)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="code", value="Code snippet")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_links(self):
        text_node = TextNode(text="Click here", text_type=TextType.LINKS, url="https://example.com")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="a", value="Click here", props={"href": "https://example.com"})
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_links_missing_url(self):
        text_node = TextNode(text="Click here", text_type=TextType.LINKS)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Links must have a URL")

    def test_text_type_images(self):
        text_node = TextNode(text="Alt text", text_type=TextType.IMAGES, url="https://example.com/image.jpg")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag="img", value="", props={"src": "https://example.com/image.jpg", "alt": "Alt text"})
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_type_images_missing_url(self):
        text_node = TextNode(text="Alt text", text_type=TextType.IMAGES)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Images must have a source URL")

    def test_text_type_unmapped(self):
        text_node = TextNode(text="Unmapped text", text_type=None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Not mapped")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGES, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
