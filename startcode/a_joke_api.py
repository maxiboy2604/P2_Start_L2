import requests

request = requests.get('https://official-joke-api.appspot.com/random_joke')
if request.status_code == 200:
    print(request.text)
else:
    print(f"Er is iets foutgelopen{request.status_code}")