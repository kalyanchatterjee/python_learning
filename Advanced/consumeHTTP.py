# Consume data from HTTP stream https://enigmatic-plains-7414.herokuapp.com
import requests
r = requests.get('https://enigmatic-plains-7414.herokuapp.com', stream=True)

print(r.__dir__())

print(r.__sizeof__())


# r.encoding = "ISO-8859-1"
# print(dir(r))

# json_text = r.json()

# print(dir(json_text))

# print(json_text.__sizeof__)
# first_chunk = r.raw.read(300)
# first_chunk.decode("utf-8")

# print(first_chunk)
