#coding:utf-8

import time,traceback,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Tools import Connect_db as Connect_db
import unittest
from rizhi import log_config as a
import logging

class boss_cdn_dns(unittest.TestCase):

    def setUp(self):
        # 登录
        self.driver = Driver
        self.errorfile_path = "E:\SinoBBD_供销大数据\AUTOTEST\Web Autoest FW\TestResult\error_添加域名.png"
        self.url = "http://test-boss.bbdcdn.net"

        # 读取用户登录信息
    # def get_login_info(self):
    #     log_msg = a.RiZhi()
    #     log_msg.log_def()
    #     print('get_login_info')
    #     #登录
    #     pass

    def test_login_(self):
        log_msg = a.RiZhi()
        log_msg.log_def()
        titleinfo = '域名列表'
        username = 'bo.fu'
        password = 'Jtw1ASoZFQsj'
        # url = "http://bbd.boss.com:88/AdminUser/login"
        # url = "http://test-boss.bbdcdn.net"
        ##全局中定义

        try:
            logging.info('_login_')
            #print('_login_')
            self.driver.get(self.url)
            time.sleep(5)
            print('输入用户名密码')
            #self.driver.find_element_by_id("bdb-login-username").clear()
            self.driver.find_element_by_id("bdb-login-username").send_keys('%s' %username)
            #输入用户名
            #self.driver.find_element_by_id("bdb-login-pwd").clear()
            self.driver.find_element_by_id("bdb-login-pwd").send_keys('%s' %password)
            # 输入密码
            print('点击登陆')
            self.driver.find_element_by_id("bdb-login-btn").click()
            self.driver.implicitly_wait(20)

        except Exception as e:
            print('登录失败1！%s' %e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            self.driver.close()
            sys.exit()

        # 账号登录
        #assert '域名列表' in self.driver.title
        title_info= self.driver.title
        print(title_info)
        if title_info == titleinfo or title_info == "sinobbd-boss":
            print('登录成功！')
            # 准备数据
        else:
            print('登录失败2！')
            self.driver.get_screenshot_as_file(self.errorfile_path)
            self.driver.close()
            sys.exit()

    def pre_data(self):
        print('pre_data')
        pass
    def _addinnerDomain_(self):
        pass

    def _addtemplated_(self):

        templated_link = self.url + "/CustomerDomainTemplate/domainTemplateList"
        try:
            #获取域名下的三个sub菜单位置
            links = self.driver.find_elements_by_tag_name("a")
            print("get links success!")

            for link in links:
                sub_menu = link.get_attribute("href")
                print(sub_menu)
                if sub_menu == templated_link:
                    time.sleep(10)
                    print("entry templated list")
                    link.click()
                    self.driver.implicitly_wait(20)
                    break
                else:
                    continue
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

        try:
            print("add templated")
            time.sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]").click()
            self.driver.implicitly_wait(20)
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

        ##验证添加功能界面启动与否
        # try:
        #     print("get diaog title info_title")
        #     addtemplate_title = self.driver.find_element_by_css_selector(".title.bdb-p-r.bdb-f-c-fff").text
        #     print(addtemplate_title)
        #     if addtemplate_title=="添加源站模板":
        #         pass
        #     else:
        #         print("启动画面错误")
        #         self.driver.get_screenshot_as_file(self.errorfile_path)
        #
        # except Exception as e:
        #     print('进入页面错误%e' %e)
        #     self.driver.get_screenshot_as_file(self.errorfile_path)
        #     sys.exit()
        ##关闭添加对话框

        try:
            self.driver.find_element_by_xpath(".//*[@id='bdb-domain-tpl-add-form']/img").click()
        except Exception as e:
            print('关闭添加对话框失败%e' % e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

    def _adddomain_(self):
        productId_xpath = "/html/body/div[1]/div[2]/div/div[6]/form/div[2]/div[1]/div[1]/div/select/option[2]"
        templateId_xpath = "/html/body/div[1]/div[2]/div/div[6]/form/div[2]/div[1]/div[3]/div/select/option[2]"
        first_step_xpath = "/html/body/div[1]/div[2]/div/div[6]/form/div[3]/button"

        domainList_link = self.url +"/CustomerDomainManager/domainList"
        try:
            # 获取域名下的三个sub菜单位置
            links = self.driver.find_elements_by_tag_name("a")
            print("get links success!")

            for link in links:
                sub_menu = link.get_attribute("href")
                print(sub_menu)
                if sub_menu == domainList_link:
                    time.sleep(10)
                    print("entry templated list")
                    link.click()
                    self.driver.implicitly_wait(20)
                    break
                else:
                    continue
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

        try:
            print('添加域名')
            time.sleep(3)
            self.driver.find_element_by_xpath(".//*[@id='bdb-domain-add']").click()
            self.driver.implicitly_wait(20)

        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

        #添加域名
        # print("input message infomation")
        # #self.driver.switch_to.frame("bdb-domain-add-first-form")
        #
        try:
            print("input productId")
            self.driver.find_element_by_xpath(productId_xpath).click()
            productid_text = self.driver.find_element_by_xpath(productId_xpath).text

            print("选择产品信息：%s" % productid_text)
            self.driver.implicitly_wait(5)

            print("input icp")
            self.driver.find_element_by_xpath("//*[@id=\"icp\"]").send_keys("anyinput")
            self.driver.implicitly_wait(3)

            print("select 源站模板")
            self.driver.find_element_by_xpath(templateId_xpath).click()

            print("input 加速 domain")
            time_now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            self.driver.find_element_by_xpath("//*[@id=\"domains\"]").send_keys("test.fubo%s.com" %time_now)
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()

        try:
            print("next step")
            self.driver.find_element_by_xpath(".//*[@id='bdb-domain-add-first-form']/div[3]/button").click()
            self.driver.implicitly_wait(30)
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()
        # info_Title = self.driver.find_element_by_css_selector("#bdb-domain-product-text>span").text
        # #info_Title = self.driver.find_element_by_(".//*[@id='bdb-domain-product-text']/span").text
        # print("产品信息：%s" % info_Title)
        # if info_Title == productid_text:
        #     print("next screen show is success!!")
        # else:
        #     print("next screen show isn't success!!")
        #     sys.exit()
        try:
            self.driver.find_element_by_xpath(".//*[@id='bdb-domain-add-second-form']/div[3]/button[2]").click()
            self.driver.implicitly_wait(30)
            time.sleep(3)

        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file(self.errorfile_path)
            sys.exit()
        print("add domain success!!!")

    ##连接数据库方法
    def _Connect_db_(self):
        try:
            print("getDB")
            db_connect = Connect_db.GetDB()
            print("conn_mysql")
            db_conn = db_connect.conn_mysql()
            print("connect success!!")
        except Exception as e:
            print("Mysql connect Fail %s" %e)
            sys.exit()

        cursor = db_conn.cursor()
        return  cursor,db_conn

    ##删除测试数据方法：domain
    def _deletetestdata_domain_(self,cursor,db_conn):
        ##查询数据
        print("Select...")
        cursor.execute('SELECT * FROM customer_domain')
        Select_info = cursor.fetchall()
        length = len(Select_info)
        print("域名数量:%s" %length)

        ##删除测试数据
        try:
            print("Delete...")
            sql_del = "Delete from `customer_domain` where domain_name like 'test.fubo%'"
            cursor.execute(sql_del)
            # info = cursor.fetchall()
            # print(info)

            cursor.execute('commit')
            # delete_info = cursor.fetchall()
            # length = len(delete_info)
            # print("删除测试域名数据 %s" %length)
            print("Delete success!!")
        except Exception as e:
            print("delete Fail Or don't Test data for delete: %s" % e)
            cursor.execute('rollback')
            # sys.exit()

        ##s删除后剩余条数
        cursor.execute("SELECT * FROM `customer_domain`")
        Select_info = cursor.fetchall()
        length = len(Select_info)
        print("测试数据删除后，剩余域名数量:%s" % length)

        cursor.close()
        db_conn.close()

    ##删除测试数据方法：Template

    def _deletetestdata_addtemplated_(self, cursor, db_conn):
        ##查询数据
        print("Select...")
        cursor.execute('SELECT * FROM customer_domain_template')
        Select_info = cursor.fetchall()
        length = len(Select_info)
        print("域名数量:%s" % length)

        ##删除测试数据
        try:
            print("Delete...")
            sql_del = "Delete from `customer_domain_template` where domain_name like 'test.fubo%'"
            cursor.execute(sql_del)
            # info = cursor.fetchall()
            # print(info)
            cursor.execute('commit')
            # delete_info = cursor.fetchall()
            # length = len(delete_info)
            # print("删除测试域名数据 %s" %length)
            print("Delete success!!")
        except Exception as e:
            print("delete Fail Or don't Test data for delete: %s" % e)
            cursor.execute('rollback')
            # sys.exit()

        ##s删除后剩余条数
        cursor.execute("SELECT * FROM `customer_domain_template`")
        Select_info = cursor.fetchall()
        length = len(Select_info)
        print("测试数据删除后，剩余域名数量:%s" % length)
        cursor.close()
        db_conn.close()

if __name__ == '__main__':
    Driver = webdriver.Firefox()
    aa = boss_cdn_dns()
    # 登录
    aa._login_()
    #
    #添加源站模板

    aa._addtemplated_()

    # 添加域名
    aa._adddomain_()

    # ##连接并删除测试数据
    #
    # curser,db_conn = aa._Connect_db_()
    #
    # #删除Testdata:domain
    # aa._deletetestdata_domain_(curser,db_conn)

    #退出浏览器
    Driver.quit()