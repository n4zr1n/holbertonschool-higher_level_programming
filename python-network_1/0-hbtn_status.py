#!/usr/bin/python3
""" a function that fetches a URL """


import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
