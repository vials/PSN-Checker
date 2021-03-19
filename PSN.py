import requests

username = input("Enter Online ID: ")
response = requests.post('https://accounts.api.playstation.com/api/v1/accounts/onlineIds', json={"onlineId": username, "reserveIfAvailable": False})
if response.status_code == 400:
	print("{} is taken.".format(username))
elif response.status_code == 201:
	print("{} is available.".format(username))
else:
	print("[{}] - {}".format(response.status_code, response.text))
