# iterate through all files
# find the todo comment
# support for .py - done
# .cpp
# .java for now

import re
import os
import sys
import argparse
from collections import defaultdict

def export_to_txt(dir, todos):
    file_name = os.path.basename(dir)
    output_path = os.path.join(dir, f"{file_name}.txt")

    with open(output_path, "w") as f:
        for file_path, todo_list in todos.items():
            for todo in todo_list:
                f.write(f"{file_path}, {todo}\n")


def get_todos(file_paths, pattern):
    todos = defaultdict(list)
    for file_path in file_paths:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file.readlines(), start=1):
                line = line.strip()
                line = line.lower()
                if (pattern.search(line)):
                    tokens = list(filter(None, pattern.split(line)))
                    todos[file_path].append(f"line {line_num}: {tokens[1]}")
    return todos


def get_files(dir, extensions):
    res = set()
    for root, _, files in os.walk(dir):
      for file in files:
          if os.path.splitext(file)[1] in extensions:
              file_path = os.path.join(root, file)
              res.add(file_path)
    return res


def main(args):
    parser = argparse.ArgumentParser(description="Scan code files for TODO comments")
    parser.add_argument("-d", "--dir", help = "The directory to scan files in, current directory by default.", required = False, default = os.getcwd())
    parser.add_argument("-ext", "--extensions", help = "File extensions to include in the scan.", nargs="+", required = False, default = [".py", ".h", ".cpp", ".java", ".js"])
    parser.add_argument("-e", "--export", help = "Export todo comments to a text file.", required = False, action="store_true", default=True)
    print(args)
    parsed_args = parser.parse_args(args[1:])
    directory = parsed_args.dir
    extensions = parsed_args.extensions
    should_export = parsed_args.export

    print(parsed_args)
    pattern = re.compile(r"^(#\s*todo):\s*")
    file_paths = get_files(directory, extensions)
    todos = get_todos(file_paths, pattern)
    if should_export:
        export_to_txt(os.getcwd(), todos)

if __name__ == "__main__":
    main(sys.argv)