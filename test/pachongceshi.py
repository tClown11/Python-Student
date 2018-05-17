from urllib import request
if __name__ == "__main__":

    kw = input("请输入需要爬取的贴吧：")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})

    #组合后的url示例：
    url = url + key
    tiebaSpider(url, beginPage, endPage)


def tiebaSpider(url, beginPage, endPage):
    """
    作用：负责处理url，分配每个url去送发请求
    url: 需要处理的第一个url
    beginPage: 爬虫执行的起始页
    endPage:  爬虫执行的截止页面
    """

    for page in range(beginPage, endPage + 1):
        pn = (page - 1)* 50

        filename = "第" + str(page) + "页.html"
        #组合为完整的url,并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        #print(fullurl)

        #调用loadPage（）发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        #将获取到的HTML页面写入本地磁盘文件
        #witeFile(html, filename)

def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    url:需要爬取的url地址
    filename:文件名
    """
    print("正在下载" + filename)

    headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = request.urlopen(url, headers = headers)
    response = request.text
    return response

#def witeFile(html, filename):
    """
    作用：保存服务器响应文件到本地磁盘文件里
    html: 服务器响应文件
    filename:  本地磁盘文件名
    """