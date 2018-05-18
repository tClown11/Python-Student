#import urllib.request
from urllib import request

response = request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
#利用type（）方法输出响应的类型
print(type(response))

print('-'*50)
#调用read（）方法可以得到返回的网页内容，调用status属性可以得到返回结果的状态码
response_1 = request.urlopen('http://www.python.org')
print(response_1.status)
print(response_1.getheaders())
print(response_1.getheader('Server'))