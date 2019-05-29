import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

x_json = json.dumps(x)

print(type(x_json))

print(x_json)

x_dict = json.loads(x_json)

print(type(x_dict))

print(x_dict["cars"])
