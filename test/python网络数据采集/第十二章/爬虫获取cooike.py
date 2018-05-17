from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome(executable_path='C:\Program Files\Python36\Scripts/chromedriver.exe')
#driver.get("http://pythonscraping.com")
#driver.implicitly_wait(1)
#print(driver.get_cookies())
def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='C:\Program Files\Python36\Scripts/chromedriver.exe', chrome_options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()


