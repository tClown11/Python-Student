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
result = html.xpath('//li[1]/a/text()')     #选取第一个li节点，中括号传入数字1即可。注意：这里和代码中不同，序号是以1开头，不是0开头
print(result)
result = html.xpath('//li[last()]/a/text()')        #选取最后一个li节点，中括号中传入last（）即可
print(result)
result = html.xpath('//li[position()<3]/a/text()')    #选取位置小于3的li节点
print(result)
result = html.xpath('//li[last()-2]/a/text()')      #选取倒数第三个li节点，中括号中传入last（）-2即可
print(result)