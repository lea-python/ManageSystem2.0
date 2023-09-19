# coding:utf-8
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from public import common
import requests
import json

def screen_cap(driver,log_paths,name):
    currenttime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    filepath = log_paths + "\\" + str(currenttime) + "_%s.png"%name
    time.sleep(1)
    driver.get_screenshot_as_file(filepath)

def click_ui(self,xpath01,xpath02,label,log_paths):
   self.driver.find_element(By.XPATH, '%s'%xpath01).click()
   if self.driver.find_element(By.XPATH,'%s'%xpath02).is_displayed():
       print("跳转"+label+"成功")
   else:
       print("跳转"+label+"失败")
   screen_cap(self.driver,log_paths,label)
    #关闭页签
   self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()

# 获取登录后的token,用于鉴权
def get_token(name,password):
   url = "http://tracker.yit.life:8816/login"

   payload = json.dumps({
   "username": "%s"%name,
   "password": "%s"%password,
   "rememberMe": False,
   "site_id": None,
   "code": "",
   "uuid": "",
   "site_no": "2",
   "login_type": 1
   })
   headers = {
   'client_type': 'web',
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   result = response.json()
   token = result["token"]
   return token


# 获取所有项目信息
def get_all_project():

   url = "http://tracker.yit.life:8816/api/admin/project_all"

   payload = ""
   headers = {
   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJIYXNGdWxsTmFtZUF1dGgiOnRydWUsIlNhbXBsZURlbGl2ZXJ5TW9kZSI6IiIsIlNsb3ROYW1lRGlzcGxheSI6MSwiY2xpZW50X2xvZ2luX3RpbWUiOiIyMDIzLTA0LTE0IDE1OjQ1OjMxIiwiZGF0YXNjb3BlIjoiMSIsImRiX25hbWUiOiJ0cmFja2VyMl9kYl8yIiwiZXZlbnRfc2NoZWR1bGVyc193YXJuX3RpbWUiOiIyIiwiZXhwIjoxNjgyNDA3NTI1LCJob3NwaXRhbF9kaXN0cmljdF9pZCI6MCwiaWRlbnRpdHkiOjUsImxvZ2luX3RpbWUiOiIyMDIzLTA0LTIzIDE1OjE5OjI0Iiwibmlja19uYW1lIjoidGVzdDAwMSIsIm9yaWdfaWF0IjoxNjgyMjM0NzI1LCJwZXJtaXNzaW9ucyI6bnVsbCwicHJvamVjdF9hdXRoIjoxLCJyb2xlaWQiOjIyLCJyb2xla2V5IjoiTEVBVEVTVCIsInJvbGVuYW1lIjoiTEVB5rWL6K-VIiwic2l0ZV9pZCI6Miwic2l0ZV9uYW1lIjoi5aSN5pem6ZmE5bGeIiwic2l0ZV9ubyI6IjIiLCJ1c2VybmFtZSI6InRlc3QwMDEifQ.IFoB2lk079vYaoHI2kAITGPufReQcCA-9pH-cnXdMOk'
   }

   response = requests.request("GET", url, headers=headers, data=payload)

   print(response.text)

class TestSmoke():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_smoke_ui(self):
    self.driver.get("http://tracker.yit.life:8816/site_no/2/#/login")#测试环境
   #  self.driver.get("http://tracker.yit.life:18097/site_no/signed/#/system/role")#测试环境
    #等待网页加载完成
    time.sleep(5)
    #窗口最大化
    self.driver.maximize_window()
    self.driver.find_element(By.NAME, "username").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("test002")
   #  self.driver.find_element(By.NAME, "username").send_keys("admin")
    self.driver.find_element(By.NAME, "password").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "password").send_keys("Lea123456")
   #  self.driver.find_element(By.NAME, "password").send_keys("P@ssword2")
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/form/button/span/span').click()
    time.sleep(5)
    if self.driver.find_element(By.ID,"tags-view-container"):
        Result = "PASS"
    else:
        Result = "FAIL"   
     
    self.driver.implicitly_wait(3)
    #跳转首页
    log_paths = common.mkdir_logs()
    if self.driver.find_element(By.ID,"tab-index_datastat").is_displayed():
      print("跳转首页成功")
    else:
      print("跳转首页失败")
    screen_cap(self.driver,log_paths,"首页")


    #展开侧边栏
    self.driver.find_element(By.XPATH, '//*[@id="hamburger-container"]').click()
    screen_cap(self.driver,log_paths,"收起侧边栏")
    self.driver.find_element(By.XPATH, '//*[@id="hamburger-container"]').click()
    screen_cap(self.driver,log_paths,"展开侧边栏")

   #=======================================基础配置==============================================
    self.driver.implicitly_wait(3)

    #基础配置:院区管理(已配置院区)
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span').click()
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转院区管理成功")
    else:
       print("跳转院区管理失败")
    screen_cap(self.driver,log_paths,"基础配置-院区管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()
    


    #基础配置:房间管理(已配置房间)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转房间管理成功")
    else:
       print("跳转房间管理失败")
    screen_cap(self.driver,log_paths,"基础配置-房间管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()
    


    #基础配置:房间设备配置(已配置房间设备)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[1]/button/span').is_displayed():
       print("跳转房间设备配置成功")
    else:
       print("跳转房间设备配置失败")
    screen_cap(self.driver,log_paths,"基础配置-房间设备配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置:采集设备配置(已配置采集设备)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[4]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[5]/div').is_displayed():
       print("跳转采集设备配置成功")
    else:
       print("跳转采集设备配置失败")
    screen_cap(self.driver,log_paths,"基础配置-采集设备配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置:公司管理(已配置公司)   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[5]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[2]/div').is_displayed():
       print("跳转公司管理成功")
    else:
       print("跳转公司管理失败")
    screen_cap(self.driver,log_paths,"基础配置-公司管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()

    #基础配置:样本处理步骤配置   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转样本处理步骤配置成功")
    else:
       print("跳转样本处理步骤配置失败")
    screen_cap(self.driver,log_paths,"基础配置-样本处理步骤配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 离心子类型配置   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[7]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转离心子类型配置成功")
    else:
       print("跳转离心子类型配置失败")
    screen_cap(self.driver,log_paths,"基础配置-离心子类型配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()

    #基础配置: 条码类型管理配置   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[8]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转条码类型管理配置成功")
    else:
       print("跳转条码类型管理配置失败")
    screen_cap(self.driver,log_paths,"基础配置-条码类型管理配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 标签模板管理配置   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[9]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div').is_displayed():
       print("跳转标签模板管理配置成功")
    else:
       print("跳转标签模板管理配置失败")
    screen_cap(self.driver,log_paths,"基础配置-标签模板管理配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 采集设备型号配置   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[10]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[4]/div').is_displayed():
       print("跳转采集设备型号配置成功")
    else:
       print("跳转采集设备型号配置失败")
    screen_cap(self.driver,log_paths,"基础配置-采集设备型号配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 备注管理   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[11]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转备注管理成功")
    else:
       print("跳转备注管理失败")
    screen_cap(self.driver,log_paths,"基础配置-备注管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


   #滑动



    #基础配置: 单位管理   
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[12]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转单位管理成功")
    else:
       print("跳转单位管理失败")
    screen_cap(self.driver,log_paths,"基础配置-单位管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 检验项目管理 
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[13]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转检验项目管理成功")
    else:
       print("跳转检验项目管理失败")
    screen_cap(self.driver,log_paths,"基础配置-检验项目管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 叫号窗口管理(暂未开发)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[14]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[3]/div').is_displayed():
       print("跳转叫号窗口管理成功")
    else:
       print("跳转叫号窗口管理失败")
    screen_cap(self.driver,log_paths,"基础配置-叫号窗口管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #基础配置: 短信模板管理(暂未开发)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[15]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转短信模板管理成功")
    else:
       print("跳转短信模板管理管理失败")
    screen_cap(self.driver,log_paths,"基础配置-短信模板管理")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #收起基础配置栏
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span').click()


    #=======================================项目管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span').click()   

    #项目管理:项目配置
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label').is_displayed():
       print("跳转项目管理——项目配置成功")
    else:
       print("跳转项目管理——项目配置失败")
    screen_cap(self.driver,log_paths,"项目管理-项目配置")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #项目管理:项目中心
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[2]/a/li/span').click()
    if self.driver.find_element(By.XPATH,'//*[@id="tab-status_all"]').is_displayed():
       print("跳转项目管理——项目中心成功")
    else:
       print("跳转项目管理——项目中心失败")
    screen_cap(self.driver,log_paths,"项目管理-项目中心")
    #关闭页签
    self.driver.find_element(By.XPATH, '//*[@id="tags-view-container"]/div/div[1]/div/span[2]/span[2]').click()


    #项目管理:患者信息管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','项目管理-患者信息管理',log_paths)

    #项目管理:培训记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[4]/div','项目管理-培训记录',log_paths)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span').click()   

    #=======================================计划排程==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/div/span').click()   

   #  #计划排程:日历提醒
   #  click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/div/div[1]/div[2]/button[1]/span','计划排程-日历提醒',log_paths)
   #  time.sleep(3)
   #  self.driver.find_element(By.XPATH, '//*[@id="hamburger-container"]').click()

    #计划排程:周排程
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/form/div[2]/label','计划排程-周排程',log_paths)  

    #计划排程:样本管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[11]/label','计划排程-样本管理',log_paths)

    #计划排程:样本提醒
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div[1]/div/div/div[1]','计划排程-样本提醒',log_paths)

    #计划排程:条码匹配
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[5]/a/li/span','//*[@id="matchBarcode"]/form/div[1]/label','计划排程-条码匹配',log_paths)

    #计划排程:条码匹配日志
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[6]/a/li/span','//*[@id="matchBarcode"]/div[1]/div[2]/table/thead/tr/th[1]/div','计划排程-条码匹配日志',log_paths)

    #计划排程:条码核对
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[7]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','计划排程-条码核对',log_paths)

    #计划排程:发送短信
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[8]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[6]/label','计划排程-发送短信',log_paths)  

    #计划排程:短信发送记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[9]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[5]/label','计划排程-短信发送记录',log_paths)  

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/div/span').click()   

    #=======================================采集管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[5]/li/div/span').click()   

    #采集管理:访视计划
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[1]/div[1]/span[2]','采集管理-访视计划',log_paths)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[5]/li/div/span').click()   

    #=======================================药房管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/div/span').click()   

    #药房管理:药物入库
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[8]/label','药房管理-药物入库',log_paths)

    #药房管理:药物拆分
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[5]/div/button[3]/span','药房管理-药物拆分',log_paths)

    #药房管理:药物移库
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[3]/a/li/span','//*[@id="pane-out"]/div/form/div[11]/div/button[3]/span','药房管理-药物移库',log_paths)           

    #药房管理:药物库存
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[9]/div/button[3]/span','药房管理-药物库存',log_paths)           

    #药房管理:发药出库
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[5]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[7]/div/button[3]/span','药房管理-发药出库',log_paths)    

    #药房管理:药物回收
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[6]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[8]/div/button[3]/span','药房管理-药物回收',log_paths) 

    #药房管理:药物销毁
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[7]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[5]/div/button[3]/span','药房管理-药物销毁',log_paths) 

    #药房管理:药物退回
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[8]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[5]/div/button[3]/span','药房管理-药物退回',log_paths) 

    #药房管理:药物转运
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[9]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[11]/div/button[3]/span','药房管理-药物转运',log_paths) 

    #药房管理:库存变动明细
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[10]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[8]/div','药房管理-库存变动明细',log_paths) 

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/div/span').click()

    #=======================================样本室管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/div/span').click()   

    #样本室管理:冰箱使用记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[2]/label','样本室管理-冰箱使用记录',log_paths)

    #样本室管理:配送单录入
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[3]/div','样本室管理-配送单录入',log_paths)

    #样本室管理:配送单审核
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[3]/div','样本室管理-配送单审核',log_paths)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[7]/li/div/span').click()


    #=======================================报表管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/div/span').click()   

    #报表管理:移液枪记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[1]/div','报表管理-移液枪记录',log_paths)

    #报表管理:样本溶血
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[6]/label','报表管理-样本溶血',log_paths)

    #报表管理:样本乳糜
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[6]/label','报表管理-样本乳糜',log_paths)

    #报表管理:冰箱使用记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[2]/label','报表管理-冰箱使用记录',log_paths)

    #报表管理:离心机记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[5]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[3]/label','报表管理-离心机记录',log_paths)

    #报表管理:库存查询
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[6]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[6]/label','报表管理-库存查询',log_paths)

    #报表管理:样本处理记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[7]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[5]/label','报表管理-样本处理记录',log_paths)

    #报表管理:报表导出记录
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[8]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/table/thead/tr/th[1]/div','报表管理-报表导出记录',log_paths)

    #报表管理:报表导出审核
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/ul/div[9]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[2]/label','报表管理-报表导出审核',log_paths)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[8]/li/div/span').click() 

    #=======================================系统管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/div/span').click()   

    #系统管理:首页配置
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/div[1]','系统管理-首页配置',log_paths)

    #系统管理:用户管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/label','系统管理-用户管理',log_paths)

    #系统管理:角色管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[1]/div/div/div[1]/form/div[1]/label','系统管理-角色管理',log_paths)

    #系统管理:部门管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','系统管理-部门管理',log_paths)

    #系统管理:岗位管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[5]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','系统管理-岗位管理',log_paths)

    #系统管理:字典管理
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[6]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','系统管理-字典管理',log_paths)

    #系统管理:参数设置
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[7]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','系统管理-参数设置',log_paths)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/div/span').click()

    #=======================================日志管理==============================================
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/div/span').click()   

    #日志管理:报告查询
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[6]/label','日志管理-报告查询',log_paths)

    #日志管理:登录日志
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/ul/div[2]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','日志管理-登录日志',log_paths)

    #日志管理:操作日志
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/ul/div[3]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div','日志管理-操作日志',log_paths)

    #日志管理:job日志
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/ul/div[4]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[4]/label','日志管理-job日志',log_paths)

    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[10]/li/div/span').click()   

    #=======================================计划排程：日历提醒==============================================
    self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/div/span').click()   

    #计划排程:日历提醒
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/div/div/div[1]/div[2]/button[1]/span','计划排程-日历提醒',log_paths)

   #=======================================退出账号==============================================
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".el-icon-caret-bottom").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".el-dropdown-menu__item:nth-child(5) > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns > .el-button--primary > span").click()
  @pytest.mark.skip(reason='test')
  def test_smoke_addnewproject(self):
      time.sleep(5)
      self.driver.get("http://tracker.yit.life:8816/site_no/2/#/login")
      #等待网页加载完成
      time.sleep(5)
      #窗口最大化
      self.driver.maximize_window()
      self.driver.find_element(By.NAME, "username").click()
      time.sleep(1)
      self.driver.find_element(By.NAME, "username").send_keys("test002")
      self.driver.find_element(By.NAME, "password").click()
      time.sleep(1)
      self.driver.find_element(By.NAME, "password").send_keys("Lea123456")
      self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/form/button/span/span').click()
      time.sleep(5)
      if self.driver.find_element(By.ID,"tags-view-container"):
         Result = "PASS"
      else:
         Result = "FAIL" 
   # =======================================新增项目==============================================
      self.driver.find_element(By.CSS_SELECTOR, ".menu-wrapper:nth-child(3) .el-submenu__title > span").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".is-opened .menu-wrapper:nth-child(1) span").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-button:nth-child(2) > span").click()
      self.driver.find_element(By.CSS_SELECTOR, ".is-required .el-textarea__inner").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".is-required .el-textarea__inner").send_keys("测试项目"+str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
      time.sleep(1)   
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(2) .el-input__inner").click()
      time.sleep(1)   
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(2) .el-input__inner").send_keys(str(time.strftime('%Y-%m-%d', time.localtime(time.time())))+"001")
      time.sleep(1)   
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(3) > .el-form-item .el-input__inner").click()
      time.sleep(1)   
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(3) > .el-form-item .el-input__inner").send_keys(str(time.strftime('%Y-%m-%d', time.localtime(time.time())))+"002")
      time.sleep(1)   
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(4) .el-input__inner").click()
      time.sleep(1) 
      # 选择CTCAE版本5.0
      self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
      time.sleep(1) 
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(5) .el-input__inner").click()
      time.sleep(1) 
      #选择与试用药关系
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]/span").click()
      time.sleep(1) 
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(7) .el-input__inner").click()
      time.sleep(1) 
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(7) .el-input__inner").send_keys("检测单位")
      time.sleep(1) 
      self.driver.find_element(By.CSS_SELECTOR, ".el-col:nth-child(9) .el-input__inner").click()
      time.sleep(1) 
      #选择项目状态
      self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[2]/span").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".el-col-12 .el-textarea__inner").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".el-col-12 .el-textarea__inner").send_keys("自动化测试项目")
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary > span").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".is-success .el-textarea__inner").click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".is-success .el-textarea__inner").send_keys("测试项目2023042301")
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .el-button--primary > span").click()
     













   # =======================================退出账号==============================================
      # time.sleep(1)
      # self.driver.find_element(By.CSS_SELECTOR, ".el-icon-caret-bottom").click()
      # time.sleep(2)
      # self.driver.find_element(By.CSS_SELECTOR, ".el-dropdown-menu__item:nth-child(5) > span").click()
      # self.driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns > .el-button--primary > span").click()
