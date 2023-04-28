#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
