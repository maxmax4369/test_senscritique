import requests

url = 'http://localhost:5000/product/123'
data = {"title": "Babylon", "grade": "7.7", "type": "Comédie dramatique"}
x = requests.post(url, data=data)
print(x.text)