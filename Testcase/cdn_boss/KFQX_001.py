#coding:utf-8

import time,traceback,sys
from selenium.webdriver.common.keys import Keys
from Tools import TestobjectReadWriter
from Sharelibs import  login,exitlogin
from Tools import Connect_db_ssh

class TestWebCase:
    def __init__(self, driver,testcase_file, test_sheet):
        self.driver = driver
        self.testcase_file = testcase_file
        self.test_sheet = test_sheet
        print('进入测试case')
        self.server, self.conn = Connect_db_ssh.GetDB().conn_mysql()
        self.cursor = self.conn.cursor()
        self.verificationErrors = []
        self.accept_next_alert = True

        # 读取用户登录信息
    def get_login_info(self):
        print('读取登录信息')
        login_info = TestobjectReadWriter.ReadWriter_ecxel(self.testcase_file, self.test_sheet)  # 读写
        row = 3  ##根据用例写入
        col = 'G'  ##根据用例写入
        Login_info = login_info.read_excel_logininfo(row, col)
        self.Login_username = Login_info[0]
        self.Login_password = Login_info[1]
        print(self.Login_username, self.Login_password)

        # 准备数据
    def pre_data(self):
        #录单信息
        self.customer_Name = "王丽"
        self.cert_Id = '62010519801228002X'
        #其他机构的inst_code
        self.INST_CODE="11010102"
        #其他机构的产品名称
        self.PRODUCT_NAME="薪易贷"
        #其他客服用户名
        self.CREATOR="zidonghuaer"
        #插入时间
        timeTemp = time.time()
        timeTempNext = time.localtime(timeTemp)
        self.curtime = time.strftime("%Y-%m-%d %H:%M:%S", timeTempNext)
        self.FuYiGongDanChaXun_Other_APP_ID = "20207410"

    def test(self):
        self.pre_data()
        self.get_login_info()
        login_bus = login.Login(self.Login_username, self.Login_password, self.driver)
        login_bus.login()
        self.Driver = self.driver
        try:
            self.MySQL_Insert_Into()
            self.MySQL_Query_Before()
            # 录单管理-其他客服zidonghuaer创建的APP_ID
            self.LuDanGuanLi_Other_APP_ID = self.MySQL_Insert_Into_Select()
            # 工单查询(客服)-其他客服zidonghuaer创建的APP_ID
            self.GongDanChaXunKF_Other_APP_ID = self.MySQL_Insert_Into_Select()
        except:
            pass
        try:
            self.LuDan()
        except:
            pass
        try:
            self.LuDanGuanLi(self.LuDanGuanLi_Other_APP_ID)
        except:
            pass
        try:
            self.GongDanChaXunKF(self.GongDanChaXunKF_Other_APP_ID)
        except:
            pass
        try:
            self.FuYiGongDanChaXun(self.FuYiGongDanChaXun_Other_APP_ID)
        except:
            pass
        testrestult,reason = self.result_confirm()
        print(testrestult,reason)
        exit_login = exitlogin.Exitlogin(self.driver)
        exit_login.exitlogin()
        if testrestult == "pass":
            try:
                self.MySQL_Delete()
            except:
                pass
        else:
            print("权限验证失败，数据库数据保留")
            print('关闭数据库服务')
            self.cursor.close()
            self.conn.commit()
            self.conn.close()
            self.server.stop()
        return testrestult,reason

    def result_confirm(self):
        reason=[]
        print("==========实际结果与预期结果对比=============")

        #贷前管理——录单
        try:
            if self.MySQL_APP_ID == "11010101" and self.a=="success" and self.abc=="":
                testresult_LuDan = 'pass'
                print("贷前管理—录单:pass", end='')
            else:
                print("贷前管理—录单:fail", end='')
                testresult_LuDan = 'fail'
                if testresult_LuDan == 'fail' and self.MySQL_APP_ID != "11010101":
                    reason.append("贷前管理-录单：工单编号与所属机构不符")
                elif testresult_LuDan == 'fail' and self.a !="success":
                    reason.append("贷前管理-录单：录单失败")
                elif testresult_LuDan == 'fail' and self.abc != "":
                    reason.append("贷前管理-录单：工单查询(客服)查询时可以获取其他客服的工单编号")
        except:
            testresult_LuDan = 'fail'
            print("贷前管理—录单:程序异常")
            print('贷前管理—录单:fail', end='')
            reason.append("贷前管理—录单:程序异常")

        #贷前管理—录单管理
        try:
            if self.LuDanGuanLi_APP_ID == "":
                print("贷前管理-录单管理:pass")
                testresult_LuDanGuanLi = 'pass'
            else:
                print("贷前管理-录单管理:fail")
                testresult_LuDanGuanLi = 'fail'
                reason.append( '贷前管理-录单管理:可以获取其他客服的工单编号')
                print(self.LuDanGuanLi_APP_ID)
        except:
            print("贷前管理-录单管理:程序异常")
            print('贷前管理-录单管理:fail', end='')
            testresult_LuDanGuanLi = 'fail'
            reason.append("贷前管理-录单管理:程序异常")

        #贷前管理-工单查询（客服）
        try:
            if self.GongDanChaXunKF_APP_ID == "":
                print("贷前管理-工单查询(客服):pass")
                testresult_GongDanChaXunKF = 'pass'
            else:
                testresult_GongDanChaXunKF = 'pass'
                reason.append('贷前管理-工单查询(客服):可以获取其他客服的工单编号')
                print("贷前管理-工单查询(客服):fail")
        except:
            print("贷前管理-工单查询(客服):程序异常")
            print('贷前管理-工单查询(客服):fail', end='')
            testresult_GongDanChaXunKF = 'fail'
            reason.append("贷前管理-工单查询(客服):程序异常")

        #贷前管理-复议工单查询
        try:
            if self.FYGDCXGL_APP_ID == "":
                print("贷前管理-复议工单查询管理:pass")
                testresult_FYGDCXGL = 'pass'
            else:
                testresult_FYGDCXGL = 'fail'
                reason.append( '贷前管理-复议工单查询管理:可以获取其他客服的工单编号')
                print("贷前管理-复议工单查询管理:fail")
        except:
            print("贷前管理-复议工单查询管理:程序异常")
            print('贷前管理-复议工单查询管理:fail', end='')
            testresult_FYGDCXGL = 'fail'
            reason.append("贷前管理-复议工单查询管理:程序异常")

        if testresult_LuDan=="pass" and testresult_LuDanGuanLi=="pass" and testresult_GongDanChaXunKF=="pass" and testresult_FYGDCXGL=="pass":
            testresult="pass"
        else:
            testresult="fail"

        return testresult,reason
    #数据库插入数据
    def MySQL_Insert_Into(self):
        try:
            self.cursor.execute(
                "INSERT INTO `pre_loan_db`.`t_lon_application` VALUES ('', NULL, NULL, 'JFB', NULL, 'F0200', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '" + str(
                    self.INST_CODE) + "', '3', NULL, NULL, NULL, NULL, '1000', NULL, '668810', '" + str(
                    self.customer_Name) + "', NULL, NULL, NULL, 'B1301', '" + str(
                    self.cert_Id) + "', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', NULL, NULL, NULL, '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '104', '10', '" + str(
                    self.PRODUCT_NAME) + "', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'F4101', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'BasicOrderProcess:2:17524', NULL, 'B1701', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'F3501', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1', '1', '1', '1', NULL, NULL, '1', '1', '0', NULL, '/bizpage/loanbefore/instancejsp/recorder/20161014_1552_record_104.jsp', '/bizpage/loanbefore/instancejsp/check/20161014_1552_check_104.jsp', '/bizpage/loanbefore/instancejsp/show/20161014_1552_show_104.jsp', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '" + str(
                    self.CREATOR) + "', '" + str(
                    self.curtime) + "', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N8701', 'N8701', '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '" + str(
                    self.curtime) + "', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '100022611410', NULL, NULL, NULL, NULL, NULL, 'C', 'N8702', '1', NULL, NULL, NULL, 'B154001', NULL, NULL, 'c2103bd7-759c-477c-ab15-810d96213d03', NULL, NULL)")
            self.conn.commit()
        except Exception as e:
            print(e)
            print('capture exception %s' % "插入数据失败")

    #查询插入数据的APP_ID
    def MySQL_Insert_Into_Select(self):
        # 查询其他机构的app_id
        try:
            print("获取其他机构插入的工单编号")
            self.cursor.execute(
                "SELECT APP_ID from t_lon_application where cert_id='" + str(self.cert_Id) + "' and INST_CODE ='" + str(
                    self.INST_CODE) + "'  ORDER BY CREATE_TIME DESC LIMIT 1")
            result_set = self.cursor.fetchall()
            if result_set:
                for x in result_set:
                    print(x[0])
                    return x[0]
        except Exception as e:
            print(e)
            print('capture exception %s' % "获取其他机构插入的工单编号失败")

    #数据库查询待录单用户的录单之前的工单总条数
    def MySQL_Query_Before(self):
        try:
            print("查询待录单用户的工单总数")
            self.cursor.execute(
                "SELECT COUNT(*) from t_lon_application where cert_id='%s'" % self.cert_Id)
            result_set = self.cursor.fetchall()
            self.pre_num = result_set[0][0]
            print("录单前此用户工单数为%s" % result_set[0][0])
            # 插入此用户其他机构的工单
            return self.pre_num

        except Exception as e:
            print(e)
            print('capture exception %s' % u"查询录单前该用户工单总条数失败")

    #数据库查询录单用户的通过bus系统录单之后的工单总条数
    def MySQL_Query_After(self):
        try:
            self.cursor.execute(
                "SELECT COUNT(*) from t_lon_application where cert_id='%s'" % self.cert_Id)
            result_set = self.cursor.fetchall()
            new_num = result_set[0][0]
            print(new_num)
            print("录单后工单总数为：%s" % new_num)
            if (new_num == (self.pre_num + 1)):
                self.a = "success"
                print("录单成功")
            else:
                print("验证录单失败")
                self.a = "fail"
                username = ''
                return (username)
            return self.a
        except Exception as e:
            print(e)
            print('capture exception %s' % u"查询录单后该用户工单总条数失败")

    #数据库查询通过bus系统录单后生成的APP_ID
    def MySQL_Select(self):
        try:
            print("连接数据库做查询")
            try:
                self.cursor.execute("SELECT INST_CODE FROM t_lon_application WHERE APP_ID='%s'" % self.APP_ID)
                result_set = self.cursor.fetchall()
                if result_set:
                    for row in result_set:
                        self.MySQL_APP_ID = row[0]
                        print(self.MySQL_APP_ID)
            except Exception as e:
                print(e)
                print('capture exception %s' % u"查询信息不存在")
                print('查询信息不存在')
        except Exception as e:
            print(e)
            print('capture exception %s' % u"数据库连接失败，获取客服权限信息失败")
            print('数据库连接失败，获取客服权限信息失败')

    #删除测试数据
    def MySQL_Delete(self):
        try:
            print("连接数据库做查询")
            try:
                self.cursor.execute("DELETE FROM t_lon_application WHERE CERT_ID='%s';" % self.cert_Id)
                print("删除测试数据成功")
                print('关闭数据库服务')
                self.cursor.close()
                self.conn.commit()
                self.conn.close()
                self.server.stop()
            except Exception as e:
                print(e)
                print('capture exception %s' % u"删除测试数据失败")
                print('删除测试数据失败')
        except Exception as e:
            print(e)
            print('capture exception %s' % u"数据库连接失败，删除测试数据失败")
            print('数据库连接失败，删除测试数据失败')

    #贷前管理-录单
    def LuDan(self):
        print("=========================================")
        print('贷前管理-录单')
        #开始录单
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('step1:点击贷前管理')
            self.Driver.find_element_by_id("span500").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理按钮未找到")
            self.Driver.get_screenshot_as_file("D:\\BusError\\error__贷前管理按钮页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('step2:点击录单')
            self.Driver.find_element_by_id("span500095").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-录单按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_进入录单页面.png")
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('    选择产品名称.....')
            self.Driver.find_element_by_id("productId")
            self.Driver.implicitly_wait(20)
            self.Driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/select/option[2]").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"产品名称下拉选项未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_产品名称.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('    录入用户身份信息.....')
            self.Driver.find_element_by_id("customerName").send_keys(self.customer_Name)
            self.Driver.find_element_by_id("certId").send_keys(self.cert_Id)
        except Exception as e:
            print(e)
            print('capture exception %s' % u"用户身份信息文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_录入身份信息.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('    选择借款人类型.....')
            borrowerTypeTextModel=self.Driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/select")
            borrowerTypeTextModel.find_element_by_xpath("//option[@value='B154001']").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"借款人文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_借款人类型.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('step3:点击查询按钮.....')
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul/li/input").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"查询按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_查询页面.png")
            print('点击查询按钮失败')
            traceback.print_exc()
            sys.exit()
        time.sleep(5)
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            for i in range(1,20):
                self.Driver.find_element_by_xpath("/html/body").send_keys(Keys.DOWN)
            self.Driver.implicitly_wait(5)
            print('step4:点击下一步按钮.....')
            self.Driver.find_element_by_xpath("/html/body/form/div[7]/div/ul/li[1]/input").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"下一步按钮未找到")
            time.sleep(5)
            self.Driver.get_screenshot_as_file("D:\BusError\error_下一步.png")
            print('点击下一步按钮失败')
            traceback.print_exc()
            sys.exit()
            #点击主页按钮，返回到主页
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('点击主页按钮，返回主页')
            self.Driver.find_element_by_xpath(".//*[@id='main']/div[2]/a").click()
        except Exception as e:
             print(e)
             print('capture exception %s' % u"主页按钮未找到")
             self.Driver.get_screenshot_as_file("D:\BusError\error_反回到主页.png")
             traceback.print_exc()
             sys.exit()
        try:
            try:
                # print('进入贷前管理页面')
                self.Driver.switch_to.default_content()
                self.Driver.switch_to.frame("fraLeft")
                # print('step1:点击贷前管理')
                self.Driver.find_element_by_id("span500").click()
            except Exception as e:
                print(e)
                print('capture exception %s' % u"贷前管理按钮未找到")
                self.Driver.get_screenshot_as_file("D:\BusError\error_贷前管理按钮页面.png")
                traceback.print_exc()
                sys.exit()
        except:
            pass

        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            # print('step2:点击录单')
            self.Driver.find_element_by_id("span500095").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-录单按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_进入录单页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            # print('    选择产品名称.....')
            self.Driver.find_element_by_id("productId")
            self.Driver.implicitly_wait(20)
            self.Driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/select/option[2]").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"产品名称下拉选项未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_产品名称.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            # print('    录入用户身份信息.....')
            self.Driver.find_element_by_id("customerName").send_keys(self.customer_Name)
            self.Driver.find_element_by_id("certId").send_keys(self.cert_Id)
        except Exception as e:
            print(e)
            print('capture exception %s' % u"用户身份信息文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_录入身份信息.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            # print('    选择借款人类型.....')
            borrowerTypeTextModel=self.Driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/select")
            borrowerTypeTextModel.find_element_by_xpath("//option[@value='B154001']").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"借款人文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_借款人类型.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            # print('step3:点击查询按钮.....')
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul/li/input").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"查询按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_查询页面.png")
            print('点击查询按钮失败')
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        self.MySQL_Query_After()
        if self.a=="success":
            try:
                self.Driver.switch_to.default_content()
                self.Driver.switch_to.frame("fraMain")
                print('获取工单编号信息.....')
                a=self.Driver.find_element_by_css_selector("html body form#recorderForm div#connectRecorde table#tblResultOfSglTbl.simpleListTable.pagesortable.msgrids tbody tr:last-child")
                self.APP_ID=a.find_element_by_css_selector("#tblResultOfSglTbl>tbody>tr>td:first-child").text
                print(self.APP_ID)
            except Exception as e:
                print(e)
                print('capture exception %s' % u"工单编号未获取到")
                self.Driver.get_screenshot_as_file("D:\BusError\error_工单编号.png")
                print('获取工单编号失败')
                traceback.print_exc()
                sys.exit()
        else:
            print("验证录单失败,不执行获取工单编号验证录单权限")

        self.MySQL_Select()
        self.abc=self.GongDanChaXunKF(self.GongDanChaXunKF_Other_APP_ID)
        print(self.abc)

    #贷前管理-录单管理
    def LuDanGuanLi(self,value):
        #点击主页按钮，返回到主页
        print("=========================================")
        print('贷前管理-录单管理')
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('点击主页按钮，返回主页')
            self.Driver.find_element_by_xpath(".//*[@id='main']/div[2]/a").click()
        except Exception as e:
             print(e)
             print('capture exception %s' % u"主页按钮未找到")
             self.Driver.get_screenshot_as_file("D:\BusError\error_反回到主页.png")
             traceback.print_exc()
             sys.exit()
        try:
            try:
                print('进入录单管理页面')
                self.Driver.switch_to.default_content()
                self.Driver.switch_to.frame("fraLeft")
                print('step1:点击贷前管理')
                self.Driver.find_element_by_id("span500").click()
            except Exception as e:
                print(e)
                print('capture exception %s' % u"贷前管理按钮未找到")
                self.Driver.get_screenshot_as_file("D:\BusError\error_贷前管理按钮页面.png")
        except:
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        # 进入录单管理页面
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('step2:点击录单管理')
            self.Driver.find_element_by_id("span500005").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-录单管理按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_进入录单管理页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #输入zidonghuaer客服建立的工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('    输入zidonghuaer客服建立的工单编号....')
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul[1]/li[1]/label/input").send_keys(value)
        except Exception as e:
            print(e)
            print('capture exception %s' % u"输入工单编号文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_工单编号文本框页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #点击录单管理查询按钮
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("step3:点击录单管理-查询按钮")
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul[2]/li[3]/button[2]").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"录单管理查询按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_录单管理查询按钮页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
         #录单管理-获取工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print('    获取查询结果...')
            self.LuDanGuanLi_APP_ID=self.Driver.find_element_by_xpath("/html/body/form/table/tbody").text
            return self.LuDanGuanLi_APP_ID
        except Exception as e:
            print(e)
            print('capture exception %s' % u"录单管理获取工单编号失败")
            self.Driver.get_screenshot_as_file("D:\BusError\error_获取工单编号页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)

    #贷前管理-工单查询(客服)
    def GongDanChaXunKF(self,GongDanChaXunKF_Other_APP_ID):
         #点击主页按钮，返回到主页
        print("=========================================")
        print('贷前管理-工单查询(客服)')
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('点击主页按钮，返回主页')
            self.Driver.find_element_by_xpath(".//*[@id='main']/div[2]/a").click()
        except Exception as e:
             print(e)
             print('capture exception %s' % u"主页按钮未找到")
             self.Driver.get_screenshot_as_file("D:\BusError\error_返回到主页.png")
             traceback.print_exc()
             sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            try:
                print('进入工单查询(客服)页面')
                self.Driver.switch_to.default_content()
                self.Driver.switch_to.frame("fraLeft")
                print('step1:点击贷前管理')
                self.Driver.find_element_by_id("span500").click()
            except Exception as e:
                print(e)
                print('capture exception %s' % u"贷前管理按钮未找到")
                self.Driver.get_screenshot_as_file("D:\BusError\error_贷前管理按钮页面.png")
                traceback.print_exc()
                sys.exit()
        except:
            pass

        self.Driver.implicitly_wait(20)
        # 进入工单查询(客服)页面
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('step2:点击工单查询(客服)')
            self.Driver.find_element_by_id("span500031").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-工单查询(客服)按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_进入工单查询(客服)页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #输入zidonghuaer客服建立的工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("   输入zidonghuaer客服建立的工单编号")
            self.Driver.find_element_by_xpath("/html/body/form/div[3]/ul[1]/li[1]/label/input").send_keys(GongDanChaXunKF_Other_APP_ID)
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-工单查询(客服)-录入工单编号文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_工单查询(客服)_工单编号文本框页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #工单查询(客服)-查询按钮
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("step3:点击工单查询(客服)-查询按钮")
            self.Driver.find_element_by_xpath("/html/body/form/div[3]/ul[3]/li[5]/button[2]").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-工单查询(客服)-查询按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_工单查询(客服)_查询按钮页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #工单查询(客服)-获取工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("    获取查询结果....")
            self.GongDanChaXunKF_APP_ID=self.Driver.find_element_by_xpath("/html/body/form/table/tbody").text
            return self.GongDanChaXunKF_APP_ID
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-工单查询(客服)-查询结果未获取到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_工单查询(客服)_获取工单编号页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)

    #贷前管理-复议工单查询
    def FuYiGongDanChaXun(self,FuYiGongDanChaXun_Other_APP_ID):
        #点击主页按钮，返回到主页
        print("=========================================")
        print('贷前管理-复议工单查询管理')
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('点击主页按钮，返回主页')
            self.Driver.find_element_by_xpath(".//*[@id='main']/div[2]/a").click()
        except Exception as e:
             print(e)
             print('capture exception %s' % u"主页按钮未找到")
             self.Driver.get_screenshot_as_file("D:\BusError\error_返回到主页.png")
             traceback.print_exc()
             sys.exit()
        self.Driver.implicitly_wait(20)
        try:
            try:
                print('进入复议工单查询管理页面')
                self.Driver.switch_to.default_content()
                self.Driver.switch_to.frame("fraLeft")
                print('step1:点击贷前管理')
                self.Driver.find_element_by_id("span500").click()
            except Exception as e:
                print(e)
                print('capture exception %s' % u"贷前管理按钮未找到")
                self.Driver.get_screenshot_as_file("D:\BusError\error_贷前管理按钮页面.png")
                traceback.print_exc()
                sys.exit()
        except:
            pass
        self.Driver.implicitly_wait(20)
        # 进入复议工单查询管理页面
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('step2:点击复议工单查询管理')
            self.Driver.find_element_by_id("span500144").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-复议工单查询管理按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_进入复议工单查询管理页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #输入zidonghuaer客服建立的工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("   输入zidonghuaer客服建立的工单编号")
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul/li[1]/label/input").send_keys(FuYiGongDanChaXun_Other_APP_ID)
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-复议工单查询管理-录入工单编号文本框未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_复议工单查询管理_工单编号文本框页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #复议工单查询管理-查询按钮
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("step3:点击复议工单查询管理-查询按钮")
            self.Driver.find_element_by_xpath("/html/body/form/div[2]/ul/li[4]/button[2]").click()
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-复议工单查询管理-查询按钮未找到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_复议工单查询管理_查询按钮页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)
        #复议工单查询管理-获取工单编号
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraMain")
            print("    获取查询结果....")
            self.FYGDCXGL_APP_ID=self.Driver.find_element_by_xpath("/html/body/form/table/tbody").text
            return self.FYGDCXGL_APP_ID
        except Exception as e:
            print(e)
            print('capture exception %s' % u"贷前管理-复议工单查询管理-查询结果未获取到")
            self.Driver.get_screenshot_as_file("D:\BusError\error_复议工单查询管理_获取工单编号页面.png")
            traceback.print_exc()
            sys.exit()
        self.Driver.implicitly_wait(20)

         #点击主页按钮，返回到主页
        print("=========================================")
        try:
            self.Driver.switch_to.default_content()
            self.Driver.switch_to.frame("fraLeft")
            print('点击主页按钮，返回主页')
            self.Driver.find_element_by_xpath(".//*[@id='main']/div[2]/a").click()
        except Exception as e:
             print(e)
             print('capture exception %s' % u"主页按钮未找到")
             self.Driver.get_screenshot_as_file("D:\BusError\error_返回到主页.png")
             traceback.print_exc()
             sys.exit()
