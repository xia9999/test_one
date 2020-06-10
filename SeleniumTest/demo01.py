from selenium import webdriver  #导入selenium
#打开浏览器，driver浏览器的实例化把柄（浏览器把柄）
driver = webdriver.Chrome(executable_path='chromedriver.exe')
#访问百度
driver.get("https://www.baidu.com")
#通过id定位元素。driver.find_element_by_id("kw")输入框元素
#send_keys("吃啥"):输入内容的方法
# driver.find_element_by_id("kw").send_keys("吃啥")  #在输入框中输入想要搜索的内容
# driver.find_element_by_id("su").click()  #点击搜索按钮

#通过xpath定位元素
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("kk")

#通过name定位
# driver.find_element_by_name('wd').send_keys("nk")

#通过class定位
# driver.find_element_by_class_name('s_ipt').send_keys("ll")

#通过css selector定位
# driver.find_element_by_css_selector('#kw').send_keys("kk")

#通过超链接：文本值定位
# driver.find_element_by_link_text('抗击肺炎').click()

#通过超链接：文本值的一部分定位
# driver.find_element_by_partial_link_text('作弊').click()

#通过标签名tag_name定位
driver.find_element_by_tag_name().send_keys()