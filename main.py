import requests
import datetime as dt
import os

pixela_endpoint = "https://pixe.la/v1/users"
username = os.environ["username"]
token = os.environ["token"]
graph_id = os.environ["graph_id"]

parameter = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_conf = {
    "id": graph_id,
    "name": "books reading",
    "unit": "views",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
today = dt.datetime.now()
post_a_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages do you read today? "),
}

response = requests.post(url=pixel_endpoint, json=post_a_pixel, headers=headers)
print(response.text)

put_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

put_conf = {
    "quantity": "10"
}

# resource = requests.put(url=put_pixel_endpoint, json=put_conf, headers=headers)
# print(resource.text)

delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
