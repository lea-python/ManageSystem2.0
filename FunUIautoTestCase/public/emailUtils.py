# coding:utf-8
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import time
import base64
from email.utils import formataddr
"""
20221107
By Lea
发送邮件功能

"""


#base64解密
def get_base64(str_get_base64):
    return base64.b64decode(str_get_base64).decode('utf-8')

# 生成html
def html_generate(html_path,data,col_title):
	title = ""
	title += "<tr>"
	for item in col_title:
		title  += "<th>" + str(item) +"</th>"
	title += "</tr>"

	coment = ""
	for item in data:
		coment += "<tr>"
		for i in item:
			coment += "<td>" + str(i) +"</td>"
		coment += "</tr>"
	
	with open(html_path,mode="r",encoding="utf-8") as f:
		html_text = f.read()
		html_text_new = html_text.replace("#{title}",title).replace("#{content}",coment)
	return html_text_new




def send_email(receivers,content,filepath,emailtype):
	"""
	sender:发送人邮箱
	password传入base64加密字符串
	receivers:接收人邮箱,列表,以逗号分隔
	content:html格式内容
	mailtitle:邮件主题
	filepath:附件文件本地路径
	emailtype:使用邮箱类型
	"""
	# sender = "lixiaotong@ringnex.com"
	# sender = "1162758844@qq.com"
	# password = get_base64(b'cWJteXFwcGpjdHRuamVjYQ==')
	# password = "Lea123456"
	# receivers = ["lixiaotong@ringnex.com","lijingjing@ringnex.com"]
	# receivers = ["1p9_y2pk95z50n@dingtalk.com"]
	From = 'lixt@yit.life'
	password = 'Lea@UFtUg@c19980'
	currentTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	mail_title = "自动化测试报告"
	msg = MIMEMultipart()
	msg['Subject'] = mail_title + currentTime
	msg['From'] = From
	msg['rcptto'] = ','.join(receivers)
	msg['Message-id'] = email.utils.make_msgid() # type: ignore
	msg['Date'] = email.utils.formatdate() # type: ignore
	report_file = MIMEApplication(open(filepath, 'rb').read())
	report_file.add_header('Content-Disposition', 'attachment', filename=filepath)
	msg.attach(report_file)
	msg.attach(MIMEText(content,'html','utf-8'))
	try:
		if emailtype == "smtp.ringnex.com":
			server = smtplib.SMTP_SSL("smtp.ringnex.com", 465)#aliyun
		elif emailtype == "smtp.qq.com":
			server = smtplib.SMTP("smtp.qq.com", 25)
		elif emailtype == "smtphz.qiye.163.com":
			print("网易企业邮箱")
			server = smtplib.SMTP_SSL("smtphz.qiye.163.com",465)
			server.login(From, password)
			server.sendmail(From, msg['rcptto'].split(','), msg.as_string())
			server.quit()
			print('邮件发送成功！')
	except:
		print("邮箱类型暂未添加,Please Call Lea")
		print('服务和端口不通')
		exit(1)

	#开启DEBUG模式
	# try:
	# 	# server.set_debuglevel(0)
	# 	server.login(From, password)
	# 	print('账密验证成功')
	# except:
	# 	print('账密验证失败')
	# 	exit(1)

