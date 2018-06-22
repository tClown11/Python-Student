from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')#找到输入框
input.send_keys('iphone')
time.sleep(2)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')#找到搜索的按钮
button.click()#点击

'''
动作链：实现一个节点的拖拽操作等
from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#drappable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

对于一些Selenium API没有提供的操作方法， 我们可以通过execute_script()方法直接模拟Javascript来运行
from selenium import webdriver
browser = webdriver.Chorme()
browser.get('https://www.zhihu.com/ex
'''