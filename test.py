# from selenium import webdriver
# import time

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# time.sleep(3)
# driver.get_screenshot_as_file("./Log/save.png")
# driver.quit()

# import os
# from datetime import date
# current_datetime = date.today()
# log_paths = os.getcwd()+"\\Log\\"+str(current_datetime)+"_LOG"
# if os.path.exists(log_paths) == False:
#     os.mkdir(log_paths)
# else:
#     pass
# import time


# currenttime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
# current_datetime = date.today()
# log_file_name = log_paths + "\\" + str(currenttime) + "_log.txt"
# print(log_file_name)
# f = open(r"%s"%log_file_name,"a",encoding="utf-8")
# print("11111111",file=f)
# f.close()
# # f = open("D:\\ManageSystem2.0\\Log\\2023-03-23_LOG\\2023-03-23-13:51:07_log.txt", 'r', encoding='utf-8')

# if os.path.exists(log_file_name) == False:
#     file = open(r"%s"%log_file_name,"r")
#     file.close()
# else:
#     pass
# with open(r"%s"%file,"a",encoding="utf-8") as f:
#     print("111111",file = f)
#     f.close()
# import os 
# import yaml
# yamlname = "login"
# yaml_paths = os.getcwd()+"\\Config\\" + yamlname + ".yml"
# try:
#     with open(yaml_paths,"r",encoding="utf-8") as f:
#         data = yaml.load(f,Loader=yaml.FullLoader)
#         print(data)
# except:
#     print("yaml-----wrong")


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
# from public import common

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
from FunUIautoTestCase.public import common

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

class TestSmoke():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    self.vars = {}
  
#   def teardown_method(self, method):
#     self.driver.quit()

  def test_login(self):
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
    click_ui(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span','//*[@id="app"]/div[1]/div/div[2]/section/div/form/div[1]/label','基础配置-院区管理',log_paths)