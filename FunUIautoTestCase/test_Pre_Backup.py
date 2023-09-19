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
from loguru import logger
def click_by_xpath(self,xpath,log_content):
    self.driver.find_element(By.XPATH, '%s'%xpath).click()
    time.sleep(1)
    logger.info("点击"+log_content)
    

class Test_Pre():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    self.vars = {}
  
#   def teardown_method(self, method):
#     time.sleep(1)
#     #退出账号
#     self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div').click()
#     self.driver.find_element(By.XPATH, '//*[@id="dropdown-menu-8161"]/li[4]/span').click()
#     self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span').click()
#     time.sleep(1)
#     self.driver.quit()
  
  def test_pre(self):
    self.driver.get("http://tracker.yit.life:7816/site_no/system/#/login")
    time.sleep(5)
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.NAME, "username").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "username").send_keys("admin")
    self.driver.find_element(By.NAME, "password").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "password").send_keys("Abc123456")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".login-btn").click()
    time.sleep(1)
    try:
      if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/p").is_displayed() == False:
          logger.info("无警告弹窗")
      else:
          self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span").click()
    except:
       pass
    time.sleep(5)
    click_by_xpath(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span','系统管理')
    click_by_xpath(self,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li/span','中心管理')
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span').click()
    time.sleep(1)
    # 中心管理
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li/span').click()
    # 新增
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div/button/span').click()
    # 输入中心编号
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input').send_keys("autotest")
    # 输入中心名称
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input').send_keys("自动化测试")
    # 输入中心地址
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div[1]/input').send_keys("autotest")
    # 确定
    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]/span').click()
if __name__ ==  '__main__':
   Test_Pre().test_pre()