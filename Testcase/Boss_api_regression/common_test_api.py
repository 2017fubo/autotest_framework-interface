# -*- coding:utf-8 -*-

__author__ = 'fubo'

import logging
import jsonschema as Jchema
import  unittest
from Tools import confighttp,TestobjectReadWriter
from rizhi import log_config as a
import json as JS


# 测试用例(组)类
class Common_Test_Api:

    def __init__(self,TestName):
        self.TestName = TestName

#公用方法
#API用例获取
    # 读取接口服务list，获取请求地址\参数，期待code\msg 方法
    def get_api_info(self):
        excel_read = TestobjectReadWriter.ReadWriter_ecxel()
        request_url, request_param, expect_code, expect_data, \
        expect_msg = excel_read.read_excel_caseinfo(self.TestName)
        return request_url, request_param, expect_code, expect_data, expect_msg

#接口返回内容信息获取
  #获取接口期待返回data分解 公用方法
    def get_expect_data_for_key(self):
        self.expect_data_key = self.expect_data["key"]
        logging.info("Key值%s" %self.expect_data_key)
        self.expect_data_val = self.expect_data["val"]
        logging.info("Val值%s" %self.expect_data_val)

        return self.expect_data_val,self.expect_data_key

##获取接口期待返回data分解 公用方法
    def get_expect_data_for_key2(self):

        self.expect_data_key = self.expect_data["key"]
        logging.info("Key值%s" % self.expect_data_key)
        self.expect_data_val = self.expect_data["val"]
        logging.info("Val值%s" % self.expect_data_val)
        self.expect_data_key2 = self.expect_data["key2"]
        logging.info("Key2值%s" % self.expect_data_key2)
        self.expect_data_val2 = self.expect_data["val2"]
        logging.info("Val2值%s" % self.expect_data_val2)

        return self.expect_data_key, self.expect_data_val,\
               self.expect_data_key2, self.expect_data_val2

#获取code，msg公用方法
    def get_responseinfo_for_code_msg(self):
        code_temp = []
        for index, value in enumerate(self.response):
            code_temp.append(value)  ##
        logging.info(code_temp)
        # 获取返回信息 返回code
        if 'ret' in code_temp:
            self.sReal_code = self.response['ret']  ##获取返回的code
        else:
            if 'code' in code_temp:
                    self.sReal_code = self.response['code']  ##获取返回的code
            else:
                self.sReal_code = False
        ##获取返回msg
        self.sReal_msg = self.response['msg']
        logging.info(self.sReal_code,self.sReal_msg)

        return self.sReal_code,self.sReal_msg

#接口验证方法
   ##只验证code和message-通常
    def common_test_msg(self):
        #读取接口服务list，获取请求地址\参数，期待code\msg
        self.request_url,self.request_param,self.expect_data,self.expect_code,\
        self.expect_msg = self.get_api_info()

        # http post请求
        Http_temp = confighttp.ConfigHttp()
        self.response = Http_temp.post(self.request_url, self.request_param)
        # 获取返回信息
        self.sReal_code =self.response['code']##获取返回的code
        self.sReal_msg = self.response['msg']
        logging.info(self.expect_msg)
        return self.sReal_code,self.expect_code,self.sReal_msg,self.expect_msg

    ##验证code、message，并验证data中包含预定的值-通常
    def common_test_data(self):
        #读取接口服务list，获取请求地址\参数，期待code\msg
        self.request_url, self.request_param, self.expect_data, \
        self.expect_code, self.expect_msg = self.get_api_info()

        self.expect_data = eval(self.expect_data)
        self.expect_data_val, self.expect_data_key = self.get_expect_data_for_key()
        # http post请求
        Http_temp = confighttp.ConfigHttp()
        self.response = Http_temp.post(self.request_url, self.request_param)
        L_temp = len(self.response['data'])
        logging.info("返回json内容%s"%self.response)
        logging.info("长度%s"%L_temp)

        # ##追加返回json格式验证 0922  fubo
        # logging.info(jsonschema_temp)
        # # self.jsonschema_temp = JS.loads(jsonschema_temp)
        #
        # temp = Jchema.validate(self.response,jsonschema_temp)
        # logging.info(temp)

        ##获取返回code，msg
        self.sReal_code, self.sReal_msg = self.get_responseinfo_for_code_msg()

        # 返回data
        self.sReal_data=[]
        for i in range(0,L_temp):
            self.sReal_data.append(self.response['data'][i][self.expect_data_key])
            logging.info("接口实际返回data" %self.sReal_data)
            i +=1
        logging.info(self.sReal_data)
        logging.info(self.expect_data_val)

        return self.sReal_data,self.expect_data_val,self.sReal_code,\
               self.expect_code,self.sReal_msg,self.expect_msg

##验证code、message，并验证data中包含预定的值-通常
    def common_test_data_nonzero(self):
        # 读取接口服务list，获取请求地址\参数，期待code\msg
        self.request_url, self.request_param, self.expect_data, self.expect_code,\
        self.expect_msg = self.get_api_info()

        self.expect_data = eval(self.expect_data)
        self.expect_data_val, self.expect_data_key = self.get_expect_data_for_key()

        # http post请求
        Http_temp = confighttp.ConfigHttp()
        self.response = Http_temp.post(self.request_url, self.request_param)
        L_temp = len(self.response['data'])
        logging.info("长度%s" % L_temp)

        ##获取返回code，msg
        self.sReal_code, self.sReal_msg = self.get_responseinfo_for_code_msg()

        # 返回data
        self.sReal_data = []
        # self.response['data'][self.expect_data_key][0]
        for i in range(0, L_temp):
            self.sReal_data.append(self.response['data'][self.expect_data_key][i])
            i += 1
        logging.info(self.sReal_data)
        logging.info(self.expect_data_val)
        return self.sReal_data, self.expect_data_val, \
               self.sReal_code, self.expect_code, self.sReal_msg, self.expect_msg

 ###验证code、message，并验证data中包含预定的值---刷新系统接口测试方法
    def common_test_data_refresh(self):
        # 读取接口服务list，获取请求地址\参数，期待code\msg
        self.request_url, self.request_param, self.expect_data, self.expect_code, \
        self.expect_msg = self.get_api_info()
        logging.info("case期待message%s"%self.expect_data)
        try:
         self.expect_data = eval(self.expect_data)

        except Exception as e:
            logging.info(e)

        try:
            ##分解期待messange
            self.expect_data_key, self.expect_data_val, self.expect_data_key2, \
            self.expect_data_val2 = self.get_expect_data_for_key2()

            # http post请求
            Http_temp = confighttp.ConfigHttp()
            self.response = Http_temp.post(self.request_url, self.request_param)
            L_temp = len(self.response['data'])
            logging.info("长度%s" % L_temp)
        except Exception as e:
            logging.info(e)

        ##获取返回code，msg
        self.sReal_code, self.sReal_msg = self.get_responseinfo_for_code_msg()

        ##获取返回data
        self.sReal_data = []
        response_key2data = self.response['data'][self.expect_data_key][self.expect_data_val][self.expect_data_key2]
        logging.info(response_key2data)
        if isinstance(response_key2data,list):
            for index, value in enumerate(response_key2data):
                self.sReal_data.append(value) ##

            logging.info(self.sReal_data)
            logging.info(self.expect_data_val2)
            return self.sReal_data, self.expect_data_val2, self.sReal_code, \
                   self.expect_code, self.sReal_msg, self.expect_msg
        else:
            logging.info(response_key2data)
            logging.info(self.expect_data_val2)

            return response_key2data, self.expect_data_val2, self.sReal_code, \
                   self.expect_code, self.sReal_msg, self.expect_msg

    ###自建boss提供给HBoss信息相关接口测试方法
    def common_test_msg_selfBoss(self):

    ##接口请求token获取(domainCost不需要auth判断)
        if self.TestName != 'domainCost':
            url = "http://test-boss.bbdcdn.net/api/Auth"
            # request_param = {"data": {"appId": "559a937c70fbd572","signature": "ea73b3dc14d2dac8407ae6e0204cf9dd0b1c0aa8"}}
            request_param = "{\"data\":{\"appId\":\"559a937c70fbd572\",\"signature\":\"ea73b3dc14d2dac8407ae6e0204cf9dd0b1c0aa8\"}}"
            Http_temp = confighttp.ConfigHttp()
            self.response_1 = Http_temp.post_auth(url,request_param)
            logging.info(self.response_1)
            self.token =self.response_1["data"]['token']##获取返回的code
            # logging.info("token值：s%" %self.token)
            # logging.info(self.token)

            ##获取接口文档中的请求地址，预期data、code、msg
            self.request_url, self.request_param, self.expect_data, \
            self.expect_code, self.expect_msg = self.get_api_info()

            self.expect_data = eval(self.expect_data)
            ###分解返回预期data
            self.expect_data_key, self.expect_data_val, \
            self.expect_data_key2,self.expect_data_val2 = self.get_expect_data_for_key2()

            # http post_auth请求
            self.response = Http_temp.http_post_headers(self.request_url,self.request_param,self.token)
        else:
            self.request_url, self.request_param, self.expect_data, self.expect_code, \
            self.expect_msg = self.get_api_info()

            self.expect_data = eval(self.expect_data)

            self.expect_data_key, self.expect_data_val, self.expect_data_key2, \
            self.expect_data_val2 = self.get_expect_data_for_key2()

            # http post请求
            Http_temp = confighttp.ConfigHttp()
            self.response = Http_temp.post(self.request_url, self.request_param)
        # 获取返回信息code,msg

        logging.info(self.response)
        self.sReal_code, self.sReal_msg = self.get_responseinfo_for_code_msg()

        logging.info(self.expect_msg)

        ##获取返回data

        self.sReal_data = []
        if self.TestName == 'DomainCost_self':
            self.response_key2data = self.response["data"][self.expect_data_key][self.expect_data_key2]
            logging.info(self.response_key2data)
            self.sReal_data = self.response_key2data

            return self.sReal_data,self.expect_data_val2,self.sReal_code,\
                   self.expect_code, self.sReal_msg, self.expect_msg

        else:
            if self.TestName == 'GetCustomerDomain':
                self.response_key2data = self.response["data"][self.expect_data_key]
                logging.info(self.response_key2data)

                self.sReal_data = []
                for i in range(0, len(self.response_key2data)):
                    self.sReal_data.append(self.response_key2data[i][self.expect_data_key2])
                    logging.info("接口实际返回data" % self.sReal_data)
                    i += 1
                logging.info(self.sReal_data)
                logging.info(self.expect_data_val2)

                return self.sReal_data,self.expect_data_val2,self.sReal_code,\
                       self.expect_code, self.sReal_msg, self.expect_msg