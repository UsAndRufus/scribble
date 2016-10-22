import requests

headers = {
    'Content-Type': 'application/json',
}

data = open('sync-request.json')
data_str = str(data.read())
print(data_str)

api_key = open('api_key.txt')
api_key_str = str(api_key.read())
print(api_key_str)

url = 'https://speech.googleapis.com/v1beta1/speech:syncrecognize?key=' + api_key_str
print(url)

r = requests.post(url,headers=headers, data=data, verify=False)

print(r)
print(r.text)
print(r.json())
