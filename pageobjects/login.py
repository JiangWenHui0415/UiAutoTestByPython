import time
from selenium import webdriver
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.maximize_window()
#隐式等待
driver.implicitly_wait(8)
print("open website:")
driver.get("https://xxx.com")
print("login:")
driver.find_element_by_id('login').click()
print("clear phoneNo")
driver.find_element_by_id('phoneNo2').clear()
driver.find_element_by_id('phoneNo2').click()
print("input phone num")
driver.find_element_by_id('phoneNo2').send_keys('1111111111')
print("clear keys")
driver.find_element_by_id('password2').clear()
driver.find_element_by_id('password2').click()
print("input keys")
driver.find_element_by_id('password2').send_keys('123456')
print("click login")
driver.find_element_by_id('passwordLoginButton1').click()
driver.implicitly_wait(8)
print("click point")
driver.find_element_by_link_text("观点").click()
print("click input button")
#driver.find_element_by_xpath("//*[@href='/schemonitor/information-index.html']").click()
driver.implicitly_wait(10)
driver.find_element_by_class_name('ke-edit').click()
driver.find_element_by_class_name('ke-edit-iframe').send_keys("UIautoTest")
# driver.find_element_by_name("")
driver.find_element_by_id("shortFilePublish").click()
time.sleep(2)
#刷新页面
#driver.refresh()
#后退
#driver.back()
#前进
#driver.forward()
#关闭当前页面
#driver.close()
#获取浏览器版本         driver.capabilities['version']
#获取当前页面url        driver.current_url
#发送键盘按键 .send_keys(Keys.CONTROL + 't')   触发CTRL+T
#网页截图  driver.get_screenshot_as_file("C:\\Users\\你的账户名\\Desktop\\baidu.png")

#关闭浏览器
driver.quit()















