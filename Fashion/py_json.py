import json

username='{"first_name":"Kartik","last_name":"Saurya",age":19}'
user=json.loads(username)
print(user)