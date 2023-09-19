# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 发送文本邮件
# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 用于构建邮件头
from email.header import Header
 
# 发信方的信息：发信邮箱，163邮箱授权码
from_addr = 'lixt@yit.life'
password = 'Lea@UFtUg@c19980'
# 收信人邮箱
to_addrs = 'lixt@yit.life'
 
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的xx你
   Gerrit密码已重置请使用新密码重新登陆,谢谢!
   新密码:
   Gerrit网址:
'''
msg = MIMEText(text, 'plain', 'utf-8')
 
# 邮件头信息
msg['From'] = Header('ceshi')
msg['To'] = Header(to_addrs)
# msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('Gerrit新密码')
 
# 开启发信服务，这里使用的是加密传输
print('准备发送')
server = smtplib.SMTP_SSL("smtphz.qiye.163.com",465)
print('已经连接,正在登录')
# server.connect("smtp.163.com",465)
# 登录发信邮箱
server.login(from_addr, password)
print('已经登录，正在发送')
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
print('发送完毕')
# 关闭服务器
server.quit()