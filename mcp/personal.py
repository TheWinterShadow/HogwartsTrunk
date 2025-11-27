from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any
import os
import platform

mcp_server = FastMCP("PersonalTasks")


# OS-specific directory paths
def get_personal_files_path() -> str:
    """Get OS-specific path for personal files directory."""
    system = platform.system().lower()
    
    if system == "darwin":  # macOS
        return '/Volumes/Personal'
    elif system == "windows":
        return '/mnt/p/'
    else:  # Linux or other
        return '/mnt/p/'


PERSONAL_FILES_DIR = get_personal_files_path()


@mcp_server.tool()
def get_personal_info() -> Dict[str, Any]:
    """Get information about the personal files directory and system.

    Returns:
        Dict[str, Any]: Information about the current OS and personal files path.
    """
    return {
        "operating_system": platform.system(),
        "personal_files_directory": PERSONAL_FILES_DIR,
        "directory_exists": os.path.exists(PERSONAL_FILES_DIR)
    }


@mcp_server.tool()
def list_personal_files() -> List[str]:
    """Get a list of personal files stored in the personal files directory.

    Returns:
        List[str]: A list of filenames in the personal files directory.
    """
    if not os.path.exists(PERSONAL_FILES_DIR):
        return []

    try:
        return os.listdir(PERSONAL_FILES_DIR)
    except (IOError, OSError):
        return []


@mcp_server.tool()
def list_personal_directory(directory_path: str) -> List[str]:
    """List the contents of a specified directory within the personal files directory.

    Args:
        directory_path (str): The relative path of the directory to list.

    Returns:
        List[str]: A list of filenames in the specified directory.
    """
    target_directory = os.path.join(PERSONAL_FILES_DIR, directory_path)

    if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
        return []

    try:
        return os.listdir(target_directory)
    except (IOError, OSError):
        return []


@mcp_server.tool()
def read_personal_file(file_name: str) -> str:
    """Read the content of a personal file from the personal files directory.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    file_path = os.path.join(PERSONAL_FILES_DIR, file_name)

    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist."
    
    if os.path.isdir(file_path):
        return f"'{file_name}' is a directory, not a file."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        return f"Unable to read '{file_name}' - file contains non-UTF-8 content."
    except (IOError, OSError) as e:
        return f"Error reading '{file_name}': {str(e)}"


@mcp_server.tool()
def update_personal_file(file_name: str, content: str) -> str:
    """Update or create a file in the personal files directory.

    Args:
        file_name (str): The name of the file to update (can include subdirectories).
        content (str): The new content for the file.

    Returns:
        str: A message indicating the result of the operation.
    """
    file_path = os.path.join(PERSONAL_FILES_DIR, file_name)
    
    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except (IOError, OSError) as e:
            return f"Error creating directory for '{file_name}': {str(e)}"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"File '{file_name}' has been updated successfully."
    except (IOError, OSError) as e:
        return f"Error updating '{file_name}': {str(e)}"


@mcp_server.tool()
def move_personal_file(source_file_name: str, destination_file_name: str) -> str:
    """Move or rename a personal file within the personal files directory.

    Args:
        source_file_name (str): The current name of the file.
        destination_file_name (str): The new name for the file.

    Returns:
        str: A message indicating the result of the operation.
    """
    source_path = os.path.join(PERSONAL_FILES_DIR, source_file_name)
    destination_path = os.path.join(PERSONAL_FILES_DIR, destination_file_name)

    if not os.path.exists(source_path):
        return f"Source file '{source_file_name}' does not exist."

    try:
        os.rename(source_path, destination_path)
        return f"File '{source_file_name}' has been moved/renamed to '{destination_file_name}'."
    except OSError as e:
        return f"Error moving '{source_file_name}': {str(e)}"


if __name__ == "__main__":
    mcp_server.run(transport='stdio')
