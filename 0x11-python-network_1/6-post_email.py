#!/usr/bin/python3
""" Script takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response."""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)
    print(req.text)
