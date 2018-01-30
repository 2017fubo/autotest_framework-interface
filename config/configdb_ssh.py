# -*- coding:utf-8 -*-

__author__ = 'fubo'

import configparser

class GetDB:
    def __init__(self, ini_file):

        config = configparser.ConfigParser()

        config.read(ini_file)

        try:
            self.host = config['DATABASE']['host']
            print(self.host)
            self.port = config['DATABASE']["port"]
            self.user = config['DATABASE']["user"]
            self.passwd = config['DATABASE']["passwd"]
            self.db = config['DATABASE']["db"]
            self.charset = config['DATABASE']["charset"]
            self.sshhost = config['DATABASE']["sshhost"]
            self.sshuser = config['DATABASE']["sshuser"]
            self.sshpasswd = config['DATABASE']["sshpasswd"]

        except Exception as e:
            print('%s', e)

    def get_conn(self):
        return self.host, self.port, self.user, self.passwd, self.db, self.sshhost, self.sshuser, self.sshpasswd
