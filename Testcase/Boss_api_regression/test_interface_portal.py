# -*- coding:utf-8 -*-

__author__ = 'fubo'

import logging
import  unittest
from Tools import confighttp,TestobjectReadWriter
from rizhi import log_config as a
from Testcase.Boss_api_regression import common_test_api

# 测试用例(组)类
class Portal_InterfaceCase(unittest.TestCase):
    u"""Portal对外服务接口"""

    @classmethod
    def setUpClass(self):
        pass
        # self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_API.png"

##公用方法
    def result_confirm_datain(self):
        # # 结果判断 data 包含与否
        self.assertIn(self.expect_data, self.sReal_data, msg=None)
        logging.info(".............结果判断验证data:%s..........."%self.expect_data)
        # 结果判断（判断code和 message）
        self.assertEqual(self.sReal_code, self.expect_code, msg=None)
        self.assertEqual(self.sReal_msg, self.expect_msg, msg=None)

        return

    def result_confirm_data(self):
        # # 结果判断 data 包含与否
        self.assertEqual(self.expect_data, self.sReal_data, msg=None)

        logging.info(".............结果判断验证data:%s..........."%self.expect_data)
        # 结果判断（判断code和 message）
        self.assertEqual(self.sReal_code, self.expect_code, msg=None)
        self.assertEqual(self.sReal_msg, self.expect_msg, msg=None)

        return

    def result_confirm_msg(self):
        logging.info(".............结果判断验证code:%s..........." % self.expect_code)
        # 结果判断（判断code和 message）
        self.assertEqual(self.sReal_code, self.expect_code, msg=None)
        self.assertEqual(self.sReal_msg, self.expect_msg, msg=None)

        return

####test case

    def test_16_trafficSearchForParticle(self):
        u"""流量查询(分颗粒度, 分域名)"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_16_trafficSearchForParticle！")
        TestName = "trafficSearchForParticle"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data_refresh()
        self.sReal_data = int(self.sReal_data)
        self.expect_data = int(self.expect_data)
        logging.info("返回的结果:%s和期待值:%s"%(self.sReal_data,self.expect_data))

        # 结果判断 data 包含与否
        self.result_confirm_data()
        return

    def test_17_bandwidthSearchForParticle(self):
        u"""带宽查询(分颗粒度, 分域名)"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_17_bandwidthSearchForParticle！")
        TestName = "bandwidthSearchForParticle"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data_refresh()
        logging.info("返回的结果:%s和期待值:%s"%(self.sReal_data,self.expect_data))

        # 结果判断 data 包含与否
        self.result_confirm_data()
        return

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()