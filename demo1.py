import requests
url="http://api.open-notify.org/astros.json"

response=requests.get(url).json()

print (response["number"])
