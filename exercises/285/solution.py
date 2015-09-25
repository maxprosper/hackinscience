import requests
try:
    r = requests.get("http://mdk.fr/ip")
    z = r.text
    d = z.split('\n', 1)[0]
    print(d)
except ConnectionError:
    print("No internet connectivity.")
