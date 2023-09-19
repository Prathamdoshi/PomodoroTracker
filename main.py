# ------------------------------ MODULES ------------------------------ #
import requests

# ------------------------------ USER AUTHENTICATION ------------------------------ #
account_endpoint = "https://pixe.la/v1/users"

param = {
    "username" : "prathamdoshi",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
    "token"  : "K7pT9w2xL6zY"
}

# commented once account is created
# account_response = requests.post(url=account_endpoint,json=param)


# ------------------------------ GRAPH CONFIGURATION ------------------------------ #


graph_endpoint = f"https://pixe.la/v1/users/{param['username']}/graphs"

header = {
    "X-USER-TOKEN"  : "K7pT9w2xL6zY",
}

graph_config = {
    "id" : "a5b-cd9e",
    "name": "Daily Pomodoro Tacker",
    "unit" : "commit",
    "type" : "int",
    "color" : "kuro"
}

# commented once graph is created
# graph_response = requests.post(url=graph_endpoint,json=graph_config,headers=header)

# ------------------------------ PIXEL POSTING ------------------------------ #
pixel_endpoint = f"https://pixe.la/v1/users/{param['username']}/graphs/{graph_config['id']}"

pixel_data = {
    "date" : "20230919",
    "quantity": "11"
}

pixel_response = requests.post(url=pixel_endpoint,headers=header,json=pixel_data)
print(pixel_response.text)