
import requests

response = requests.get('https://bored.api.lewagon.com//api/activity?type=recreational')
if response.status_code == 200:
    data = response.json()
    print(data['activity'])
else:
    print(f"Er is iets foutgelopen {response.status_code}")