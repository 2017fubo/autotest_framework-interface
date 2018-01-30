# -*- coding:utf-8 -*-
__author__ = 'fubo'
import unittest
from importlib import import_module
import sys,os
import imp
from Tools import TestobjectReadWriter
from Tools import Module_import

class  RunCase:

    def __init__(self,case_name,run_mode,run_case_list,testcase_file,test_sheet,driver):
        self.case_name = case_name
        self.run_mode = run_mode
        self.run_case_list = run_case_list
        self.testcase_file = testcase_file
        self.test_sheet = test_sheet
        self.Ln_driver = driver

    def run_case(self):
        testcase_file = self.testcase_file
        test_sheet = self.test_sheet
        result_info_list = []
        reason_info_list = []
        case_list = []
        if 0 == self.run_mode:#指定实施
            for case_id in self.run_case_list:
                print('caseID:%s' %case_id)
                if case_id<10:
                    case_id = self.case_name + '0'+ str(case_id)
                    case_id = str(case_id)
                else:
                    case_id = self.case_name + str(case_id)
                    case_id = str(case_id)

                print(case_id)
                Ex_module_name = case_id
                curpath = os.path.abspath('.')
                testcase_path = "%s/%s" % (curpath, "testcase")
                print('当前路径%s'%testcase_path)
                sys.path.append(testcase_path)
                try:
                    a = __import__(Ex_module_name)
                    tmp = 0
                except Exception as e:
                    print('该test案例不存在%s', e)
                    tmp = 1
                if tmp == 0:
                    aa = a.TestWebCase(self.Ln_driver,self.testcase_file,self.test_sheet)
                    #aa = a.TestWebCase(self.testcase_file, self.test_sheet)
                    result_info = aa.test()
                    result = result_info[0]
                    reason = result_info[1]
                    print(result, reason)
                    result_info_list.append(result)
                    reason_info_list.append(reason)
                    case_list.append(case_id)
                else:
                    print('测试案例不存在，请确认后重新实施！')
        else:
            if 1 == self.run_mode:#全实施
                testcase_sheet = TestobjectReadWriter.ReadWriter_ecxel(testcase_file,test_sheet)
                self.case_list = testcase_sheet.read_excel_caseinfo()

                for case_id in self.case_list:
                    print('/r/n %s'%case_id)
                    if case_id == None:
                        print('CaseID为空，不执行')
                    else:
                        #case_id = self.case_name + str(case_id)
                        #case_id = str(case_id)
                        Ex_module_name = case_id
                        curpath = os.path.abspath('.')
                        testcase_path = "%s/%s" % (curpath, "testcase")
                        # 动态的添加库路径
                        sys.path.append(testcase_path)
                        try:
                            a = __import__(Ex_module_name)
                            tmp = 0
                        except Exception as e:
                            print('该test案例不存在%s', e)
                            tmp = 1

                        if tmp == 0:
                            ##aa = a.TestWebCase(self.Ln_driver,self.testcase_file,self.test_sheet)
                            aa = a.TestWebCase(self.Ln_driver,self.testcase_file, self.test_sheet)
                            result_info = aa.test()
                            result = result_info[0]
                            reason = result_info[1]
                            print(result,reason)
                            result_info_list.append(result)
                            reason_info_list.append(reason)
                            case_list.append(case_id)
                        else:
                            print('测试案例不存在，请确认后重新实施！')


        return case_list,result_info_list