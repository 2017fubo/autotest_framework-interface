# -*- coding:utf-8 -*-
__author__ = 'fubo'

import mysql.connector
from config import globalconfig

class GetDB:
    def __init__(self):
        pass

    def conn_mysql(self):

        print('获取db信息...')
        config = globalconfig.Global()
        print('11111')
        db_info = config.get_conn()

        print(db_info)
        host = db_info[0]
        print(host)
        port = db_info[1]
        user = db_info[2]
        passwd = db_info[3]
        db = db_info[4]
        print(host,port,user,passwd,db)

        try:
            conn =  mysql.connector.connect(
                host = host,
                port = port,
                user = user,
                passwd = passwd,
                db=db)
        except Exception as e:
            print(e)

        return conn