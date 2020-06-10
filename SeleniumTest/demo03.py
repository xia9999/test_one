from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('http://132.232.44.158:8080/ljindex/')
driver.find_element_by_link_text('注册').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys('xhq123')
driver.find_element_by_xpath('//*[@id="phonenum"]').send_keys('15141452852')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456789')
driver.find_element_by_xpath('//*[@id="confirpw"]').send_keys('123456789')
driver.find_element_by_xpath('//*[@id="emailnum"]').send_keys('mmm@qq.com')
driver.find_element_by_xpath('//*[@id="userRegist"]').click()
time.sleep(2)
#获取alert警告对话框
alert = driver.switch_to_alert()
#打印对话框内容
print(alert.text)
#接受对话框，点击确认
alert.accept()
time.sleep(2)
assert driver.title == '登录'
