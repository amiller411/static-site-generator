import unittest
from generation import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        # Test case with a valid level 1 heading
        markdown = "# My Markdown Document\n\nThis is some content."
        self.assertEqual(extract_title(markdown), "My Markdown Document")

    def test_multiple_headings(self):
        # Test case with multiple headings (should extract only the first level 1 heading)
        markdown = "# First Title\n\n## Subheading\n\n# Another Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_no_title_raises_exception(self):
        # Test case with no level 1 heading (should raise Exception)
        markdown = "This is just content with no headings."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Match not found")

    def test_heading_with_extra_whitespace(self):
        # Test case with extra whitespace around the title
        markdown = "#   Title with Extra Spaces   "
        self.assertEqual(extract_title(markdown), "Title with Extra Spaces")

    def test_heading_with_special_characters(self):
        # Test case with special characters in the heading
        markdown = "# Title with @#$%^&*()!"
        self.assertEqual(extract_title(markdown), "Title with @#$%^&*()!")

    def test_empty_markdown_raises_exception(self):
        # Test case with empty markdown content (should raise Exception)
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Match not found")

if __name__ == "__main__":
    unittest.main()
