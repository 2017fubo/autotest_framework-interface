# -*- coding:utf-8 -*-
__author__ = '付波'
import traceback, types

class loader(object):
    def __init__(self,path):
        #self.path = r'E:\9F\Busautotest\Web\Bus\testcase\\' + 'KFQX010' + str(path) + '.py'
        print(self.path)

    def load(self, name):
        try:
            m = types.ModuleType(name)
            exec(open(self.path).read() in m.__dict__)
            return m
        except:
            print("Load module [path %s] error: %s"
                  % (self.path, traceback.format_exc()))
            return None