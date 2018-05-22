from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
#将文本改成html的形式
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
#若是没用contains，将会无法匹配
result_1 = html.xpath('//li[@calss, "li"]/a/text()')
print(result_1)


#多属性匹配
result_2 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result_2)
#(@class， "li")是多值匹配，所以在不是多值的情况下是没有小括号的