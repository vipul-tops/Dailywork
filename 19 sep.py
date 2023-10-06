import json

x='{"Name":"Vipul","Age":25,"City":"Sanand"}'

y= json.loads(x)

print(y["Age"])
print(y["Name"])
print(y["City"])

print("-"*40)


a = {
    "Name": "Vipul",
    "Age": 25,
    "City": "Sanand"
}

y = json.dumps(a)

print(y)

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)
