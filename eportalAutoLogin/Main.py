#!/usr/bin/env python
# coding=utf8
# 自动登录TYUT_IPV6 + 邮件推送IP地址
# @date:20171127
# 
# 命令行用法：python AutoLogin.py 学号 密码
# 可以写个批处理文件，写入命令，存为开机自启动脚本
# *nix下可使用crontab
# 自动连接校园网，并在IP地址变更后，自动发送新的IP地址到预设的邮箱

from AutoLogin import TYUTLogin
from Notifier import Mailer
import sys

username = "" # eg:wangnima0011
password = ""   # eg:abcdefgasda
if len(sys.argv) < 3:
    print("Use hard code params.")
    if(username == '' or password == ''):
        print("username or password error!")
        exit()
else:
    username = sys.argv[1]
    password = sys.argv[2]
l = TYUTLogin()
if l.check() == -1:
    ret = l.login(username, password)
else:
    ret = 0

if(ret == 1):
    mail_host="smtp.163.com"  #设置服务器
    mail_user=""    #发件邮箱用户名
    mail_pass="~`,hZVzH+2ENB:Pb"   #发件邮箱密码 
    receivers = ['aaa@bbb.com','...','...']  # 收件人地址列表
    m = Mailer(mail_host,mail_user,mail_pass)
    receiverNum, succNum = m.SendMail(receivers,"这里填标题",l.getIP())
    print("Send "+str(receiverNum)+" mails, success " + str(succNum) +" mails")