#!/usr/bin/python3
""" Python script that fetches """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    headers = {'cfclearance': 'true'}
    response = requests.POST(url, headers=headers, data=data)
    print(response.headers.get("X-Request-Id"))
