import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read())
    #可以通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过他的抓取
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
#除了data参数和timeout参数外，还有context参数，它必须是ssl.SSLContext类型，用来指定SSL设置