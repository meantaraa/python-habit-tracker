import requests
from datetime import datetime

#code to create a user

USERNAME="a-young"
TOKEN="Iwillnottellyou"
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

#code to create a graph

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#code to perform post operation

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixela_creation_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y-%m-%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),

}

response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "8.4"
}

#code to perform put operation

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

#code to perform delete operation

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.delete(url= delete_endpoint, headers=headers)
print(response.text)
