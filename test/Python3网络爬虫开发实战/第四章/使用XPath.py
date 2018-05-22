from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
 '''

html = etree.HTML(text)
result = etree.tostring(html)
#print(result.decode('utf-8'))
#可以看到经过处理后，li节点标签被补全，并且自动添加了body、html节点
#也可以直接读取文本进行解析

html = etree.parse('./text.html', etree.HTMLParser())
result_1 = etree.tostring(html)
print(result_1.decode('utf-8'))