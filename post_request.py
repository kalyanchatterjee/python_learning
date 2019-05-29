import requests
import json

payload = dict(posse=["-aa", "-A", "-ÄÄÄ"])
json_payload = json.dumps(payload)

r = requests.post("http://httpbin.org/post", json_payload)

# print(r.status_code)
# print(r._content)
# print(r.raw)
# print(r.headers)

content = r._content.decode("utf-8")

content_dict = json.loads(content)

print(content_dict["data"])
