#- * - coding:utf - 8 -*-
#
__author__ = 'fubo'
import sys, os
class Exitlogin:

    def __init__(self,driver):
        self.Driver = driver

    def exitlogin(self):
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraTop")
            print('退出登录-注销')
            self.Driver.find_element_by_xpath("/html/body/form/div/ul/li[1]/a").click()
            print('注销成功！')
        except:
            self.Driver.get_screenshot_as_file("E:\9F\error.png")
            print('注销失败')
