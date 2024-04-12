import re
import os
import sys
import argparse
from collections import defaultdict

def export_to_txt(dir, todos):
    file_name = os.path.basename(dir)
    output_path = os.path.join(os.getcwd(), f"{file_name}.txt")

    with open(output_path, "w") as f:
        for file_path, todo_list in todos.items():
            for todo in todo_list:
                f.write(f"{file_path}, {todo}\n")

def print_to_cli(todos):
    for file_path, todo_list in todos.items():
        for todo in todo_list:
            print(f"{file_path}, {todo}")

def get_todos(file_paths):
    todos = defaultdict(list)
    todo_regex = re.compile(r'(?i)^\s*(?:#|\/\/|\/\*|\'\'\'|\"\"\")\s*TODO:\s*(.*?)$') 

    for file_path in file_paths:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file.readlines(), start=1):
                match = todo_regex.match(line)
                if match:
                    todo_text = match.group(1)
                    todos[file_path].append(f"line {line_num}: {todo_text}")
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
    default_extensions = [".py", ".h", ".cpp", ".java", ".js"]
    parser = argparse.ArgumentParser(description="Scan code files for TODO comments")
    parser.add_argument("-d", "--dir", help = "The directory to scan files in. Default: current directory.", required = False, default = os.getcwd())
    parser.add_argument("-ext", "--extensions", help = f"File extensions to include in the scan. Default: {default_extensions}", nargs="+", required = False, default = default_extensions)
    parser.add_argument("-e", "--export", help = "Export todo comments to a text file. Default: False", required = False, action="store_true", default=False)
    return parser

def main(args):
    parser = create_parser()
    
    parsed_args = parser.parse_args(args[1:])
    directory = parsed_args.dir
    extensions = parsed_args.extensions
    should_export = parsed_args.export

    file_paths = get_files(directory, extensions)
    todos = get_todos(file_paths)
    if should_export:
        export_to_txt(directory, todos)
    else:
        return todos

if __name__ == "__main__":
    main(sys.argv)
