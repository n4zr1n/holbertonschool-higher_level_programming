#!/usr/bin/python3
""" POST request """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = ""
    response = requests.post(url, data=data)
    print(response.text)
