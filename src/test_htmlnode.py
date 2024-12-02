import unittest

from htmlnode import HTMLNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_props_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        repr_expected = (
            "tag: p\n"
            "value: test text\n"
            "children: []\n"
            "props: {'href': 'https://www.google.com', 'target': '_blank'}"
        )
        
        node = HTMLNode("p", "test text", [], test_props_dict)
        self.assertEqual(repr(node), repr_expected)

    def test_props_to_html(self):
        test_props = {"class": "highlight", "id": "intro"}
        node = HTMLNode("div", "Content", [], test_props)
        expected_html_props = ' class="highlight" id="intro"'
        self.assertEqual(node.props_to_html(), expected_html_props)

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "text")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

if __name__ == "__main__":
    unittest.main()