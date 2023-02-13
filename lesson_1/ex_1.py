import json
import requests


url = 'https://api.github.com'
user = 'VaLeraSi'

repos = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(repos.json(), f)

for i in repos.json():
    print(i['name'])