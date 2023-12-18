import json
import requests
def prompt_request(question):
    url = 'http://127.0.0.1:5000/prompt'
    headers = {'Content-Type': 'application/json'}
    data = {'prompt': question}
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data) # timeout=30
    return response

