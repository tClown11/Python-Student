from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

#可以匹配指定节点名称
result_1 = html.xpath('//li')
print(result_1)
print(result_1[0])