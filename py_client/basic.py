import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"


get_reponse = requests.get(endpoint, json={"query": "Hello world"})
# print(get_reponse.text)
# print(get_reponse.status_code)



print(get_reponse.json())
# print(get_reponse.status_code)