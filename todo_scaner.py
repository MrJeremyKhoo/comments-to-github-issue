# iterate through all files
# find the todo comment
# support for .py
# .cpp
# .java for now

import re
import os

def export_to_txt():
    # write file name, line number.
    pass


def scan_todos(file):
    pattern = r"^(#\s*todo):\s*"
    for line_num, line in enumerate(file.readlines(), start=1):
        line = line.strip()
        line = line.lower()
        if (re.search(pattern, line)):
            tokens = list(filter(None, re.split(pattern, line)))
            print(tokens)
        # print(line_num, line)


def iterate(dir=os.getcwd(), extension="py"):
    # path = '/Users/a65888/Documents/UG_Study/Y3S2/CS3203/23s2-cp-spa-team-13/Team13/Code13/src/spa/src/PKB'
    for root, _, files in os.walk(dir):
      for file in files:
          if file.endswith(".py"):
              print(os.path.join(root, file))
              with open(file) as f:
                  scan_todos(f)

iterate()