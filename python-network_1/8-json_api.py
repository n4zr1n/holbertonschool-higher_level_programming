#!/usr/bin/python3
""" Search API """
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("f[{}] {}".format(json_data.Id, json_data.__name__))
        else:
            print("No result")
    except ValueError:
        print("The response body is not properly JSON formatted")
