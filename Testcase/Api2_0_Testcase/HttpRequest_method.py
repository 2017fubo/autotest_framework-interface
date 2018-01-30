# -*- coding:utf-8 -*-

__author__ = 'fubo'
import urllib.request
import http.cookiejar
import urllib.parse
import json,sys
import configparser
import ssl
import logging
import http.client

class HttpRequest_method:

    def __init__(self):
        # self.headers = {}  # http 头
        #install cookie
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        # self.headers = headers
        # logging.info("headers 已经传入%s"%self.headers)

    #
    # # 设置http头
    # def set_header(self, headers):
    #    self.headers = headers

    def get(self,Request_address, url, params,header):
        #params = urllib.parse.urlencode(eval(params))  #
        params_temp = params
        url = Request_address + url +params_temp  ###
        request = urllib.request.Request(url, headers=header)
        try:
            response = urllib.request.urlopen(request)## http get 请求
            response1 = response.read().decode('utf-8')  ## decode函数对获取的字节数据进行解码
            status_code = response.getcode()
            json_response = json.loads(response1)  # 将返回数据转为json格式的数据
            logging.debug(status_code,json_response)
            return json_response,status_code
        except Exception as e:
            print('%s' % e)
            return {}

    def post(self,Request_address, url,params,header):
        data = json.dumps(eval(params))
        data = data.encode('utf-8')
        temp_url = Request_address  + url
        # logging.info("接口地址%s"%temp_url)
        # logging.info("请求header:%s"%header)
        try:
            request = urllib.request.Request(temp_url,headers=header)
            response = urllib.request.urlopen(request, data)## http post 请求
            response1 = response.read().decode('utf-8')## decode函数对获取的字节数据进行解码
            status_code = response.getcode()
            logging.info("返回code%s"%status_code)
            json_response = json.loads(response1)# 将返回数据转为json格式的数据
            return json_response,status_code
        except Exception as e:
            print('%s' % e)
            return {}

    def postxml(self, Request_address, url, params, header):####注入接口(华数fds注入) 请求方法

        conn = http.client.HTTPConnection("118.190.141.177:8989")
        header = { 'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"}

        try:
            if url ==  "api/receive":###写死请求参数 form-data
                params = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                         "Content-Disposition: form-data; name=\"context\"\r\n\r\n" \
                         "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ccsc><cust_id>2259</cust_id><passwd>cb0aa5d907c17521dffbb2a02eca1c07" \
                         "</passwd><item_id value=\"1282267652\"><site>210</site><source_path>http://192.168.100.139/customer/node-3.1.2.0.tgz" \
                         "</source_path><publish_path>http://vodfree-bj.wasu.cn/1282267652.tgz</publish_path><md5></md5><priority>3</priority><band_width>1300" \
                         "</band_width></item_id></ccsc>\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"op\"\r\n\r\npublish\r\n" \
                         "------WebKitFormBoundary7MA4YWxkTrZu0gW--"

                conn.request("POST", "/api/receive", params, header)

            elif url ==  "iptv/inject":###写死请求参数 form-data
                  params = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"context\"\r\n\r\n<?xml version=\"1.0\"" \
                             " encoding=\"UTF-8\"?><ccsc><cust_id>WS00000002</cust_id><passwd>dda1f51bdd1ccea03d6dba62066a1e36</passwd><item_id value=\"" \
                             "CP23010020171122018611\"><site>115</site><source_path>http://125.210.119.64/data24/ott/346/2017-11/23/1511419287676_625320.ts" \
                             "</source_path><publish_path>http://vodfree-bj.wasu.cn/data24/ott/346/2017-11/23/1511419287676_625320.ts</publish_path>" \
                             "<md5>18d3766ac484bec9f915c720661d6652</md5><priority>3</priority></item_id></ccsc>\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                             "Content-Disposition: form-data; name=\"op\"\r\n\r\npublish\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

                  conn.request("POST", "/iptv/inject", params, header)

            elif url == "hls/inject":##写死请求参数 form-data
                    logging.info("URL:%s"%url)
                    params = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"context\"\r\n\r\n<?xml version=\"1.0\" " \
                             "encoding=\"UTF-8\"?><ccsc><cust_id>WS00000002</cust_id><passwd>dda1f51bdd1ccea03d6dba62066a1e36</passwd>" \
                             "<item_id value=\"CP23010020171122018611\"><site>115</site><source_path>http://125.210.119.64/data24/ott/346/2017-12/23/1511419287676_625320.ts" \
                             "</source_path><publish_path>http://vodfree-bj.wasu.cn/data24/ott/346/2017-12/23/1511419287676_625320.ts</publish_path><md5>18d3766ac484bec9f915c720661d6652</md5>" \
                             "<priority>3</priority></item_id></ccsc>\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
                             "name=\"op\"\r\n\r\npublish\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

                    conn.request("POST", "/hls/inject", params, header)

            response = conn.getresponse()
            response_info = response.read().decode('utf-8')## decode函数对获取的字节数据进行解码
            status_code = response.getcode()
            logging.info("返回code%s" %status_code)
            logging.info("response_info:%s"%response_info)

            return response_info,status_code
        except Exception as e:
            logging.info(e)

        return {}
    # def httpspost(self, url, params):
    #     https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))##ssl https方式
    #     opener = urllib.request.build_opener(https_sslv3_handler)
    #     urllib.request.install_opener(opener)
    #
    #     data = json.dumps(eval(params))
    #     data = data.encode('utf-8')
    #     url = 'https://' + self.host + ':' + str(self.port)  + url
    #
    #     try:
    #         request = urllib.request.Request(url, headers=self.headers)
    #         response = urllib.request.urlopen(request, data)
    #         response = response.read().decode('utf-8')
    #         json_response = json.loads(response)
    #         return json_response
    #     except Exception as e:
    #         print('%s' % e)
    #         return {}


    # 封装HTTP xxx请求方法
    # 自由扩展
