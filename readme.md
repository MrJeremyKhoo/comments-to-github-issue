Progam to consolidate all todos in a codebase. It finds and lists the file paths and the comment in your cli or exports to a text file.

# Todo Scanner

Python script that scans code files in a specified directory for TODO comments and lists them. It supports multiple file extensions and offers the option to export the findings to a text file.

## How to download
```
$ git clone https://github.com/Agentum07/todo-scanner.git
$ cd todo-scanner
$ python todo_scanner.py
```
OR just download todo_scanner.py using your web-browser and run it.

## How to use
To run the script, simply run:
```
$ python todo_scanner.py
```
To see what options there are, run:
```
$ python todo_scanner.py -h
```
The options that are available are:
```
usage: todo_scanner.py [-h] [-d DIR] [-ext EXTENSIONS [EXTENSIONS ...]] [-e]

Scan code files for TODO comments

options:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     The directory to scan files in. Default: current directory.
  -ext EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                        File extensions to include in the scan. Default: ['.py', '.h', '.cpp', '.java', '.js']
  -e, --export          Export todo comments to a text file. Default: False
```

Sample run:
```
$ python todo_scanner.py -d my_project -ext .cpp -e
```
Explanation:
- Run the script in the directory `my_project`
- Only look for todos in files with extension `.cpp`
- export the todos to a text file

A new text file `my_project.txt` will be created in your directory.

## Demo
