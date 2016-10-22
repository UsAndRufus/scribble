import requests

api_key = str(open('api_key.txt').read())
url = 'https://speech.googleapis.com/v1beta1/speech:syncrecognize?key=' + api_key
print(url)

json = str(open('sync-request.json').read())
print(json)

response = requests.post(url, data=json, json=None)
print(response)
print(response.text)
