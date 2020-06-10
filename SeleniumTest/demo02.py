from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()  #网页最大化
driver.get('http://132.232.44.158:8080/ljindex/')
time.sleep(3)   #等待3秒
driver.find_element_by_link_text('登录').click()
time.sleep(3)
driver.find_element_by_id('username').send_keys('anran')
driver.find_element_by_id('password').send_keys('123456789')
driver.find_element_by_id('userLogin').click()
time.sleep(3)
assert driver.current_url == "http://132.232.44.158:8080/ljindex/"   #判断是否登录成功
print('成功了')