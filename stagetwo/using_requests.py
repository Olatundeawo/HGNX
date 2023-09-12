#!/usr/bin/env pthon3
""" Using the requests libray
"""
import requests

url = 'https://olatundeawo.pythonanywhere.com/api'

data = {
    4: {"name": "Tunde"}
}
response = requests.post(url, json=data)

if response.status_code == 201:
    created_post = response.json()
    print(created_post)
else:
    print('Post request failed with status code {}'.format(response.status_code))