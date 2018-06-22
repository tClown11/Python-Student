'''
节点查找
'''
'''
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//[@id="q"]')
print(input_first, input_second, input_third)
browser.close()'''
#以上是通过id，css，xpath的方式获取同一个属性值的方法
'''
所有获取单节点的方法
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector'''
#另外selenium通用查找单节点的方法
#find_element(查找方式(必须以大写字母表示), 值)



'''查找多个节点'''
'''
运用的是   find_elements()这样的方法'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
browser.close()'''