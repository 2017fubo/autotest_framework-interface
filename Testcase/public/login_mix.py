#- * - coding:utf - 8 -*-
#
__author__ = 'fubo'
import sys, os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from rizhi import log_config as a
import logging
import time

class Login:

    def __init__(self,driver):
        ##全局中定义
        # self.username = "bo.fu  "
        # self.password = "fubo1234"
        self.driver = driver
        self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_添加域名.png"
        self.titleinfo = '供销大数据管理后台'

    def userinfo(username ="bo.fu",password ="fubo1234"):
        pass

        return username,password

    def login(self):###融合Boss 登录
        # log_msg = a.RiZhi()
        # log_info,log_debug,log_waring = log_msg.log_def()
        username,password = Login.userinfo()
        logging.info("%s,%s"%(username,password))
        # log_info("%s,%s"%(username,password))
        # log_debug("%s,%s"%(username,password))
        # log_waring("%s,%s"%(username,password))

        self.url = "http://pre-boss-cdn.sinobbd.com"
        try:
            logging.info('_login_')
            # print('_login_')
            self.driver.get(self.url)
            time.sleep(5)
            logging.info("输入用户名密码")
            # print('输入用户名密码')
            # self.driver.find_element_by_id("bdb-login-username").clear()
            self.driver.find_element_by_id("uname").send_keys('%s' % username)
            # 输入用户名
            # self.driver.find_element_by_id("bdb-login-pwd").clear()
            self.driver.find_element_by_id("password").send_keys('%s' % password)
            # 输入密码
            logging.info("点击登录！")
            self.driver.find_element_by_id("submit").click()
            self.driver.implicitly_wait(20)

        except Exception as e:
            print('登录失败-点击登录失败：%s' % e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            self.driver.close()
            sys.exit()

        # 账号登录
        # assert '域名列表' in self.driver.title
        title_info = self.driver.title
        print(title_info)
        if title_info == self.titleinfo or title_info == "sinobbd-boss":
            print('登录成功！')
            # 准备数据
        else:
            print('登录失败2-登录成功页面title验证不正确！')
            self.driver.get_screenshot_as_file(self.errorfile_path)
            self.driver.close()
            sys.exit()

        return self.driver