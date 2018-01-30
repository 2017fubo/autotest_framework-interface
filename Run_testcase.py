# -*- coding:utf-8 -*-
__author__ = 'fubo'
from selenium import webdriver
import unittest
from Tools import TestobjectReadWriter
from rizhi import log_config as a
import logging
from config import globalconfig
import sys,os
from Testcase.Boss import boss_mix,reptile_temp
from Testcase.cdn_boss import boss_cdn
from Testcase.public import login_mix
import HTMLTestRunner
import time
from Testcase.public import Email

def creat_suit_api():

    testcasepath_api = "E:\SinoBBD\AUTOTEST\Web_Autoest_FW\Testcase\Api2_0_Testcase"
    logging.info("Start Test")
    testunit = unittest.TestSuite()
    #discover读取（需要执行的用例_）
    discover = unittest.defaultTestLoader.discover(testcasepath_api,
                                                   pattern= "test_interface_api20_*.py",
                                                   top_level_dir= None)
    logging.info("装载测试案例:%s"%discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            logging.warning("%s"%testunit)
    return testunit

def creat_suit_ui():
    testcasepath_ui = "E:\SinoBBD\AUTOTEST\Web_Autoest_FW\Testcase\Api_regression"
    logging.info("Start Test")
    testunit = unittest.TestSuite()
    #discover读取（需要执行的用例标记Boss_）
    discover = unittest.defaultTestLoader.discover(testcasepath_ui,
                                                   pattern= "test_interface_*.py",
                                                   top_level_dir= None)
    logging.info("装载测试案例")
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            logging.info("%s"%testunit)
    return testunit

if __name__ == '__main__':
    log_msg = a.RiZhi()
    log_msg.log_def()
    logging.debug(u"测试开始")
    ###执行API
    all_testcase_names = creat_suit_api()
    time_temp = time.strftime("%Y%m%d-%HH%MM", time.localtime())
    filename = "E:\SinoBBD\AUTOTEST\Web_Autoest_FW\TestResult\TestResult_"+ time_temp + "result.html"
    filep = open(filename,"wb")
    logging.info("做成测试报告并执行测试案例")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream= filep,
        title= "CDN研发-API2.0接口测试结果",
        description= u"API2.0接口测试执行结果汇总：")
    #执行测试用例
    logging.info("执行测试案例")
    runner.run(all_testcase_names)
    filep.close()
    #发送mail 仍需要调研
    # email_temp = Email.Mail_Send()
    # email_temp.send_report()
    # end