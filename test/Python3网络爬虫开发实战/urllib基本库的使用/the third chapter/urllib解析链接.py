#urlparse()
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)


#urlunparse()
from urllib.parse import urlunparse

data = ['http', 'www.daidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))


#urlspilt()
from urllib.parse import urlsplit

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result.scheme, result[0],result[1])

#urlunsplit()
from urllib.parse import urlunsplit

data = ['http', 'www.daidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunsplit(data))


