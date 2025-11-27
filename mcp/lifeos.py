from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any
import os
import platform

mcp_server = FastMCP("LifeOSTasks")


# OS-specific directory paths
def get_lifeos_paths() -> tuple[str, str]:
    """Get OS-specific paths for LifeOS directory and README."""
    system = platform.system().lower()

    if system == "darwin":  # macOS
        base_dir = '/Volumes/Personal/Knowledge/Obsidian/LifeOS'
        readme_path = '/Volumes/Personal/Knowledge/Obsidian/LifeOS/LifeOS README.md'
    elif system == "windows":
        base_dir = '/mnt/p/Knowledge/Obsidian/LifeOS'
        readme_path = '/mnt/p/Knowledge/Obsidian/LifeOS/LifeOS README.md'
    else:  # Linux or other
        base_dir = '/home/user/Personal/Knowledge/Obsidian/LifeOS'
        readme_path = '/home/user/Personal/Knowledge/Obsidian/LifeOS/LifeOS README.md'

    return base_dir, readme_path


LIFEOS_DIR, LIFEOS_README = get_lifeos_paths()


@mcp_server.resource("lifeos-readme")
def get_lifeos_readme() -> str:
    """LifeOS directory documentation and overview.

    This resource provides the content of the LifeOS README.md file, which contains
    documentation about the LifeOS directory structure and organization.
    """
    if not os.path.exists(LIFEOS_README):
        return f"LifeOS README.md not found at {LIFEOS_README}"

    try:
        with open(LIFEOS_README, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except OSError as e:
        return f"Error reading LifeOS README: {str(e)}"


@mcp_server.tool()
def get_lifeos_info() -> Dict[str, Any]:
    """Get information about the LifeOS directory paths and system.

    Returns:
        Dict[str, Any]: Information about the current OS and LifeOS paths.
    """
    return {
        "operating_system": platform.system(),
        "lifeos_directory": LIFEOS_DIR,
        "lifeos_readme": LIFEOS_README,
        "directory_exists": os.path.exists(LIFEOS_DIR),
        "readme_exists": os.path.exists(LIFEOS_README)
    }


@mcp_server.tool()
def list_lifeos_files() -> List[str]:
    """Get a list of files in the LifeOS directory.

    Returns:
        List[str]: A list of filenames and directories in the LifeOS directory.
    """
    if not os.path.exists(LIFEOS_DIR):
        return []

    try:
        return os.listdir(LIFEOS_DIR)
    except OSError:
        return []


@mcp_server.tool()
def list_lifeos_directory(directory_path: str) -> List[str]:
    """List the contents of a specified directory within the LifeOS directory.

    Args:
        directory_path (str): The relative path of the directory to list.

    Returns:
        List[str]: A list of filenames and directories in the specified directory.
    """
    target_directory = os.path.join(LIFEOS_DIR, directory_path)

    if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
        return []

    try:
        return os.listdir(target_directory)
    except OSError:
        return []


@mcp_server.tool()
def read_lifeos_file(file_name: str) -> str:
    """Read the content of a file from the LifeOS directory.

    Args:
        file_name (str): The name of the file to read (can include subdirectories).

    Returns:
        str: The content of the file.
    """
    file_path = os.path.join(LIFEOS_DIR, file_name)

    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist in LifeOS directory."

    if os.path.isdir(file_path):
        return f"'{file_name}' is a directory, not a file."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        return f"Unable to read '{file_name}' - file contains non-UTF-8 content."
    except OSError as e:
        return f"Error reading '{file_name}': {str(e)}"


@mcp_server.tool()
def update_lifeos_file(file_name: str, content: str) -> str:
    """Update or create a file in the LifeOS directory.

    Args:
        file_name (str): The name of the file to update (can include subdirectories).
        content (str): The new content for the file.

    Returns:
        str: A message indicating the result of the operation.
    """
    file_path = os.path.join(LIFEOS_DIR, file_name)

    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            return f"Error creating directory for '{file_name}': {str(e)}"

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"File '{file_name}' has been updated successfully."
    except OSError as e:
        return f"Error updating '{file_name}': {str(e)}"


@mcp_server.tool()
def create_lifeos_directory(directory_path: str) -> str:
    """Create a directory within the LifeOS directory structure.

    Args:
        directory_path (str): The relative path of the directory to create.

    Returns:
        str: A message indicating the result of the operation.
    """
    target_directory = os.path.join(LIFEOS_DIR, directory_path)

    try:
        os.makedirs(target_directory, exist_ok=True)
        return f"Directory '{directory_path}' has been created successfully."
    except OSError as e:
        return f"Error creating directory '{directory_path}': {str(e)}"


@mcp_server.tool()
def search_lifeos_files(search_term: str) -> List[Dict[str, Any]]:
    """Search for files in the LifeOS directory that contain a specific term.

    Args:
        search_term (str): The term to search for in file names.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing file information.
    """
    if not os.path.exists(LIFEOS_DIR):
        return []

    results = []

    for root, _, files in os.walk(LIFEOS_DIR):
        for file in files:
            if search_term.lower() in file.lower():
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, LIFEOS_DIR)

                try:
                    stat_info = os.stat(file_path)
                    results.append({
                        "file_name": file,
                        "relative_path": relative_path,
                        "size": stat_info.st_size,
                        "modified": stat_info.st_mtime
                    })
                except OSError:
                    results.append({
                        "file_name": file,
                        "relative_path": relative_path,
                        "size": "unknown",
                        "modified": "unknown"
                    })

    return results


if __name__ == "__main__":
    mcp_server.run(transport='stdio')
