# -*- coding:utf-8 -*-
import os
import re
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        urt = source[4:]
        url = "http://" + urt
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl, "")
    #出现  Invalid argument: 'downloaded/misc/jquery.js?v=1.4.4'
    #发现是src有问题，没有在代码中进行处理，这里第一个获取到的src的url是
    #http://pythonscraping.com/misc/jquery.js?v=1.4.4
    #实际文件应该是jquery.js，但是后面带了个版本号的小尾巴“?v=1.4.4”
    #所以在写入文件的时候出错。

   #解决方法及re.sub的用法
    #由于示例网站里面src的url不止一处带小尾巴，所以考虑用正则表达式进行替换。
    #网上随便搜到一个正则表达式替换字符串的示例:
    path = re.sub("\?.*","",path)  # 把问好开头的字符串都替换为空
    path = downloadDirectory + path
    #这个获取文件路径中所在的目录。
    directory = os.path.dirname(path)


    #exists()会自动判断失效的文件链接。如果检查的文件是一个软链接，但这个软连接指向的文件被删除了，会返回False。而lexists()不会做这个检查，只要软连接存在，即使它指向的文件不存在，也返回True。
    #当查询没有权限指向os.stat()时，exists()也会返回False。

    #linux?windows系统没有软连接。

    #一个文件有一个或多个硬链接，所有硬链接被删除后，文件会被删除。
    #一个文件有0个或多个软链接，所有软链接被删除后，文件不会被删除。

    #软链接有点像windows的快捷方式。
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))