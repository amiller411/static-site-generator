'''High level functions for markdown to html generation.'''
import os
import re
from block_handling import markdown_to_html_node
from file_handling import get_all_file_paths


def extract_title(markdown):
    """gets title from markdown data"""
    # Use a regular expression to find the first level 1 heading
    match = re.search(r'^# (.+)', markdown, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()  # Return the content after '#'
    raise Exception("Match not found")


def generate_page(from_path, template_path, dest_path):
    """
    Write a html file for all available markdown files.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r', encoding='utf-8') as file:
        content_markdown = file.read()

    with open(template_path, 'r', encoding='utf-8') as file:
        content_template = file.read()

    node = markdown_to_html_node(content_markdown)
    html_string = node.to_html()
    page_title = extract_title(content_markdown)
    template_updated = content_template.replace('{{ Title }} ', page_title).replace('{{ Content }}', html_string)

    # Extract the directory portion of the file path
    directory = os.path.dirname(dest_path)
    
    # Create all directories if they don't exist
    if directory:  # Ensures directory is not empty
        os.makedirs(directory, exist_ok=True)

    # write html page to path
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(template_updated)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    all_md_files = get_all_file_paths(dir_path_content)

    with open(template_path, 'r', encoding='utf-8') as file:
        content_template = file.read()

    for file in all_md_files:
        print(f"Generating page from {file} to {dest_dir_path} using {template_path}")
        file_name = file

        with open(file, 'r', encoding='utf-8') as file:
            content_markdown = file.read()

        node = markdown_to_html_node(content_markdown)
        html_string = node.to_html()
        page_title = extract_title(content_markdown)
        template_updated = content_template.replace('{{ Title }} ', page_title).replace('{{ Content }}', html_string)
        
        dest_path = file_name.replace(dir_path_content, dest_dir_path)

        # Extract the directory portion of the file path
        directory = os.path.dirname(dest_path)

        # Create all directories if they don't exist
        if directory:  # Ensures directory is not empty
            os.makedirs(directory, exist_ok=True)

        # write html page to path
        with open(dest_path.replace('.md', '.html'), 'w', encoding='utf-8') as file:
            file.write(template_updated)


