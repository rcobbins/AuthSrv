import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

aam_url = "https://components.cyberarkdemo.com/AIMWebService/api/Accounts"
app_id = "AAMTest"
safe = "AAMTest"
key_object = "JSONList"

server_url = "http://localhost:5000/AuthAPIKey"

response = requests.get(aam_url + "?AppId=" + app_id + "&Safe=" + safe + "&Object=" + key_object, verify=False)

secrets = json.loads(response.json()['Content'])['secrets']

for secret in secrets:
    print("Authenticating with API Key: " + secret)
    response = requests.post(server_url, data=secret)
    if response.status_code == requests.codes.ok:
        print(response.json()['message'])
        print("Returned with new session token: " + response.json()['session_token'])
    else:
        print(response.json()['message'])
    print("\n\n\n")
