# -*- coding:utf-8 -*-

__author__ = '付波'

import configparser

class ConfigRunMode:
    def __init__(self, run_case_config_file):
        config = configparser.ConfigParser()

        config.read(run_case_config_file)
        
        try:
            self.case_name = config['RUNCASECONFIG']['casename']
            #print(self.case_name)
            self.run_mode = config['RUNCASECONFIG']['runmode']
            self.run_mode = int(self.run_mode)
            #print(self.run_mode)
            self.case_list = config['RUNCASECONFIG']['case_id']
            #print(self.case_list)
            self.case_list = eval(self.case_list)

        except Exception as e:
            print('%s', e)

    def get_run_mode(self):
        return self.run_mode

    def get_case_list(self):
        return  self.case_list

    def get_case_name(self):
        return  self.case_name