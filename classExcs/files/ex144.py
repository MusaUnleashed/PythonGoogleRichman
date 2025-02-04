import os
import sys
from collections import defaultdict
from pathlib import Path


def get_extension(filename):
    """Returns the file extension, or '.' if there's no extension."""
    if filename.endswith("."):
        return "."
    ext = Path(filename).suffix[1:]
    return ext if ext else "."


def get_file_info(directory):
    """Returns a dictionary with extensions as keys and (count, total_size) as values."""
    file_info = defaultdict(lambda: [0, 0])

    try:
        for entry in Path(directory).iterdir():
            if entry.is_file():  # Ignore directories
                ext = get_extension(entry.name)
                size = entry.stat().st_size

                file_info[ext][0] += 1
                file_info[ext][1] += size
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        sys.exit(1)

    return file_info


def print_file_info(directory):
    """Prints the file extension information sorted by extension name."""
    file_info = get_file_info(directory)

    for ext in sorted(file_info):
        count, size = file_info[ext]
        print(f"{ext} {count} {size}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "usage: ext_info.py path\ndisplays number of files and total size of files per extension in the specified path."
        )
        sys.exit(1)

    directory = sys.argv[1]
    print_file_info(directory)
