# -*- coding:utf-8 -*-

__author__ = 'fubo'

import logging
import  unittest
from Tools import confighttp,TestobjectReadWriter
from rizhi import log_config as a
from Testcase.Boss_api_regression import common_test_api
from Testcase.Boss_api_regression import  _jsonschema

# 测试用例(组)类
class SelfBoss_InterfaceCase(unittest.TestCase):
    u"""自建Boss对外服务接口"""
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
    def test_03_PhysicalNode(self):
        u"""物理节点信息获取接口"""
        logging.info("Start Test test_PhysicalNode！")
        TestName = "PhysicalNode"
        ##追加返回json格式验证 0922  fubo
        json_temp = _jsonschema._Jsonschema_(TestName)
        temp_jsonschema = json_temp.jsonschema_PhysicalNode()

        # 获取接口地址、参数、预期返回结果
        test_api_temp = common_test_api.Common_Test_Api(TestName)
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data()

        # # 结果判断 data 包含与否
        self.result_confirm_datain()

        return

    def test_04_VirtualNode(self):
        u"""虚拟节点信息获取接口"""
        logging.info("Start Test test_VirtualNode！")
        TestName = "VirtualNode"
        # 获取接口地址、参数、预期返回，以及真实接口返回data、code、msg
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        self.sReal_data, self.expect_data, self.sReal_code,\
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data()
        # 结果判断 data 包含与否
        self.result_confirm_datain()

        return

    def test_05_DeviceInfo(self):
        u"""设备信息获取接口"""
        logging.info("Start Test test_DeviceInfo！")
        TestName = "DeviceInfo"

        # 获取接口地址、参数、预期返回，以及真实接口返回data、code、msg
        test_api_temp = common_test_api.Common_Test_Api(TestName)
        self.sReal_code, self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_msg()

        # 结果判断（仅判断code和 message）
        self.result_confirm_msg()

        return

    def test_06_ServerGroup(self):
        u"""服务器组接口"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_ServerGroup！")
        TestName = "ServerGroup"
        test_api_temp = common_test_api.Common_Test_Api(TestName)
        self.sReal_data, self.expect_data, self.sReal_code,\
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data()

        # 结果判断 data 包含与否
        self.result_confirm_datain()
        return

    def test_07_BuildServerIp(self):
        u"""ip信息接口"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_ServerGroup！")
        TestName = "BuildServerIp"
        test_api_temp = common_test_api.Common_Test_Api(TestName)
        self.sReal_data, self.expect_data, self.sReal_code, \
        self.expect_code, self.sReal_msg, self.expect_msg = test_api_temp.common_test_data()

        # 结果判断 data 包含与否
        self.result_confirm_datain()
        return


    def test_11_GetCustomerDomain(self):
        u"""客户域名列表接口"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_11_GetCustomerDomain！")
        TestName = "GetCustomerDomain"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data,self.sReal_code, self.expect_code,\
        self.sReal_msg, self.expect_msg = test_api_temp.common_test_msg_selfBoss()

        # 结果判断 data 包含
        self.result_confirm_datain()
        return

    def test_12_DomainCost_self(self):
        u"""域名计费带宽流量接口"""

        # 获取接口地址、参数、预期返回结果
        logging.info("Start Test test_12_DomainCost_self！")
        TestName = "DomainCost_self"
        test_api_temp = common_test_api.Common_Test_Api(TestName)

        ##Hboss 方法使用
        self.sReal_data, self.expect_data, self.sReal_code, self.expect_code, \
        self.sReal_msg, self.expect_msg = test_api_temp.common_test_msg_selfBoss()

        # 结果判断 data 包含
        self.result_confirm_datain()
        return

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()