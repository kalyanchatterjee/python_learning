import requests

url = "https://enigmatic-plains-7414.herokuapp.com/"

r = requests.post(url, data=payload, headers=headers, stream=True)

for line in (r.raw.read_chunked()):
    print(line)

