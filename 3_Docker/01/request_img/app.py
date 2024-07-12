import requests

response = requests.get('https://api.github.com/')

print(response.json())
