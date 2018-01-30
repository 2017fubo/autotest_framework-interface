##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

em_name= 'bo.fu'
em_ps = '111111'

webdriver = webdriver.Firefox()

webdriver.get("http://mail.126.com/")
print("1")
webdriver.switch_to.frame("x-URS-iframe")
print("2")
webdriver.find_element_by_name("email").send_keys("%s" %em_name)
print("3")
webdriver.find_element_by_name("password").send_keys("%s" %em_ps)
print("4")
webdriver.find_element_by_id("dologin").click()

webdriver.quit()