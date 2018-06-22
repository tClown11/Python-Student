import requests

proxy = '127.0.0.1:9743'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
#若需要认证，则代理前面加上用户名和密码
proxy = 'username:password@127.0.0.1:9743'


#如果需要使用SOCKS5代理
#在这里需要安装 requests[socks] 模块
import requests

proxy = '127.0.0.1:9743'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)


import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)