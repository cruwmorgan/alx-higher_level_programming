#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        data = the_page.decode('utf-8')
        string = 'Body response:\n\t- type: {}\n\t- content: {}\n\t- \
                utf8 content: {}'.format(type(the_page), the_page, data)
        print(string)
