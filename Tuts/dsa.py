import requests
url = 'http://127.0.0.1:8000/create'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

# print(x.text)