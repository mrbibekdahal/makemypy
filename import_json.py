import json

x =  '{ "name":"Rajesh", "age":24, "city":"tokyo"}'
y = json.loads(x)
print(y["city"])