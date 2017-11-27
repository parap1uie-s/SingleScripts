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
import socket, struct

class TYUTLogin:
    # analyze OS windows/linux
    # if (os.name == "nt"):#windows
    # # get local ip (windows)
    #     localip = socket.gethostbyname_ex(socket.gethostname())
    # else:#linux or unix
    # # get local ip (unix)
    #     import fcntl
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     localip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', 'eth0'[:15]))[20:24])
    ipList = socket.gethostbyname_ex(socket.gethostname())
    ips = []
    for ip in ipList[2]:
        if not (ip.startswith("192") or ip.startswith("169")):
           ips.append(ip)
    if len(ips) > 1 or len(ips) == 0:
        print("There are not only one ip address or no ip fit the rule")
        print(ipList)
        exit()
    localip = ips[0]
    print(localip)

    def getIP(self):
        return self.localip
    # check network status
    def check(self):
        url = "http://www.baidu.com"
        response = urllib.request.urlopen(url)
        geturl = response.geturl()
        if url == geturl:
            print("connected")
            return 0
        else:
            print("not connected")
            return -1


    # login
    def login(self,username,password):
        url = "http://202.207.240.67:801/eportal/?c=ACSetting&a=Login&wlanuserip="+self.localip+"&wlanacip=null&wlanacname=&port=&iTermType=1&mac=000000000000&ip="+self.localip+"&redirect=null"
        request = urllib.request.Request(url)
        request.add_header('Host','202.207.240.67:801')
        request.add_header('Connection','keep-alive')
        request.add_header('Cache-Control','max-age=0')
        request.add_header('Origin','http://202.207.240.67')
        request.add_header('Upgrade-Insecure-Requests','1')
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        request.add_header('Content-Type','application/x-www-form-urlencoded')
        request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        # request.add_header('Referer','http://202.207.240.67/a70.htm?wlanuserip=101.7.149.100&wlanacname=&me60=ethtrunk/2:2775.653')
        request.add_header('Referer','http://202.207.240.67/a70.htm')
        request.add_header('Accept-Encoding','gzip, deflate, br')
        request.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4')
        request.add_header('Cookie','wlanacname=; wlanacip=null')

        # data = r"DDDDD="+username+"&upass="+password+"&R1=0&R2=&R6=0&para=00&0MKKey=123456"
        data = {'DDDDD' : username, 'upass' : password, 'R1':'0', 'R2':'', 'R6':'0', 'para':'00','0MKKey':'123456'}
        data = urllib.parse.urlencode(data).encode(encoding='UTF8')
        response = urllib.request.urlopen(request,data)
        code = response.getcode()
        if(code == 200):
            return 1
        return -1