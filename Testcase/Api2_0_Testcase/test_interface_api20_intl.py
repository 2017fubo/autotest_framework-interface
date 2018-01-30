# -*- coding:utf-8 -*-
__author__ = 'fubo'
import logging,sys
import unittest
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_baseinfo as baseinfo
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_paraminfo as paraminfo
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_urlinfo as urlinfo
import Testcase.Api2_0_Testcase.HttpRequest_method as HttpReq_MD
# 测试用例(组)类
class API_InterfaceCase(unittest.TestCase):
    u"""接口测试_internal"""
    # @classmethod
    def setUp(self):
    # 获取接口请求基础信息，address、header等
        try:
            ##获取intl接口请求地址 address
            tmp_baseinfo = baseinfo.API2_0_Request_baseinfo()
            self.api_address = tmp_baseinfo.Request_address()
            logging.info("请求address :%s" % self.api_address)
            #获取boss系统intl api请求的header
            self.boss_header = tmp_baseinfo.Intlapi_header_boss()
            #获取portal系统intl api请求的header
            self.portal_header = tmp_baseinfo.Intlapi_header_protal()
        ####
        #获取所有intl 接口的 请求地址
            tmp_urlinfo = urlinfo.API2_0_Request_urlinfo()
            self.url_all = tmp_urlinfo.intl_rquest_url()
            #logging.debug(self.url_all)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口地址 or header错误%s"%e)
    #return self.api_address,self.boss_header,self.portal_header,self.url_all

    def test_01_flowTerminal(self):
        u"""CS终端流量查询"""
        logging.info("Start Test test_01_flowTerminal！")
    #获取 test_01_flowTerminal 测试URL 1
        try:
            tmp_url = self.url_all #所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[0] #获取请求url 00_flowTerminal
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取 url 错误%s" %e)
        ###对期待code和msg赋值
        self.expect_code = "400010001"  ##期待code
        self.expect_msg = "请求成功"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_02_purge_list(self):
        u"""CS系统刷新任务列表请求接口"""
        logging.info("Start Test test_02_purge_list！")
        #获取 test_02_purge_list 测试URL 2
        try:
            tmp_url = self.url_all ###所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[1]  ###获取请求url 1_purge_list
            logging.debug(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s"%e)
        self.expect_code = "400010001"
        self.expect_msg = "请求成功"
        return

    def test_03_purge_all_list(self):
        u"""Boss系统刷新任务列表请求接口"""
        logging.info("Start Test test_03_purge_all_list！")
        #获取  测试URL 3
        try:
            self.req_url = self.url_all[2]  ###获取请求url 3 _purge_all_list
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误"%e)
        self.expect_code = "500010001"
        self.expect_msg = "请求成功"
        return

    def test_04_preload_list(self):
        u"""CS系统预缓存任务列表"""
        logging.info("Start Test test_04_preload_list！")
        #获取接口地址、url
        try:
            self.req_url = self.url_all[3]  ###获取请求url 4_preload_list
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        self.expect_code = "400010001"
        self.expect_msg = "请求成功"
        return

    def test_05_preload_all_list(self):
        u"""Boss系统预缓存任务列表"""
        logging.info("Start Test test_05_preload_all_list！")
        # 获取  测试URL 5
        try:
            self.req_url = self.url_all[4]  ###获取请求url 05_preload_all_list
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url错误%s" % e)

        self.expect_code = "500010001"
        self.expect_msg = "请求成功"
        return

    def test_06_preload_set(self):
        u"""Boss预缓存系统强制刷新"""
        logging.info("Start Test test_06_preload_set！")
        # 获取  测试URL 5
        try:
            self.req_url = self.url_all[5]  ###获取请求url 06_preload_set
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口地址 or header or url 错误%s" % e)

        self.expect_code = "600010001"
        self.expect_msg = "请求成功"

        return

    def test_07_inject_list(self):
        u"""CS内容注入任务列表请求接口"""
        logging.info("Start Test test_07_inject_list！")
        # 获取接口地址url
        try:
            self.req_url = self.url_all[6] ##获取请求url 07_inject_list
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" %e)
        self.expect_code = "400010001"
        self.expect_msg = "请求成功"

        return

    def test_08_inject_all_list(self):
        u"""Boss内容注入任务列表请求接口"""
        logging.info("Start Test test_08_inject_all_list！")
        # 获取  测试URL 5
        try:
            self.req_url = self.url_all[7]  ###获取请求url test_08_inject_all_list
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口 url 错误%s" % e)

        self.expect_code = "500010001"
        self.expect_msg = "请求成功"
        return

    def test_09_inject_set(self):
        u"""Boss预注入任务强制刷新"""
        logging.info("Start Test test_09_inject_set！")
        # 获取  测试URL 5
        try:
            self.req_url = self.url_all[8]  ###获取请求url test_09_inject_set
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        #
            self.assertEqual(1, 0, msg="接口请求错误%s" % e)
        self.expect_code = "600010001"
        self.expect_msg = "请求成功"

        return

    def test_10_log_select(self):
        u"""Boss日志查询"""
        logging.info("Start Test test_10_log_select！")
        # 获取  测试URL 5
        try:
            self.req_url = self.url_all[9]  ###获取请求url test_10_log_select
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口 url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "400010001"
        self.expect_msg = "请求成功"
        return

    def test_12_userInfo(self):
        u"""Boss用户信息获取并缓存"""
        logging.info("Start Test test_12_userInfo！")
        # 获取  测试URL 12
        try:
            self.req_url = self.url_all[10]  ###获取请求url test_12_userInfo
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "400010001"
        self.expect_msg = "请求成功"
        return

    def test_13_purge(self):
        u"""CS刷新任务"""
        logging.info("Start Test test_13_purge！")
        # 获取  测试URL 13
        try:
            self.req_url = self.url_all[11] ###获取请求url test_13_purge
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "300020001"
        self.expect_msg = "刷新调用成功"
        return

    def test_14_preload(self):
        u"""CS系统预缓存"""
        logging.info("Start Test test_14_preload！")
        # 获取 测试URL 13
        try:
            self.req_url = self.url_all[12] ###获取请求url test_14_preload
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "300020009"
        self.expect_msg = "预缓存调用成功"
        return

    def test_15_flow_manu(self):
        u"""CS请求分厂商获取流量"""
        logging.info("Start Test test_15_flow_manu！")
        # 获取  测试URL 13
        try:
            self.req_url = self.url_all[13]  ###获取请求url test_15_flow_manu
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "300020013"
        self.expect_msg = "流量查询请求成功"
        return

    def test_17_getHttpCode(self):
        u"""Boss根据域名获取http状态码"""
        logging.info("Start Test test_17_getHttpCode！")
        # 获取  测试URL 13
        try:
            self.req_url = self.url_all[14]  ###获取请求url test_17_getHttpCode
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        self.expect_code = "300080001"
        self.expect_msg = "http状态码查询成功"
        return

    def test_18_getBaseInjectList(self):
        u"""获取getBaseInjectList未发送的任务状态"""
        logging.info("Start Test test_18_getBaseInjectList！")
        # 获取  测试URL 16
        try:
            self.req_url = self.url_all[15]  ###获取请求url test_18_getBaseInjectList
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "0"
        self.expect_msg = "请求成功"
        return

    def test_19_getBaseInjectSyncList(self):
        u"""获取injectsynclist未发送的任务状态"""
        logging.info("Start Test test_19_getBaseInjectSyncList！")
        # 获取  测试URL 16
        try:
            self.req_url = self.url_all[16]  ###获取请求url test_19_getBaseInjectSyncList
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = "0"
        self.expect_msg = "请求成功"
        return

    def test_20_getDomainList(self):
        u"""全量域名获取"""
        logging.info("Start Test test_20_getDomainList！")
        # 获取  测试URL 16
        try:
            self.req_url = self.url_all[17]  ###获取请求url test_20_getDomainList
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口url 错误%s" % e)
        ##获取请求url对应的参数
        self.expect_code = 0
        self.expect_msg = "查询成功。"
        return

    def tearDown(self):
        ##
        ##依据要测试的url，获取请求url对应的参数##
        ##
        try:
            tmp_paraminfo = paraminfo.ReadWriter_ecxel()
            self.req_info = tmp_paraminfo.read_caseparam_int(self.req_url)
            self.req_paraminfo = self.req_info[0]
            self.req_sysinfo = self.req_info[1]
            self.req_httpmethod = self.req_info[2]
            logging.debug("获取的请求参数:%s" % self.req_paraminfo)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取请求参数%s" %e)
        ##依据获取的接口请求信息进行接口请求。

        if self.req_sysinfo == "Portal":
            self.header = self.portal_header
        elif self.req_sysinfo == "BOSS":
            self.header = self.boss_header
        else:
            self.assertEqual(1, 0, msg="接口系统信息请求错误")
        try:
            if self.req_httpmethod == "POST":
                request = HttpReq_MD.HttpRequest_method()
                self.response = request.post(self.api_address, self.req_url, self.req_paraminfo, self.header)
            elif self.req_httpmethod == "GET":
                request = HttpReq_MD.HttpRequest_method()
                self.response = request.get(self.api_address, self.req_url, self.req_paraminfo, self.header)
            else:
                self.assertEqual(1, 0, msg="请求方法信息错误")

            self.response_json = self.response[0]
            self.response_status = self.response[1]
        except Exception as e:
            self.assertEqual(1, 0, msg="接口请求错误%s" % e)

        # # 结果判断
        if self.response_status == 200:
        ##将返回的code和mes和data 分别保存
            if self.req_url != "internal/getDomainList":
                self.sReal_code = self.response_json["result"]["code"]
                self.sReal_msg = self.response_json["result"]["message"]
            else:
                self.sReal_code = self.response_json["code"]
                self.sReal_msg = self.response_json["message"]
        else:
            self.assertEqual(1, 0, msg="接口返回Http code：%s" % self.response_status)
        logging.info(".............结果判断验证:...........")
        self.assertEqual(self.sReal_code, self.expect_code, msg="返回code不符合期望，接口请求错误,返回的json:\r\n%s" %self.response_json)
        self.assertEqual(self.sReal_msg, self.expect_msg, msg="返回msg不符合期望，接口请求错误,返回的json:\r\n%s" % self.response_json)
        logging.info("Pass")

    #
    # if __name__ == '__main__':
    #         unittest.main()