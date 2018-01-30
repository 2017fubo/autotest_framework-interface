# -*- coding:utf-8 -*-
__author__ = 'fubo'
import urllib.request
import http.cookiejar
import urllib.parse
import json
from urllib.request import HTTPBasicAuthHandler

import configparser
import ssl
from rizhi import log_config as a
import logging


class ConfigHttp:

    def __init__(self):
        # config = configparser.ConfigParser()
        # config.read(ini_file)
        # print(ini_file)
        self.host = '121.42.147.39' #预发
        self.port = '' #http
        self.headers = {}  # http 头
        #install cookie
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
    
    #https

    def get_host(self):
        return self.host

    def get_port(self):
        return  self.port

    # 设置http头
    def set_header(self):
        self.headers = self.headers

    ## 带headers 权鉴
    def http_post_headers(self, url, params,token):
        self.headers = {
            'Content-Type' : "application/json",
            'Authorization' : "%s" %token
        }
        logging.info(self.headers)
        data = json.dumps(eval(params))
        data = data.encode('utf-8')
        logging.info('变换后的请求参数：%s' % data)
        request = urllib.request.Request(url,headers=self.headers)
        response = urllib.request.urlopen(request,data)
        response = response.read().decode('utf-8')

        json_response = json.loads(response)
        return json_response

    def post(self, url, data):
        if data == None:
            logging.info(".................没有参数的post请求.......................")
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response
        else:
            logging.info(data)
            data = urllib.parse.urlencode(eval(data))#将参数转为url编码字符串
            data = data.encode('utf-8')
            logging.info('变换后的请求参数：%s'%data)
            request = urllib.request.Request(url,headers=self.headers)
            response = urllib.request.urlopen(request, data)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response

    def post_auth(self, url, data):###自建与hoss信息提供相关接口使用
        data = json.dumps(eval(data))
        data = data.encode('utf-8')
        logging.info('变换后的请求参数：%s' % data)

        self.headers = {"Content-type": "application/json"}
        if data == None:
            logging.info(".................没有参数的post请求.......................")
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response
        else:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request, data)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response
    #
    # def httpspost(self, url, params):
    #     https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv3))##ssl https方式
    #     opener = urllib.request.build_opener(https_sslv3_handler)
    #     urllib.request.install_opener(opener)
    #     data = json.dumps(eval(params))
    #     data = data.encode('utf-8')
    #     url = 'https://' + self.host + ':' + str(self.port)  + url
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