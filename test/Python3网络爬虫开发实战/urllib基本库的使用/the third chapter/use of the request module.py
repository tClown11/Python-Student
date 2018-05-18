import urllib.request

request = urllib.request.Request('https://pyhton.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))