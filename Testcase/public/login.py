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
        self.username = "bo.fu  "
        self.password = "fubo1234"
        self.driver = driver
        self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_添加域名.png"
        self.titleinfo = '供销大数据管理后台'


    def userinfo(self):
        self.data = {"username":"bo.fu","password":"fubo1234"}

        return self.data

    def login(self):###自建Boss
        log_msg = a.RiZhi()
        log_msg.log_def()
        userinfo_temp = self.data

        username,password = userinfo_temp.items()
        #password = 'fubo1234'
        # url = "http://bbd.boss.com:88/AdminUser/login"
        logging.info(username,password)

        self.url = "http://test-boss.bbdcdn.net/AdminUser/login"
        ##全局中定义
        try:
            logging.info('_login_')
            # print('_login_')
            self.driver.get(self.url)
            time.sleep(5)
            logging.info("输入用户名密码")
            # print('输入用户名密码')
            # self.driver.find_element_by_id("bdb-login-username").clear()
            self.driver.find_element_by_id("bdb-login-username").send_keys('%s' % username)
            # 输入用户名
            # self.driver.find_element_by_id("bdb-login-pwd").clear()
            self.driver.find_element_by_id("bdb-login-pwd").send_keys('%s' % password)
            # 输入密码
            print('点击登陆')
            self.driver.find_element_by_id("bdb-login-btn").click()
            self.driver.implicitly_wait(20)
        except Exception as e:
            print('登录失败-点击登录失败！%s' % e)
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