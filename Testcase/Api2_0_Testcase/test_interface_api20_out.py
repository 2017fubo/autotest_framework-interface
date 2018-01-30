# -*- coding:utf-8 -*-
__author__ = 'fubo'
import logging,sys
import time
import unittest
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_baseinfo as baseinfo
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_paraminfo as paraminfo
import Testcase.Api2_0_Testcase.Api2_0_Testcase_Res.Request_urlinfo as urlinfo
import Testcase.Api2_0_Testcase.HttpRequest_method as HttpReq_MD
# 测试用例(组)类
class API_InterfaceCase(unittest.TestCase):
    u"""接口测试_Out_for customer(api)"""
    #
    def setUp(self):
    # 获取接口请求基础信息，address、header等
        try:
            ##获取intl接口请求地址 address
            tmp_baseinfo = baseinfo.API2_0_Request_baseinfo()
            self.api_address = tmp_baseinfo.Request_address()
            logging.info("请求address :%s" % self.api_address)
            #获取boss系统intl_api请求的header
            self.header = tmp_baseinfo.Outapi_header()
            logging.info("Header信息%s" %self.header)
        ####
        #获取所有intl 接口的 请求地址
            tmp_urlinfo = urlinfo.API2_0_Request_urlinfo()
            self.url_all = tmp_urlinfo.Out_request_url()
            # logging.debug(self.url_all)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取接口地址 or header错误%s" %e)

    def test_01_purge(self):
        u"""刷新接口"""
        logging.info("Start Test test_01_purge！")
    #获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all #所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[0] #获取请求url test_01_purge
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" %e)
        ###对期待code和msg赋值
        self.expect_code = "AR001"  ##期待code
        self.expect_msg = "刷新调用成功"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_02_newTasksNotice_purge(self):
        u"""回调接口-（刷新）"""
        logging.info("Start Test test_02_newTasksNotice for purge！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[1]  # 获取请求url
            self.req_url = "port/newTasksNotice-purge"
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "1001"  ##期待code
        self.expect_msg = "请求成功。"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_03_purge_get(self):
        u"""刷新查询接口"""
        logging.info("Start Test test_03_purge_get！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[2]  # 获取请求url api/purge?
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AR101"  ##期待code
        self.expect_msg = "刷新查询接口调用成功"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_04_inject(self):
        u"""注入接口(通常注入)"""
        logging.info("Start Test test_04_inject！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[3]  # 获取请求url api/purge
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AI001"  ##期待code
        self.expect_msg = "注入调用成功"
        # 结果判断 在teardown中执行
        return

    def test_05_inject_get(self):
        u"""内容注入查询"""
        logging.info("Start Test test_05_inject_get！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[4]  # 获取请求url api/purge
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AI101"  ##期待code
        self.expect_msg = "内容注入查询调用成功"
        # 结果判断 在teardown中执行
        return

    def test_06_newInjectTasks(self):
        u"""回调接口-（注入回调）"""
        logging.info("Start Test test_06_newInjectTasks！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[5]  # 获取请求url api/purge
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" %e)
        ###对期待code和msg赋值
        self.expect_code = "2001"  ##期待code
        self.expect_msg = "请求成功。"
        # 结果判断 在teardown中执行
        return

    def test_07_preload(self):
        u"""预缓存接口"""
        logging.info("Start Test test_07_preload！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[6]  # 获取请求url api/preload
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" %e)
        ###对期待code和msg赋值
        self.expect_code = "AP001"  ##期待code
        self.expect_msg = "预缓存调用成功"
        # 结果判断 在teardown中执行
        return

    def test_08_newTasksNotice_preload(self):
        u"""回调接口-（预缓存）"""
        logging.info("Start Test test_08_newTasksNotice_preload for preload！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[7]  # 获取请求url port/newTasksNotice
            self.req_url = "port/newTasksNotice-preload"
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "2001"  ##期待code
        self.expect_msg = "请求成功。"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_09_preload_get(self):
        u"""预缓存查询接口"""
        logging.info("Start Test test_09_preload_get！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[8]  # 获取请求url port/test_09_preload? get
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AP101"  ##期待code
        self.expect_msg = "预缓存查询调用成功"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_10_bandwidth(self):
        u"""域名请求带宽查询"""
        logging.info("Start Test test_10_bandwidth！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[9]  # 获取请求url port/test_10_bandwidth? get
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AW001"  ##期待code
        self.expect_msg = "带宽查询请求成功"
        ##期待msg 固定值：请求成功
        # 结果判断 在teardown中执行
        return

    def test_11_receive(self):
        u"""注入接口(华数fds注入)"""
        logging.info("Start Test test_11_receive！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[10]  # 获取请求url port/test_11_receive post form-data param
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "0"  ##期待code
        self.expect_msg = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ccsc><result>SUCCESS</result><detail></detail></ccsc>"
        ##期待msg 固定值：请求成功
    ##请求参数在 HttpRequest_method中也写死。
        # 结果判断 在teardown中执行
        return

    def test_12_flow(self):
        u"""流量查询接口"""
        logging.info("Start Test test_12_flow！")
        # 获取 test_01_flowTerminal测试URL1
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[11]  # 获取请求url port/test_12_flow GET
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AB001"  ##期待code
        self.expect_msg = "流量查询请求成功"
        ##期待msg 固定值：请求成功
        return

    def test_13_downloadLog(self):
        u"""日志下载接口"""
        logging.info("Start Test test_13_downloadLog！")
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[12]  # 获取请求url port/test_13_downloadLog POST
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "400010003"  ##期待code
        self.expect_msg = "流量查询请求成功"
        ##期待msg 固定值：请求成功
        return

    def test_14_inject_iptv(self):
        u"""IPTV注入"""
        logging.info("Start Test test_14_inject_iptv！")
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[13]  # 获取请求url port/test_14_inject_iptv POST
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "0"  ##期待code
        self.expect_msg = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ccsc><result>SUCCESS</result><detail></detail></ccsc>"
        ###请求参数在 HttpRequest_method中也写死。
        ##期待msg 固定值：请求成功
        return

    def test_15_inject_hls(self):
        u"""HLS切片"""
        logging.info("Start Test test_15_inject_hls！")
        time.sleep(15)
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[14]  # 获取请求url port/test_15_inject_hls POST
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "0"  ##期待code
        self.expect_msg = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ccsc><result>SUCCESS</result><detail></detail></ccsc>"
        ###请求参数在 HttpRequest_method中也写死。
        ##期待msg 固定值：请求成功
        return

    def test_17_inject_upeng(self):
        u"""注入-优朋注入"""
        logging.info("Start Test test_17_inject_upeng！")
        try:
            tmp_url = self.url_all  # 所有请求url（本测试Class中所有的请求url）
            self.req_url = tmp_url[16]  # 获取请求url port/test_17_inject_upeng POST
            logging.info(self.req_url)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取url错误%s" % e)
        ###对期待code和msg赋值
        self.expect_code = "AI001"  ##期待code
        self.expect_msg = "注入调用成功"

        return

    def tearDown(self):
        ##
        ##依据要测试的url，获取请求url对应的参数##
        try:
            tmp_paraminfo = paraminfo.ReadWriter_ecxel()
            self.req_info = tmp_paraminfo.read_caseparam_out(self.req_url)
            self.req_paraminfo = self.req_info[0]
            self.req_httpmethod = self.req_info[1]
            logging.debug("获取的请求参数:%s" % self.req_paraminfo)
        except Exception as e:
            self.assertEqual(1, 0, msg="获取请求参数%s"%e)

        ##依据获取的接口请求信息进行接口请求。
        if self.req_url in {"port/newTasksNotice-purge","port/newTasksNotice-preload"}:
            self.req_url = "port/newTasksNotice"
        elif self.req_url in {"api/inject_upeng"}:
            self.req_url = "api/inject"
            logging.info(self.req_url)
        else:
            self.req_url = self.req_url

        try:
            if self.req_httpmethod == "POST":
                request = HttpReq_MD.HttpRequest_method()
                self.response = request.post(self.api_address, self.req_url, self.req_paraminfo, self.header)
                self.response_json = self.response[0]
                self.response_status = self.response[1]
            elif self.req_httpmethod == "GET":
                request = HttpReq_MD.HttpRequest_method()
                self.response = request.get(self.api_address, self.req_url, self.req_paraminfo, self.header)
                self.response_json = self.response[0]
                self.response_status = self.response[1]
            elif self.req_httpmethod == "POSTxml":
                request = HttpReq_MD.HttpRequest_method()
                self.response_xml = request.postxml(self.api_address, self.req_url, self.req_paraminfo, self.header)
                self.response_json = self.response_xml[0]
                self.response_status = self.response_xml[1]
            else:
                self.assertEqual(1, 0, msg="请求方法信息填写错误，请修改用例中的请求方法")
        except Exception as e:
            self.assertEqual(1, 0, msg="接口请求错误%s，请查看HttpRequest_method方法"%e)
        # # 结果判断
        if self.response_status == 200:
        ##将返回的code和mes和data分别保存
            if self.req_url in{"api/inject?","api/bandwidth"}:###返回没有result 层级
                self.sReal_code = self.response_json["result"]["code"]
                self.sReal_msg = self.response_json["result"]["message"]
            elif self.req_url in{"api/receive","iptv/inject","hls/inject"}:###返回xml
                self.sReal_msg = self.response_json
                self.sReal_code = "0"
            else:
                self.sReal_code = self.response_json["result"]["code"]
                self.sReal_msg = self.response_json["result"]["message"]
        else:
            self.assertEqual(1, 0, msg="接口返回Http code：%s" % self.response_status)

        logging.info(".............结果判断验证:...........")
        logging.info("code:%s,%s\r\nmsg:%s,%s" %(self.sReal_code,self.expect_code,self.sReal_msg, self.expect_msg))
        self.assertEqual(self.sReal_code, self.expect_code, msg="返回code不符合期望，接口请求错误,返回的json:\r\n%s" %self.response_json)
        self.assertEqual(self.sReal_msg, self.expect_msg, msg="返回msg不符合期望，接口请求错误,返回的json:\r\n%s" % self.response_json)
        logging.info("Pass")
    #
    # if __name__ == '__main__':
    #         unittest.main()
