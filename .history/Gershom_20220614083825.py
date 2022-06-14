import requests

url = 'http://insecure.benax.rw/iot/'
requestData = {
    'device':'GershomNsengiyumva',
    'distance':"25cm"
}

response = requests.post(url, json=requestData)
print(response.text)