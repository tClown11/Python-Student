#访问页面
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

#查找节点
#1、单个节点
#from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_thrid = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_thrid)
browser.close()
#通用方法:公式
input_four = browser.find_element(By.ID, id)

#多个节点
#from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_element_by_css_selector('.service-bd li')
print(lis)
browser.close()

#节点交互
#from selenium import webdriver
#import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()