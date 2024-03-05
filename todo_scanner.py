# iterate through all files
# find the todo comment
# support for .py
# .cpp
# .java for now

import re
import os
from collections import defaultdict
def export_to_txt():
    # write file name, line number.
    pass


def get_todos(file_paths, pattern):
    todos = defaultdict(list)
    for file_path in file_paths:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file.readlines(), start=1):
                line = line.strip()
                line = line.lower()
                if (pattern.search(line)):
                    tokens = list(filter(None, pattern.split(line)))
                    # print(f"{file_path}, line {line_num}: {tokens[1]}")
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


def main():
    pattern = re.compile(r"^(#\s*todo):\s*")
    file_paths = get_files()
    todos = get_todos(file_paths, pattern)
    print(todos)

main()