import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'CHANGEME'
PASSWORD = 'CHANGEME'

# The repository to add this issue to
REPO_OWNER = 'CHANGEME'
REPO_NAME = 'CHANGEME'

def make_github_issue(json_obj):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.session(auth=(USERNAME, PASSWORD))
    # Create our issue
    issue = json_obj

    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print ('Could not create Issue "%s"' % title)
        print ('Response:', r.content)


def parse_todo_string(todo_string):
    """Parses a TODO comment string into a JSON issue format.

    Args:
        todo_string (str): The TODO comment string in the format 
                           "/path/to/file.py, line <line_number>: <task description>"

    Returns:
        dict: A dictionary representing the issue.
    """

    pattern = r"(?P<filepath>.+),\sline\s(?P<line_number>\d+):\s(?P<title>.+)"
    match = re.search(pattern, todo_string)

    if match:
        return {
            'title': match.group('title'),
            'body': match.group('filepath') + ', line ' + match.group('line_number'),
            'assignee': None,  # Use 'None' as a placeholder
            'milestone': None,
            'labels': []
        }
    else:
        return None

def main(string):
   make_github_issue(parse_todo_string(string))
    
if __name__ == "__main__":
    main(string);

