import requests
import json
url = 'https://jsonplaceholder.typicode.com/todos/1'
resp = requests.get(url)
sd_dict = resp.json()
user_id = sd_dict['userId'] 
print(user_id)
print(sd_dict)