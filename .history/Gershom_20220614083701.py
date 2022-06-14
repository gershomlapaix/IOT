import requests

url = 'http://insecure.benax.rw/iot/'
requestData = {
    'device':'Gersh-device',
    'distance':"25cm"
}

response = requests.post(url, json=requestData)