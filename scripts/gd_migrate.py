import xml.etree.ElementTree as ET
import os

def get_glodroid_project_paths(xml_file_path: str) -> list[str]:
    """
    Reads a glodroid.xml manifest file and extracts all 'path' attributes
    from <project> tags into a list.

    Args:
        xml_file_path: The full path to the glodroid.xml file.

    Returns:
        A list of strings, where each string is a project path.
        Returns an empty list if the file is not found or no paths are found.
    """
    if not os.path.exists(xml_file_path):
        print(f"Error: The file '{xml_file_path}' does not exist.")
        return []

    project_paths = []
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Find all <project> tags and extract their 'path' attribute
        for project_element in root.findall('project'):
            path = project_element.get('path')
            if path:
                project_paths.append(path)
    except ET.ParseError as e:
        print(f"Error parsing XML file '{xml_file_path}': {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return project_paths

def get_patch_directories(patches_path: str) -> list[str]:
    """
    Reads folder paths in the specified patches directory that contain .patch files.
    """
    if not os.path.isdir(patches_path):
        print(f"Error: The patches directory '{patches_path}' does not exist.")
        return []

    patch_folders = []
    for root, _, files in os.walk(patches_path):
        # Check if any file in the current directory ends with .patch
        if any(f.endswith(".patch") for f in files):
            rel_path = os.path.relpath(root, patches_path)
            if rel_path != ".":
                patch_folders.append(rel_path)

    return patch_folders

if __name__ == "__main__":
    # Example usage:
    glodroid_xml_path = "/SSD1/workspace/GD_A16/aosptree/.repo/manifests/glodroid.xml"
    patches_dir_path = "/SSD1/workspace/GD_A16/patches-aosp"

    paths = get_glodroid_project_paths(glodroid_xml_path)
    patch_dirs = get_patch_directories(patches_dir_path)

    # Add patch directory paths to the list
    paths.extend(patch_dirs)

    # Remove duplicates while preserving order
    paths = list(dict.fromkeys(paths))

    if paths:
        print("\nExtracted paths: with the number of projects is: {}".format(len(paths)))
        for p in paths:
            print(f"- {p}")
    else:
        print("\nNo project paths found or an error occurred.")
