import os
import logging
from file_handling import populate_public_dir
from generation import *

log_file = os.path.join(os.getcwd(), "basic.log")

logging.basicConfig(
    filename=log_file,            # Log file path
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)


def main():
    """
    Clears the public dir
    Copies static files to public dir
    Generates output HTML from markdown using provided template file
    """
    static_dir = "static"
    public_dir = "public"
    content_dir = "content"
    content_markdown = "content/index.md"
    template_file = "template.html"
    output_dir = "public"
    output_path = "public/index.html"

    populate_public_dir(static_dir, public_dir)
    # generate_page(content_markdown, template_file, output_path)
    generate_page_recursive(content_dir, template_file, output_dir)

if __name__ == "__main__":
    main()
