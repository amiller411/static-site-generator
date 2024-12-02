'''Module to handle file movements.'''
import logging
import os
import shutil

def get_all_file_paths(folder_path: str) -> list:
    """
    Returns a list of full file paths for all files in the specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        list: A list of file paths for all files in the folder.
    """
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def insert_folder_in_path(file_path: str, folder_name: str) -> str:
    """
    Inserts a folder at the end of a file path, just before the file name.

    Args:
        file_path (str): The original file path.
        folder_name (str): The name of the folder to insert.

    Returns:
        str: The updated file path with the folder inserted.
    """
    # Split the path into directory and file name
    directory, file_name = os.path.split(file_path)

    # Insert the folder name before the file name
    new_path = os.path.join(directory, folder_name, file_name)
    return new_path

def populate_public_dir(source_dir, dest_dir):
    """
    Recursively copies contents
    """
    # Delete destination contents
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    os.mkdir(os.path.join(dest_dir, "images"))

    # Copy all files, sub dirs and nested files
    source_contents = get_all_file_paths(source_dir)

    img_ext = [".png", ".jpeg"]

    for obj in source_contents:
        if os.path.isfile(obj):
            try:
                not_ext, ext = os.path.splitext(obj)
                output_path = obj.replace(source_dir, dest_dir)
                if ext in img_ext:
                    output_path = insert_folder_in_path(output_path, "images")

                shutil.copy(obj, output_path)
                logging.info(f"Copied: {obj}")
                # Log paths
            except Exception as e:
                logging.error(f"Copy error: {obj}")
    return

