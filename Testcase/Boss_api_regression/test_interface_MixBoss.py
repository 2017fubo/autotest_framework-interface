# -*- coding:utf-8 -*-

__author__ = 'fubo'

import logging
import  unittest
from Tools import confighttp,TestobjectReadWriter
from rizhi import log_config as a
from Testcase.Boss_api_regression import common_test_api

# 测试用例(组)类
class MixBoss_InterfaceCase(unittest.TestCase):
    u"""融合Boss对外服务接口"""

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
    #
    def test_13_cacheSystemRelation(self):
        u"""Cache刷新系统所需关联关系接口"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_13_cacheSystemRelation！")
        TestName = "cacheSystemRelation"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data_refresh()


        # 结果判断 data 包含与否
        self.result_confirm_datain()

        return

    def test_14_ServerGroupAndDomainRelation(self):
        u"""服务器组与域名关系映射"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_14_ServerGroupAndDomainRelation！")
        TestName = "ServerGroupAndDomainRelation"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data_nonzero()

        # 结果判断 data 包含与否
        self.result_confirm_datain()
        return

###id_15暂时未对接，手动测试
    def test_15_domainCost(self):
        u"""计费带宽、流量查询接口"""

        pass
    #    logging.info("实施失败，请手动实施%s"% self.s)

    #     # 获取接口地址、参数、预期返回结果
    #     logging.info("Start Test test_15_domainCost！")
    #     TestName = "domainCost"
    #     test_api_temp = common_test_api.Common_Test_Api(TestName)
    #
    #     ##Hboss 方法使用
    #     self.sReal_code, self.expect_code, \
    #     self.sReal_msg, self.expect_msg = test_api_temp.common_test_msg_selfBoss()
    #
    #     # 结果判断 data 包含与否
    #     self.result_confirm_msg()
    #     return

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()