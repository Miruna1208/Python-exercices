import requests
from datetime import datetime

TOKEN = "sjnodihwefncow2"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": "miruna",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/miruna/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
pixel_endpoint = f"{pixela_endpoint}/miruna/graphs/graph1"
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)


