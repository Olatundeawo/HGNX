#!/usr/bin/env pthon3
""" Using the requests libray
"""
import requests

url = 'https://olatundeawo.pythonanywhere.com/api/4'

data = {'name': "Samson"}
response = requests.delete(url)

if response.status_code == 204:
    created_post = response.json()
    print(created_post)
else:
    print('Post request failed with status code {}'.format(response.status_code))