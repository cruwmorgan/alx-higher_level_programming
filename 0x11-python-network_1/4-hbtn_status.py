#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from requests import get

if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    response = get(req)
    data = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(data), data)
    print(string)
