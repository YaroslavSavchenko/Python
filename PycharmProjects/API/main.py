import requests
params = {'response_type':'token', 'client_id':'5e9a9b55952b4f7c94d78d1f30e26912'}
req = requests.get('https://oauth.yandex.ru/authorize?',params=params)

print(req)


#headers = {'user-agent': 'my-agent/1.0.1'}
#response = requests.get('http://httpbin.org/', headers=headers)
#print(response.headers)