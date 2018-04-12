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
from Config import *
import sys

if len(sys.argv) < 3:
    print("Use hard code params.")
    if(username == '' or password == ''):
        print("username or password error!")
        exit()
    else:
    	username = Config.username
    	password = Config.password
else:
    username = sys.argv[1]
    password = sys.argv[2]

l = TYUTLogin(Config.netcard)
if l.check() == -1:
    ret = l.login(username, password, Config.host, Config.port)
else:
    ret = 0

if(ret == 1 && Config.enableMail):
    m = Mailer(Config.smtpMailHost, Config.smtpMailUser, Config.smtpMailPassword)
    receiverNum, succNum = m.SendMail(Config.smtpMailReceivers,Config.mailTitle, l.getIP())
    print("Send "+str(receiverNum)+" mails, success " + str(succNum) +" mails")
