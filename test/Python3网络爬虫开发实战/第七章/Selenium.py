#获取商品列表
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq


#browser = webdriver.Chrome()    #首先构造了一个webdriver对象，使用的浏览器是Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)    #指定最长等待时间
KEYWORD = 'iphone7p'    #指定一个关键词

#定义一个方法，用于抓取商品列表页
def index_page(page):
    '''
    抓取索引页
    :param page:  页码
    :return:
    '''
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:   #判断当前页码
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )    #获取页码输入框，并赋值为input
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )    #获取“确定”按钮，并赋值为submit
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )     #将高亮的页码节点对应的CSS选择器和当前要跳转的页码通过参数传递给这个等待条件，这样它就会检测当前高亮的页码节点是不是
              # 我们传过来的页码数，如果是，就证明页面成功转到了这一页，页面跳转成功
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )     #选出页面内容中每个商品的信息块
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    '''
    提取商品数据
    :return:
    '''
    html = browser.page_source    #获取页码的源代码，然后构造了pyquery解析对象
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()   #提取商品列表，使用了CSS选择器，匹配整个网页的每个商品
    for item in items:  #因为匹配结果有多个，所以又对它进行一次遍历，提取每个商品的内容
        product = {
            'image': item.find('.pic .img').attr('data-src'),   #先用find()方法找到图片的节点，然后在调用attr()方法获取商品的data-src属性
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        #save_to_mongo(product)

#因为没有安装MongoDB，所以屏蔽
"""
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mongo(result):
    '''
    保存至MongoDB
    :param result: 结果
    :return: 
    '''
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')
"""

#遍历每页
MAX_PAGE = 100
def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    index_page(1)

if __name__ == "__main__":
    main()