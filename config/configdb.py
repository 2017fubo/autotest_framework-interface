# -*- coding:utf-8 -*-

__author__ = 'fubo'

import configparser

class GetDB:
    def __init__(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file)
        print(ini_file)
        try:
            print("Start read config file...")
            # self.host = config['DATABASE']['host']
            # self.port = config['DATABASE']["port"]
            # self.user = config['DATABASE']["user"]
            # self.passwd = config['DATABASE']["passwd"]
            # self.db = config['DATABASE']["db"]
            self.host = '127.0.0.1'
            self.port = 3306
            self.user = 'root'
            self.passwd = 'root'
            self.db = 'bbd_boss'

        except Exception as e:
            print('%s', e)

    def get_conn(self):
        return self.host, self.port, self.user, self.passwd, self.db