# -*- coding: utf-8 -*-
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

#第一步是从文件读取XML
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
# 这段代码把一个远程Word文档读成一个二进制文件对象( BytesIO与本章之前用的StringIO 类似),
# 再用 Python 的标准库 zipfile 解压(所有的 .docx 文件为了节省空间都进行过压缩),
# 然后读取这个解压文件,就变成 XML
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
#print(xml_content.decode('utf-8'))

#正文包含在<w:t></w:t>标签中
wordObj = BeautifulSoup(xml_content.decode('utf-8'), "html.parser")
#print(wordObj)
textStrings = wordObj.findAll("w:t")
#print(textStrings)
for textElem in textStrings:
    print(textElem.text)