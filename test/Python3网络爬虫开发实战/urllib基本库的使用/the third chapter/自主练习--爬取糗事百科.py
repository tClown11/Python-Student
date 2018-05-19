import requests
import re
import time


#访问网页
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


#爬取网页上的数据
def parse_one_page(html):
    #<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>
    #通过正则表达式选取出所需的内容
    pattern = re.compile('<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern, html)
    #print(items)
    #对爬取的数据进行处理
    for item in items:
        yield {
         item[0].strip(): item[1].strip()
        }

#写入文本
def write_to_file(context):
    with open('result_1.txt', 'a', encoding='utf-8') as f:
        #print(type(json.dumps(context)))
        #f.write(json.dumps(context, ensure_ascii=False)+ '\n')
        f.write(str(context)+ '\n')

def main(offset):
    url = 'https://www.qiushibaike.com/8hr/page/'+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
    #print(html)

if __name__ == "__main__":
    for i in range(10):
        main(offset=i)
        time.sleep(2)