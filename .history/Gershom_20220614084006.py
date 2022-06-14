import requests

url = 'http://insecure.benax.rw/iot/'
requestData = {
    'device':'GershomNsengiyumva',
    'distance':"25cm"
}

response = requests.post(url, data=requestData)
print(response.text)