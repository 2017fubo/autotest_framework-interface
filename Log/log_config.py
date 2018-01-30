# -*- coding:utf-8 -*-

__author__ = 'fubo'
import logging

class RiZhi:
    def __init__(self):
        pass

    def log_def(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')
        # print("log test tag1......................")

        console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        console.setLevel(logging.DEBUG)
        # print("log test tag2......................")
        formatter = logging.Formatter('%(name)-12s:%(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        return