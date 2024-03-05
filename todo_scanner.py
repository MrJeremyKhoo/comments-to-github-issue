# iterate through all files
# find the todo comment
# support for .py - done
# .cpp
# .java for now

import re
import os
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


def get_files(dir=os.getcwd(), extension="py"):
    dir = "/Users/a65888/Desktop/todo-summarizer"
    res = set()
    for root, _, files in os.walk(dir):
      for file in files:
          if file.endswith(".py"):
              file_path = os.path.join(root, file)
              res.add(file_path)
    return res


def main(export=True):
    pattern = re.compile(r"^(#\s*todo):\s*")
    file_paths = get_files()
    todos = get_todos(file_paths, pattern)
    if export:
        export_to_txt(os.getcwd(), todos)

main()