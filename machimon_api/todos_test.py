import requests
import random

params = {"task": "fuck my gf"}

for i in range(10):
    body = {"value": random.random()}

    r = requests.post("http://127.0.0.1:5000/todos", json=body)
    print(r.status_code)
