import requests
import json

url = 'http://127.0.0.1:5000/prompt'
headers = {'Content-Type': 'application/json'}
data = {'prompt': 'Hej, vad är budgeten?'}
json_data = json.dumps(data)
response = requests.post(url, headers=headers, data=json_data)

print(response.status_code)
print(response.json())
