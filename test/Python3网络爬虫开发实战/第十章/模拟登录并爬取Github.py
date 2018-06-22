import requests
from lxml import etree


#初始化变量
class Login(object):
    def __init__(self):
        self.headers = {
            'Rdferer': 'https://github.com/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/setting/profile'
        self.session = requests.Session()   #requests库的Session，可以维持会话，自动处理cookies，相当于cookies值已被获取


#用session对象的get()方法访问github的登录界面，然后用XPath解析出登录所需的authenticity_token信息并返回
    def token(self):
        response = self.session.get(self.login_url, hearders=self.hearders)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div/input[2]/@value')[0]   #选取出authenticity_token
        return token


    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'login': email,
            'password': password
        }

        response = self.session.get(self.logined_url, data=post_data, headers= self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)


    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamics = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamics)


    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="User_profile_email"]/option[@value!=""]/text()')
        print(name, email)


if __name__ == "__main__":
    login = Login()
    login.login(email='tj1211keynote@outlook.com', password='tj12110896')