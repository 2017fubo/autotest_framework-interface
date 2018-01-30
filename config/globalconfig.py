# -*- coding:utf-8 -*-
__author__ = 'fubo'
from config import configrunmode,configtestobject,configdb,configdb_ssh
import  os

class Global:

    def __init__(self):
        path = os.path.abspath(os.curdir)
        #print(path)
        pass

    def get_case_name(self):
        return self.run_mode_config.get_case_name()

    def get_run_mode(self):
        runmode_config_path = self.path + '\\' + 'config\\runmode_config.ini'
        self.run_mode_config = configrunmode.ConfigRunMode(runmode_config_path)
        return self.run_mode_config.get_run_mode()

    #
    def get_run_case_list(self):
        return self.run_mode_config.get_case_list()
    #
    def get_testcase_file(self):
        runtest_object_path = self.path + '\\'+'config\\testobject_config.ini'
        self.run_test_object = configtestobject.TestObject(runtest_object_path)
        return self.run_test_object.get_testcase_file()

    def get_testsheet(self):
        return self.run_test_object.get_testsheet()

    def get_conn(self):
        path = os.path.abspath(os.curdir)
        db_conn_path = path + '\\' + 'config\\database_config.ini'
        self.db_conn = configdb.GetDB(db_conn_path)
        print(db_conn_path)
        return self.db_conn.get_conn()

    def get_conn_ssh(self):
        db_ssh_cnn_path = self.path + '\\' + 'config\\database_config_ssh.ini'
        self.db_conn_ssh = configdb_ssh(db_ssh_cnn_path)
        return  self.db_conn_ssh.get_conn()