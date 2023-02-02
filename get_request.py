import requests

r = requests.get('http://localhost:8080/time.html')

print(r.text)