from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent' : 'Mozilla/4.0 (compatilble; MSIE 5.5; Windows NT)',
    'Host' : 'httpbin.org'
}
dict = {
    'name' : 'Clown'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
#另外,headers可以用add_header()方法来添加：
#req = request.Request(url, data=data, method='POST')
#req.request.add_header('User-Agent' : 'Mozilla/4.0 (compatilble; MSIE 5.5; Windows NT)')