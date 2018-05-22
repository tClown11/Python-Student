#父节点

from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

#也可以用parent：：获取父节点
result_2 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result_2)

#属性匹配
result_1 = html.xpath('//li[@class="item-0"]')
print(result_1)

#文本获取
result_3 = html.xpath('//li[@class="item-0"]/text()')
print(result_3)
#想获取li节点内部的文本，就有两种方式：1、是先选取a节点再获取文本。  2、用//
#1、
result_4 = html.xpath('//li[@class="item-0"]/a/text()')
print(result_4)
#2、
result_5 = html.xpath('//li[@class="item-0"]//text()')
print(result_5)


#属性获取(!=属性匹配)       属性匹配是中括号加属性名和值来限定某个属性，如：[@href="link.html"]，而此处的@href指的是获取节点的某个属性
result_6 = html.xpath('//li/a/@href')
print(result_6)

