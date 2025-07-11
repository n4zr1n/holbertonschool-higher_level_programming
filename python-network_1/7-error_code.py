#!/usr/bin/python3
""" POST request """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    if response.status.code >= 400:
        print("Error code: ", response.status.code)
    else:
        print(response.text)
