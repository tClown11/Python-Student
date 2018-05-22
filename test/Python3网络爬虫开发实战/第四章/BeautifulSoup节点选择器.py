html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
print("-"*50)
#提取名称
print(soup.title.name)
print('-'*50)


#获取属性
print(soup.p.attrs)     #调用 attrs 获取所有属性。
print(soup.p.attrs['name'])
#可以看到 attrs 的返回结果是字典形式，把选择的节点的所有属性和属性值组合成一个字典，接下来如果要获取 name 属性，
# 就相当于从字典中获取某个键值，只需要用中括号加属性名称就可以得到结果了，比如获取 name 属性就可以通过 attrs['name'] 得到相应的属性值。

#更简单的获取方式，我们可以不用写 attrs，直接节点元素后面加中括号，传入属性名就可以达到属性值了
print(soup.p['name'])
print(soup.p['class'])
#在这里注意到有的返回结果是字符串，有的返回结果是字符串组成的列表
#属性的值是唯一的，返回的结果就是单个字符串
#而对于 class，一个节点元素可能由多个 class，所以返回的是列表，所以在实际处理过程中要注意判断类型


#获取内容
#可以利用 string 属性获取节点元素包含的文本内容，比如上面的文本我们获取第一个 p 节点的文本：
print(soup.p.string)
#再次注意一下这里选择到的 p 节点是第一个 p 节点，获取的文本也就是第一个 p 节点里面的文本。


#嵌套选择
html_1 =  """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup_1 = BeautifulSoup(html, 'lxml')
print(soup_1.head.title)
print(type(soup_1.head.title))
print(soup_1.head.title.string)