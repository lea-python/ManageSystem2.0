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
from loguru import logger


class TestSmoke():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    self.vars = {}
  
#   def teardown_method(self, method):
#     self.driver.quit()

  def test_smoke_ui(self):
    self.driver.get("http://tracker.yit.life:8816/site_no/auto_test/#/login")
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