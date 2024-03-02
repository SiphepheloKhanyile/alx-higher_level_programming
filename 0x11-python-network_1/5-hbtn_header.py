#!/usr/bin/python3
"""
Module for a script that takes in a URL,
sends a request to the URL
And displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url, timeout=None)
    print(response.headers['X-Request-Id'])
