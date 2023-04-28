#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    owner = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = get(url)
    try:
        objects = response.json()
        for i, obj in enumerate(objects):
            print('{}: {}'.format(obj.get('sha'),
                                  obj.get('commit').get('author')
                                  .get('name')))
            if i == 9:
                break
    except ValueError:
        pass
