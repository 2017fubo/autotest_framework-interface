##coding:utf-8 融合boss

import urllib
import re
#import jieba
import unittest
from rizhi import log_config as a
import logging

class Reptile(unittest.TestCase):

    def __init__(self,driver):
        self.Driver = driver
        self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_添加域名.png"

    def test_add_customer_view(self):
        log_msg = a.RiZhi()
        log_msg.log_def()
        # logging.info("添加客户菜单项目验证")
        url = "http://boss.sinobbd.com/"
        html = urllib.urlopen(url).read()
        logging.info(html)
        p = re.compile(r"[\u4e00-\u9fa5]+")
        word = p.findall(html)

        return word

    def test_customer_verify(self):
        log_msg = a.RiZhi()
        log_msg.log_def()
        url_temp = "http://boss.sinobbd.com/"
        html = urllib.urlopen(url_temp).read()
        logging.info(html)
        p = re.compile(r"[\u4e00-\u9fa5]+")
        pass
        return



if __name__ == '__main__':
    unittest.main()