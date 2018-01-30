import os
import logging


# api请求地址相关信息定义类
# ###api url address infomation ####

class API2_0_Request_urlinfo:

    def intl_rquest_url(self):

    # 测试request_url
    #internal 接口地址全量
        #portal
        intl_api_url = ["internal/flowTerminal",##ID 01 CS终端流量查询
                          "internal/purge_list",##ID 02 cs系统刷新任务列表请求接口
                          "internal/purge_all_list",  ##ID 03 Boss系统刷新任务列表请求接口
                          "internal/preload_list",##ID 04 cs系统预缓存任务列表
                          "internal/preload_all_list",  ##ID 05 Boss系统预缓存任务列表
                          "internal/preload_set",  ##ID 06_ boss预缓存系统强制刷新
                          "internal/inject_list",##ID 07 cs内容注入任务列表请求接口
                          "internal/inject_all_list",  ##ID 08_ boss内容注入任务列表请求接口
                          "internal/inject_set",  ##ID 09_ boss预注入任务强制刷新
                          "internal/log_select",  ##ID 10_ 融合日志查询
                          "internal/userInfo",##ID 12 获取boss用户信息并缓存
                          "internal/purge", ##ID 13 cs刷新任务
                          "internal/preload",##ID 14 cs系统预缓存
                          "internal/flow_manu",##ID 15 请求分厂商获取流量
                          "internal/getHttpCode",##ID 17 根据域名获取http状态码
                          "internal/getBaseInjectList",##ID 18 获取未发送的任务状态--injectList
                          "internal/getBaseInjectSyncList",##ID 19获取未发送的任务状态(injectsynclist)
                          "internal/getDomainList",  ## 20 全量域名获取
                          ]

        return  intl_api_url
    #
    # def intl_rquest_url_boss(self):
    #     # 测试request_url
    #     # internal 接口地址 全量
    #     # portal
    #     boss_api_url = [
    #
    #                     ]
    #     return boss_api_url

    def Out_request_url(self):
        out_api_url =["api/purge",###id 1 刷新接口
                      "port/newTasksNotice", ##id 2 回调接口-刷新
                      "api/purge?",##id 3刷新查询接口 Get
                      "api/inject",##id 4 注入接口
                      "api/inject?",##id 5 注入查询接口 Get
                      "port/newInjectTasks",##id6 回调接口-（注入回调）
                      "api/preload",##id 7 预缓存接口
                      "port/newTasksNotice",##id 8 回调接口-（预缓存）
                      "api/preload?",  ##id 9 预缓存查询接口 Get
                      "api/bandwidth",## id 10 域名请求带宽查询 get
                      "api/receive",## id 11注入接口(华数fds注入)
                      "api/flow",##id 12流量查询接口
                      "api/downloadLog",  ##id 13流量查询接口
                      "iptv/inject",  ##id 14 IPTV注入
                      "hls/inject",  ##id 15 HLS切片
                      "port/selfPurgeEdge", ##id 16 回调接口-（-自建父层刷新成功回调刷新边缘）
                      "api/inject_upeng"##id 16 回调接口-（-自建父层刷新成功回调刷新边缘）
                      ]
        return out_api_url

    def request_method(self):
        get = "GET"
        post = "POST"

        return get, post