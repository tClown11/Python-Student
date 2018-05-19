#代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_hander = ProxyHandler({
    'http' : 'http://127.0.0.1:9743',
    'http' : 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_hander)
try:
    response = opener.open('https://www/baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

#Cookies
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+ "="+item.value)