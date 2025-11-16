from mcp.server.fastmcp import FastMCP

from typing import List
import os

mcp_server = FastMCP("PersonalTasks")


@mcp_server.tool()
def list_personal_files() -> List[str]:
    """Get a list of personal files stored in the 'personal_files' directory.

    Returns:
        List[str]: A list of filenames in the 'personal_files' directory.
    """
    personal_files_dir = '/mnt/p/'
    if not os.path.exists(personal_files_dir):
        return []

    return os.listdir(personal_files_dir)


@mcp_server.tool()
def list_personal_directory(directory_path: str) -> List[str]:
    """List the contents of a specified directory within the 'personal_files' directory.

    Args:
        directory_path (str): The relative path of the directory to list.

    Returns:
        List[str]: A list of filenames in the specified directory.
    """
    personal_files_dir = '/mnt/p/'
    target_directory = os.path.join(personal_files_dir, directory_path)

    if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
        return []

    return os.listdir(target_directory)


@mcp_server.tool()
def read_personal_file(file_name: str) -> str:
    """Read the content of a personal file from the 'personal_files' directory.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    personal_files_dir = '/mnt/p/'
    file_path = os.path.join(personal_files_dir, file_name)

    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist."

    with open(file_path, 'r') as file:
        content = file.read()

    return content


@mcp_server.tool()
def move_personal_file(source_file_name: str, destination_file_name: str) -> str:
    """Move or rename a personal file within the 'personal_files' directory.

    Args:
        source_file_name (str): The current name of the file.
        destination_file_name (str): The new name for the file.

    Returns:
        str: A message indicating the result of the operation.
    """
    personal_files_dir = '/mnt/p/'
    source_path = os.path.join(personal_files_dir, source_file_name)
    destination_path = os.path.join(personal_files_dir, destination_file_name)

    if not os.path.exists(source_path):
        return f"Source file '{source_file_name}' does not exist."

    os.rename(source_path, destination_path)

    return f"File '{source_file_name}' has been moved/renamed to '{destination_file_name}'."


if __name__ == "__main__":
    mcp_server.run(transport='stdio')
