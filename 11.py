import json
import requests
from pprint import pprint
info = 0
with open('12pc.txt', 'w') as file_json:
    json.dump(info, file_json)
name = "kubernetes"
url = f"https://api.github.com/users/{name}"
data1 = requests.get(url).json()
pprint(data1)
c1 = json.dumps(data1)
pprint(c1)
user_data = json.loads(c1)
pprint(user_data)
info = {'company': (user_data["company"]),'created_at': (user_data["created_at"]),'email': (user_data["email"]),'id': (user_data["id"]),'name': (user_data["name"]),'url': (user_data["url"])}
pprint(info)
