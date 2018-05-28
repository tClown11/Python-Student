import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


#组装url，并且建立连接（需要捕获链接失败的异常）
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

#实现解析方法
def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield{
                    'image': image.get('url'),
                    'title': title
                }


#实现保存图片的方法
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        print(local_image_url)
        new_image_url = local_image_url.replace('list', 'large')
        print(new_image_url)
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


#构造一个offset数组，遍历offset，提取图片链接，并将其下载
def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == "__main__":
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()