# Python Code Line Counter

import os


def count_python_lines(folder):
    total_lines = 0
    blank_lines = 0
    nonblank_lines = 0
    file_count = 0

    for root, dirs, files in os.walk(folder):
        dirs[:] = [
            directory for directory in dirs
            if directory not in {".git", ".venv", "venv", "__pycache__"}
        ]

        for filename in files:
            if not filename.endswith(".py"):
                continue

            path = os.path.join(root, filename)

            try:
                with open(path, "r", encoding="utf-8") as file:
                    lines = file.readlines()

                file_count += 1
                total_lines += len(lines)

                for line in lines:
                    if line.strip():
                        nonblank_lines += 1
                    else:
                        blank_lines += 1

            except (OSError, UnicodeDecodeError):
                print("Could not read:", path)

    print("\n===== PYTHON PROJECT STATISTICS =====")
    print("Python files:", file_count)
    print("Total lines:", total_lines)
    print("Nonblank lines:", nonblank_lines)
    print("Blank lines:", blank_lines)


folder = input("Enter project folder path: ").strip()

if os.path.isdir(folder):
    count_python_lines(folder)
else:
    print("Invalid folder path.")