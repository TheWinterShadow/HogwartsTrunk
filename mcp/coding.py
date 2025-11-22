from mcp.server.fastmcp import FastMCP

from typing import List
import os

mcp_server = FastMCP("CodingTasks")


@mcp_server.tool()
def list_coding_directories() -> List[str]:
    """Get a list of directories (repositories) in the coding directory.

    Returns:
        List[str]: A list of directory names in the coding directory.
    """
    coding_dir = '/mnt/q/'
    if not os.path.exists(coding_dir):
        return []

    return [item for item in os.listdir(coding_dir)
            if os.path.isdir(os.path.join(coding_dir, item))]


@mcp_server.tool()
def list_repository_contents(repo_name: str) -> List[str]:
    """List the contents of a specified repository in the coding directory.

    Args:
        repo_name (str): The name of the repository to list.

    Returns:
        List[str]: A list of filenames and directories in the repository.
    """
    coding_dir = '/mnt/q/'
    target_directory = os.path.join(coding_dir, repo_name)

    if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
        return []

    return os.listdir(target_directory)


@mcp_server.tool()
def read_repository_file(repo_name: str, file_path: str) -> str:
    """Read the content of a file from a repository in the coding directory.

    Args:
        repo_name (str): The name of the repository.
        file_path (str): The relative path to the file within the repository.

    Returns:
        str: The content of the file.
    """
    coding_dir = '/mnt/q/'
    full_path = os.path.join(coding_dir, repo_name, file_path)

    if not os.path.exists(full_path):
        return f"File '{file_path}' does not exist in repository '{repo_name}'."

    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        return f"File '{file_path}' appears to be a binary file and cannot be read as text."
    except Exception as e:
        return f"Error reading file '{file_path}': {str(e)}"


@mcp_server.tool()
def find_readme_files(repo_name: str) -> List[str]:
    """Find README files in a repository.

    Args:
        repo_name (str): The name of the repository to search.

    Returns:
        List[str]: A list of README file paths found in the repository.
    """
    coding_dir = '/mnt/q/'
    repo_path = os.path.join(coding_dir, repo_name)

    if not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        return []

    readme_files = []
    readme_patterns = ['README*', 'readme*', 'Readme*']

    for root, dirs, files in os.walk(repo_path):
        for pattern in readme_patterns:
            for file in files:
                if file.upper().startswith('README'):
                    rel_path = os.path.relpath(
                        os.path.join(root, file), repo_path)
                    readme_files.append(rel_path)
                    break

    return readme_files


@mcp_server.tool()
def read_readme_summary(repo_name: str) -> str:
    """Read and return a summary of README files from a repository.

    Args:
        repo_name (str): The name of the repository.

    Returns:
        str: A summary of the README content or error message.
    """
    readme_files = find_readme_files(repo_name)

    if not readme_files:
        return f"No README files found in repository '{repo_name}'."

    summary = f"README files found in '{repo_name}':\n\n"

    for readme_file in readme_files[:3]:  # Limit to first 3 README files
        content = read_repository_file(repo_name, readme_file)
        if not content.startswith("File") and not content.startswith("Error"):
            # Take first 500 characters of README
            preview = content[:500]
            if len(content) > 500:
                preview += "..."
            summary += f"=== {readme_file} ===\n{preview}\n\n"

    return summary


@mcp_server.tool()
def sample_repository_code(repo_name: str, max_files: int = 5) -> str:
    """Sample code files from a repository to understand its purpose and tech stack.

    Args:
        repo_name (str): The name of the repository.
        max_files (int): Maximum number of files to sample (default: 5).

    Returns:
        str: A summary of the code files and their contents.
    """
    coding_dir = '/mnt/q/'
    repo_path = os.path.join(coding_dir, repo_name)

    if not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        return f"Repository '{repo_name}' does not exist."

    # Common code file extensions
    code_extensions = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.cs': 'C#',
        '.go': 'Go',
        '.rs': 'Rust',
        '.php': 'PHP',
        '.rb': 'Ruby',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.scala': 'Scala',
        '.sh': 'Shell Script',
        '.yml': 'YAML',
        '.yaml': 'YAML',
        '.json': 'JSON',
        '.xml': 'XML',
        '.html': 'HTML',
        '.css': 'CSS',
        '.scss': 'SCSS',
        '.sass': 'SASS',
        '.vue': 'Vue.js',
        '.jsx': 'React JSX',
        '.tsx': 'React TypeScript'
    }

    code_files = []
    tech_stack = set()

    for root, dirs, files in os.walk(repo_path):
        # Skip common non-code directories
        excluded_dirs = ['.git', '.vscode', '__pycache__',
                         'node_modules', '.next', 'dist', 'build']
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in code_extensions:
                rel_path = os.path.relpath(os.path.join(root, file), repo_path)
                code_files.append((rel_path, code_extensions[ext]))
                tech_stack.add(code_extensions[ext])

    if not code_files:
        return f"No code files found in repository '{repo_name}'."

    # Sample up to max_files
    sampled_files = code_files[:max_files]

    summary = f"Repository '{repo_name}' Analysis:\n\n"
    summary += f"Tech Stack: {', '.join(sorted(tech_stack))}\n"
    summary += f"Total code files: {len(code_files)}\n\n"

    for file_path, language in sampled_files:
        content = read_repository_file(repo_name, file_path)
        if not content.startswith("File") and not content.startswith("Error"):
            # Take first 200 characters of code
            preview = content[:200].strip()
            if len(content) > 200:
                preview += "..."
            summary += f"=== {file_path} ({language}) ===\n{preview}\n\n"

    return summary


@mcp_server.tool()
def analyze_repository_for_task(repo_name: str, task_description: str) -> str:
    """Analyze a repository to determine if it's suitable for a specific task.

    Args:
        repo_name (str): The name of the repository.
        task_description (str): Description of the task or project type.

    Returns:
        str: Analysis of repository suitability for the task.
    """
    # Get README summary
    readme_summary = read_readme_summary(repo_name)

    # Get code sample
    code_sample = sample_repository_code(repo_name, 3)

    analysis = f"Analysis of '{repo_name}' for task: '{task_description}'\n\n"
    analysis += f"README Summary:\n{readme_summary}\n\n"
    analysis += f"Code Sample:\n{code_sample}\n\n"

    # Basic keyword matching for relevance
    task_lower = task_description.lower()
    content_lower = (readme_summary + code_sample).lower()

    relevance_indicators = []

    # Check for common tech keywords
    tech_keywords = {
        'web': ['html', 'css', 'javascript', 'react', 'vue', 'angular', 'node'],
        'api': ['api', 'rest', 'graphql', 'endpoint', 'server', 'backend'],
        'data': ['data', 'sql', 'database', 'analytics', 'pandas', 'numpy'],
        'machine learning': ['ml', 'ai', 'tensorflow', 'pytorch', 'sklearn', 'model'],
        'mobile': ['android', 'ios', 'swift', 'kotlin', 'react native', 'flutter'],
        'desktop': ['electron', 'qt', 'tkinter', 'javafx', 'wpf'],
        'game': ['game', 'unity', 'unreal', 'pygame', 'godot'],
        'automation': ['automation', 'script', 'selenium', 'ansible', 'terraform']
    }

    for category, keywords in tech_keywords.items():
        if category in task_lower:
            matching_keywords = [kw for kw in keywords if kw in content_lower]
            if matching_keywords:
                relevance_indicators.append(
                    f"Relevant for {category}: found {matching_keywords}")

    if relevance_indicators:
        analysis += "Relevance Analysis:\n" + "\n".join(relevance_indicators)
    else:
        analysis += "No specific relevance indicators found for the given task."

    return analysis


@mcp_server.tool()
def find_best_repositories_for_task(task_description: str, max_repos: int = 5) -> str:
    """Find the best repositories for a specific task by analyzing all available repos.

    Args:
        task_description (str): Description of the task or project type.
        max_repos (int): Maximum number of repositories to analyze (default: 5).

    Returns:
        str: Ranking of repositories by suitability for the task.
    """
    repos = list_coding_directories()

    if not repos:
        return "No repositories found in the coding directory."

    # Analyze each repository
    repo_scores = []

    for repo in repos[:max_repos]:
        try:
            analysis = analyze_repository_for_task(repo, task_description)

            # Simple scoring based on keyword matches
            score = 0
            task_lower = task_description.lower()
            analysis_lower = analysis.lower()

            # Score based on task keywords found in analysis
            for word in task_lower.split():
                if len(word) > 3:  # Skip short words
                    score += analysis_lower.count(word) * 2

            # Bonus for having README
            if "README files found" in analysis and "No README files found" not in analysis:
                score += 5

            # Bonus for having code files
            if "Tech Stack:" in analysis:
                score += 3

            repo_scores.append((repo, score, analysis))

        except Exception as e:
            repo_scores.append(
                (repo, 0, f"Error analyzing repository: {str(e)}"))

    # Sort by score descending
    repo_scores.sort(key=lambda x: x[1], reverse=True)

    result = f"Best repositories for task: '{task_description}'\n\n"

    for i, (repo, score, analysis) in enumerate(repo_scores, 1):
        result += f"{i}. {repo} (Score: {score})\n"
        if score > 0:
            # Include brief summary
            lines = analysis.split('\n')
            summary_lines = [line for line in lines[:10] if line.strip()]
            result += "\n".join(summary_lines[:5]) + "\n\n"
        else:
            result += f"   {analysis}\n\n"

    return result


@mcp_server.tool()
def move_repository_file(repo_name: str, source_file_path: str, destination_file_path: str) -> str:
    """Move or rename a file within a repository in the coding directory.

    Args:
        repo_name (str): The name of the repository.
        source_file_path (str): The current relative path of the file.
        destination_file_path (str): The new relative path for the file.

    Returns:
        str: A message indicating the result of the operation.
    """
    coding_dir = '/mnt/q/'
    source_path = os.path.join(coding_dir, repo_name, source_file_path)
    destination_path = os.path.join(
        coding_dir, repo_name, destination_file_path)

    if not os.path.exists(source_path):
        return f"Source file '{source_file_path}' does not exist in repository '{repo_name}'."

    # Create destination directory if it doesn't exist
    dest_dir = os.path.dirname(destination_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    os.rename(source_path, destination_path)

    return f"File '{source_file_path}' has been moved/renamed to '{destination_file_path}' in repository '{repo_name}'."


if __name__ == "__main__":
    mcp_server.run(transport='stdio')
