
import requests

name = input("Naam: ")
response = requests.get(
    url = f"https://api.agify.io?name={name}",
    params ={"name": name}
)
if response.status_code == 200:
    data = response.json()
    print(data["age"])
else:
    print(f"error{response.status_code}")
