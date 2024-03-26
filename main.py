import requests
import os
import tkinter as tk

API_KEY = 'AIzaSyBQRouUTWLMvu1vdeD3r4Y0VMkT67FGPG4'
CSE_ID = '65762c42fe2ef4999'
user_input = input("Enter the query you want to search: ")
query = user_input

url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}'
response = requests.get(url)
data = response.json()

with open('output.txt', 'w') as f:
    for item in data.get('items', []):
        link = item.get('link')
        if link:
            f.write(link + '\n')
print('Done! The links have been saved in output.txt')
      