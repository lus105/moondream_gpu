from pathlib import Path

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp']

def list_files(root_path: Path, file_extensions: list = None) -> list[Path]:
    """Returns a list of file paths from the given directory and its subdirectories.

    Args:
        root_path (Path): Path to the root directory.
        file_extensions (list, optional): List of file extensions to filter by. Defaults to None.

    Returns:
        list[Path]: List of file paths matching the specified extensions.
    """
    root = Path(root_path)

    if not root.exists():
        return []

    if file_extensions is None:
        return []

    # Convert extensions to a set of lowercase extensions for matching
    file_extensions = {ext.lower() for ext in file_extensions}

    file_paths = [
        file_path
        for file_path in root.rglob('*')
        if file_path.is_file() and file_path.suffix.lower() in file_extensions
    ]

    return file_paths