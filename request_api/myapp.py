import requests
URL = "http://localhost:8080/stuinfo/1"
r = requests.get(url = URL)
data = r.json()
print(data)