import requests

print("requests version:", requests.__version__)
print("response for GET 'http://www.google.com/':",
      requests.get("http://www.google.com/"))
print("\nlab 1 python script source code:\n```\n" + 
      requests.get("https://raw.githubusercontent.com" +
                   "/aakindel/404_lab_1/master/lab1.py").text + "```")
