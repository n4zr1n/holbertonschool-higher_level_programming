#!/usr/bin/python3
""" Python script that fetches """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.POST(url, data=data)
    print(response.headers.get("X-Request-Id"))
