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


def print_to_cli(todos):
    for file_path, todo_list in todos.items():
        for todo in todo_list:
            print(f"{file_path}, {todo}")

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


def create_parser():
    default_extensions = ["py", "h", "cpp", "java", "js"]
    parser = argparse.ArgumentParser(description="Scan code files for TODO comments")
    parser.add_argument("-d", "--dir", help = "The directory to scan files in. Default: current directory.", required = False, default = os.getcwd())
    parser.add_argument("-ext", "--extensions", help = f"File extensions to include in the scan. Default: {default_extensions}", nargs="+", required = False, default = default_extensions)
    parser.add_argument("-e", "--export", help = "Export todo comments to a text file. Default: False", required = False, action="store_true", default=False)
    return parser

def main(args):
    pattern = re.compile(r"^(#\s*todo):\s*")
    parser = create_parser()
    
    parsed_args = parser.parse_args(args[1:])
    directory = parsed_args.dir
    extensions = parsed_args.extensions
    should_export = parsed_args.export

    extensions = [f".{ext}" for ext in extensions]
    file_paths = get_files(directory, extensions)
    todos = get_todos(file_paths, pattern)
    if should_export:
        export_to_txt(directory, todos)
    else:
        print_to_cli(todos)

if __name__ == "__main__":
    main(sys.argv)