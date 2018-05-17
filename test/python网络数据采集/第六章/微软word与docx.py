# -*- coding: utf-8 -*-
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

#第一步是从文件读取XML
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
#这段代码吧一个远程Word文档读成一个二进制文件对象（BytesIO与文章之前用的SrtingIO类似），
#再用Python的标准库zipFile解压（所有的.docx文件为了节省空间都进行过压缩），
#然后读取这个解压文件，就变成 XML
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))