import urllib.request
import json
url ="http://api.open-notify.org/astros.json"

#send get request
response=urllib.request.urlopen(url)
print (response)
response=response.read()

print(type(response))

