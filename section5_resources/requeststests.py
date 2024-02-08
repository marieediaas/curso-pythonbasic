import requests

r = requests.get("http://google.com")
#it will return 200 which means ok, it was found
#to see all status search http status codes
print("Status: ", r.status_code)
#gives the exact url
print(r.url)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)