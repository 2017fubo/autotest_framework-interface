import os
import logging

# api请求地址相关信息定义类
# ###header infomation ####
class API2_0_Request_baseinfo:

    def Request_address(self):
        # 测试request_url
        test_address = "http://118.190.141.177:8989/"
        return test_address

    def Intlapi_header_boss(self):
        ## 测试 request_header
        self.boss_header = {
                            "Lg-date": "2017-12-13T10:41:26+08:00",
                            'Content-Type': "application/json"
                            }
        return self.boss_header

    def Intlapi_header_protal(self):
        self.protal_header = {"request-date": "Mon, 22 May 2017 07:35:01 GMT",
                            "Authorization": "Basic MTY1OTpaVFk0WkdRNU5qVTVaREk1WTJZNU4yWmhObVpoTlRGbVlUUmxORFppTVRJPQ==",
                            "Content-Type": "application/json"
                            }
        return self.protal_header

    def Outapi_header(self):
        self.outapi_header = {
                              "x-request-date": "Wed, 08 Nov 2017 18:22:01 CST",
                              "Authorization": "Basic MjM6TXpKaE1UbGxOVFk1TkRjME16YzJNamc0WlRJMU5ETmtOMlV3T0Roa01ETT0=",
                              "Content-Type": "application/json",
                             }
        return self.outapi_header