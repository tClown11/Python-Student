import urllib.request

request = urllib.request.Request('https://pyhton.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
#class urllib.request.Request(url, data=None, herders={}, origin_req_host=None, unverifiable=False, method=None)