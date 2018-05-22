from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

#获取所有子孙节点
result_1 = html.xpath('//ul//a')
print(result_1)