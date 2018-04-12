#!/usr/bin/env python
# coding=utf8
# 自动登录TYUT_IPV6
# @date:20171127
# 
# 命令行用法：python AutoLogin.py 学号 密码
# 可以写个批处理文件，写入命令，存为开机自启动脚本
# *nix下可使用crontab
#
import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error
import sys
import socket
import os
import struct

class TYUTLogin:
    localip = ""
    def __init__(self, netcardName):
        # analyze OS windows/linux
        if (os.name == "nt"):#windows
        # get local ip (windows)
            localip = socket.gethostbyname_ex(socket.gethostname())
        else:#linux or unix
        # get local ip (unix)
            import netifaces as ni
            ip = ni.ifaddresses(netcardName)[ni.AF_INET][0]['addr']
        self.localip = ip

    def getIP(self):
        return self.localip
    # check network status
    def check(self):
        url = "http://www.baidu.com"
        try:
            response = urllib.request.urlopen(url)
            geturl = response.geturl()
        except Exception as e:
            print("not connected")
            return -1
        if url == geturl:
            print("connected")
            return 0
        else:
            print("not connected")
            return -1


    # login
    def login(self,username,password, host, port):
        url = "http://{}:{}/eportal/?c=ACSetting&a=Login&wlanuserip=".format(host,port)+self.localip+"&wlanacip=null&wlanacname=&port=&iTermType=1&mac=000000000000&ip="+self.localip+"&redirect=null"
        request = urllib.request.Request(url)
        request.add_header('Host','{}:{}'.format(host,port))
        request.add_header('Connection','keep-alive')
        request.add_header('Cache-Control','max-age=0')
        request.add_header('Origin','http://{}'.format(host))
        request.add_header('Upgrade-Insecure-Requests','1')
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        request.add_header('Content-Type','application/x-www-form-urlencoded')
        request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        request.add_header('Referer','http://{}/a70.htm'.format(host))
        request.add_header('Accept-Encoding','gzip, deflate, br')
        request.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4')
        request.add_header('Cookie','wlanacname=; wlanacip=null')

        data = {'DDDDD' : username, 'upass' : password, 'R1':'0', 'R2':'', 'R6':'0', 'para':'00','0MKKey':'123456'}
        data = urllib.parse.urlencode(data).encode(encoding='UTF8')
        response = urllib.request.urlopen(request,data)
        code = response.getcode()
        if(code == 200):
            return 1
        return -1
