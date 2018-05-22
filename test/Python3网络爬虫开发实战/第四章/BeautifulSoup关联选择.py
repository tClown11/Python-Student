html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
#同样可以调用chilrden属性得到相应的结果
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
#children是直接子节点，用descendants可以得到子孙节点
#父节点是parent，，祖先节点是parents
#兄弟节点：下一个兄弟节点next_siblings，，，，上一个兄弟节点previous_siblings




#find_all()
#API:       find_all(name, attrs, recursive, text, **kwargs)
#name
#我们可以根据节点名来查询元素


#attrs
#根据属性查询,参数的类型是字典类型(例：attrs={})



#text
#text 参数可以用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))
#在这里有两个 a 节点，其内部包含有文本信息，在这里我们调用 find_all() 方法传入 text 参数，
# 参数为正则表达式对象，结果会返回所有匹配正则表达式的节点文本组成的列表



#find()
#除了 find_all() 方法，还有 find() 方法，只不过 find() 方法返回的是单个元素，也就是第一个匹配的元素，
# 而 find_all() 返回的是所有匹配的元素组成的列表

