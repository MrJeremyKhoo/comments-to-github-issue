import todo_scanner
import github_issue
import sys
import json

def main(args):
    string = todo_scanner.main(args);
    github_issue.main(string);
    
if __name__ == "__main__":
    main(sys.argv);

