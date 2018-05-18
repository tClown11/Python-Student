from urllib import parse
from urllib import request

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
#bytes()传递两个参数，第一个必须是str类型，第二个参数是指定的编码格式
#传输了data这个参数后就不是get方式了，属于post方式
#传递的str参数出现在form字段中