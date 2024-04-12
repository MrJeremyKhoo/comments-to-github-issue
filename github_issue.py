import json
import requests
import re

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'MrJeremyKhoo'
token = ''

# The repository to add this issue to
REPO_OWNER = 'Agentum07'
REPO_NAME = 'todo-scanner'

# todo: do not make duplicate issues
def make_github_issue(json_obj):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    headers = {"Authorization": "token {}".format(token)}

    issue = json_obj

    # Add the issue to our repository
    response = requests.post(url, data=json.dumps(issue), headers=headers)

    if response.status_code == 201:
        print('Successfully created Issue "%s"' % issue['title'])
    else:
        print('Could not create Issue "%s"' % issue['title'])
        print('Status Code:', response.status_code)
        print('Response:', response.content)

def parse_todo_string(todo_string):
    pattern = r"^(?P<filepath>.*: line \d+):(?P<title>.*)"
    match = re.search(pattern, todo_string)

    if match:
        return {
            'title': match.group('title'),
            'body': match.group('filepath'),
            'assignee': None,  # Use 'None' as a placeholder
            'milestone': None,
            'labels': []
        }
    else:
        return None
#todo: dont call make_github_issue too quickly if too many items
def main(input_dict):
    for file_path, todos_list in input_dict.items():
        for todo_text in todos_list:
            concatenated_string = f"{file_path}: {todo_text}"  # Concatenate file_path with todo_text
            json_obj = parse_todo_string(concatenated_string)
            make_github_issue(json_obj)
    
if __name__ == "__main__":
    main(string);

