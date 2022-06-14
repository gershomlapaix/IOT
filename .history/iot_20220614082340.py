import requests

url = 'http://insecure.benax.rw/iot'
requestData = {
    'device':'x-device',
    'distance':"25cm"
}

response = requests.post(url, json=requestData)