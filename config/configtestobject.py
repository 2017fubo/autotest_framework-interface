# -*- coding:utf-8 -*-

__author__ = '付波'

import configparser

class TestObject:

    def __init__(self, run_case_config_file):

        config = configparser.ConfigParser()
        config.read(run_case_config_file)
        
        try:
            self.testcase_file = config['TESTOBJECTCONFIG']['testcase_file']#.get("TESTOBJECTCONFIG","testcase_file")#
            #print(self.testcase_file )
            self.test_sheet = config['TESTOBJECTCONFIG']['test_sheet']#.get("TESTOBJECTCONFIG","test_sheet")#
            #print(self.test_sheet)

        except Exception as e:
            print('%s', e)

    def get_testcase_file(self):
        return self.testcase_file

    def get_testsheet(self):
        return  self.test_sheet