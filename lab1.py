import requests

print("requests version:", requests.__version__)
print("response for GET 'http://www.google.com/':",
      requests.get("http://www.google.com/"))
