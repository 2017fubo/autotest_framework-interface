##coding:utf-8 融合boss
import time,traceback,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from rizhi import log_config as a
import logging
from Testcase.public import login_mix


class boss_mix_customer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        log_msg = a.RiZhi()
        log_msg.log_def()
        logging.info("Start Test")
        # print('Test start')
        self.driver = webdriver.Firefox()
        self.login_temp = login_mix.Login(self.driver)
        # logging.debug("sss:%s"%self.login_temp)
        self.Driver = self.login_temp.login()
        self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_添加域名.png"


    def test_add_customer_view(self):
        # log_msg = a.RiZhi()
        # log_msg.log_def()
        logging.info("添加客户菜单项目验证")

        return

    def test_customer_verify(self):
        pass
        logging.info("执行test_customer_verify ")

        return

    @classmethod
    def tearDownClass(self):
        driver = self.driver
        driver.quit()

if __name__ == '__main__':
    unittest.main()