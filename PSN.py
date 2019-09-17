import requests

username = input("Enter Online ID: ")
try:
	response = requests.post('https://accounts.api.playstation.com/api/v1/accounts/onlineIds', json={"onlineId": username, "reserveIfAvailable": False})
except Exception as e:
	print(str(e))
	pass
if response.status_code == 400:
	print("Username: ["+username+"] Taken")
elif response.status_code == 201:
	print("Username: ["+username+"] Available")
else:
	print(response.status_code)
	print(response.content)
