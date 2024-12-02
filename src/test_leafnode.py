import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq_a(self):
        a = "<p>This is a paragraph of text.</p>"
        
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), a)

    def test_eq_b(self):
        b = '<a href="https://www.google.com">Click me!</a>'
        
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), b)


if __name__ == "__main__":
    unittest.main()