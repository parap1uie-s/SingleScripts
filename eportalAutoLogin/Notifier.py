#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
class Mailer:
    mail_host = ""
    mail_user = ""
    mail_pass = ""
    def __init__(self, mail_host, mail_user, mail_pass):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass

    def SendMail(self, receivers,subject,content):
        if(len(receivers) < 1):
            return False
        succ = 0
        error = 0

        smtpObj = smtplib.SMTP()
        smtpObj.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(self.mail_user,self.mail_pass)  

        for receiver in receivers:
            message = MIMEText(content, 'plain', 'utf-8')
            message['From'] = self.mail_user
            message['To'] =  receiver
            message['Subject'] = Header(subject, 'utf-8')
            print(receiver)
            try:
                smtpObj.sendmail(self.mail_user, receiver, message.as_string())
                succ += 1
                time.sleep(5)
            except smtplib.SMTPException:
                error += 1
        return len(receivers),succ