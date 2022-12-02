from selenium import webdriver
from PIL import Image
import requests
import time
from bs4 import BeautifulSoup
class loginschool:
    username = input('account:')
    password = input('password:')
    browser = webdriver.Chrome()
    browser.get('http://ids.chd.edu.cn/authserver/login?service=http%3A%2F%2Fportal.chd.edu.cn%2F')
    input_name = browser.find_element_by_name('username')
    input_name.send_keys(username)
    # input_element.submit()
    input_password = browser.find_element_by_id('password')
    input_password.send_keys(password)
    browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
    browser.find_element_by_xpath('//*[@id="pf1299"]/div/div[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[2]/td/a').click()
    time.sleep(6)
    browser.find_element_by_xpath('//div[@class="scroll_box"]//li/a[1]').click()
    time.sleep(4)  # 加入这一步。。是浏览器反应不过来,得到反应信息。
    # browser.switch_to.frame('iframeResult')
    print(browser.page_source)

