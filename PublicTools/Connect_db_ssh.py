# -*- coding:utf-8 -*-
__author__ = 'fubo'

import mysql.connector
from sshtunnel import SSHTunnelForwarder
from config import globalconfig

class GetDB:
    def __init__(self):
        pass

    def conn_mysql(self):
        print('获取db信息...')
        config = globalconfig.Global()
        print('11111')
        db_info = config.get_conn_ssh()

        host = db_info[0]
        port = db_info[1]
        user = db_info[2]
        passwd = db_info[3]
        db = db_info[4]
        sshhost = db_info[5]
        sshuser = db_info[6]
        sshpasswd = db_info[7]
        print(host,port,user,passwd,db,sshhost,sshuser,sshpasswd)

        server = SSHTunnelForwarder(
            ssh_address_or_host=(sshhost, 22), #
            ssh_username=sshuser,  #
            ssh_password=sshpasswd,  #
            remote_bind_address=(host, 3306))
        server.start()

        conn = mysql.connector.connect(host='127.0.0.1',
                                       port=server.local_bind_port,
                                       user=user,
                                       passwd=passwd,
                                       db=db)
        return server, conn