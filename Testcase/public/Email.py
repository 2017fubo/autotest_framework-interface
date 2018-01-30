#- * - coding:utf - 8 -*-
#
__author__ = 'fubo'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from rizhi import log_config as a
import logging
import time,os

class Mail_Send:

    def __init__(self):
        #邮件信息配置
        self.sender  = 'fubo201012@163.com'
        self.receiver = 'bo.fu@sinobbd.com'
        self.subject = 'CDN研发-接口回归结果'
        self.smtpserver = 'smtp.163.com'
        self.username = 'fubo201012@163.com'
        self.password = 'fubo1234'

    def mail_send(self):##发送mail
        ##读取测试报告
        f = open(self.file_new,'rb')
        mail_body = f.read()
        f.close()

        ##定义邮件
        msg = MIMEText(mail_body,_subtype="html",_charset="utf-8")
        time_temp = time.strftime("%Y%m%d-%Hh%Mm", time.localtime())
        msg["Subject"] = Header(self.subject + time_temp,'utf-8')

        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(self.username,self.password)
        smtp.sendmail(self.sender,self.receiver,msg.as_string())
        smtp.quit()

        return

    def send_report(self):
        result_dir = 'E:\\SinoBBD\\AUTOTEST\\Web_Autoest_FW\\TestResult'
        lists = os.listdir(result_dir)
        logging.info(lists)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
        logging.info("最新测试报告："+lists[-1])
        self.file_new = os.path.join(result_dir,lists[-1])
        self.mail_send()