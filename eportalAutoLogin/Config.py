"""
eportalAutoLogin
Base Configurations class.
"""


# Base Configuration Class
# Don't use this class directly. Instead, sub-class it and override
# the configurations you need to change.

class Config(object):
    """
    校园网账号
    """
    username = ""
    password = ""
    host = "202.207.240.67"
    port = "801"
    """
    your netcard name
    see 'ifconfig'
    """
    netcard = "enp3s0"

    """
    邮件配置
    由于密码明文存储，在不能100%确保服务器安全时
    建议配置一个新的邮箱专用于发件
    并且在收件邮箱将发件邮箱设置到白名单，以防高频率发信被判定为垃圾邮件
    """
    enableMail = True
    smtpMailHost = "smtp.163.com"  # 发件服务器
    smtpMailUser = ""              # 发件邮箱
    smtpMailPassword = ""          # 发件邮箱密码
    smtpMailReceivers = [""]       # 收件邮箱
    mailTitle = ""                 # 邮件标题，建议配置，否则易被判定为垃圾邮件，无法发送


