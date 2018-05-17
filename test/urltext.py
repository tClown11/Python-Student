# -*- coding: UTF-8 -*-
from selenium import webdriver

brower = webdriver.PhantomJS()
brower.get('https://www.baidu.com')
print(brower.current_url)