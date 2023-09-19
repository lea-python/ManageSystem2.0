import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
20230317 By Lea
对selenium的方法的改良,由于脚本速度过快导致点击事件以及发生,但页面还未刷新
"""

def pub_sleep(func):
    def inner(driver,type,value):
        time.sleep(1)
        func(driver,type,value)
    return inner


@pub_sleep
def click_by_element(driver,type,value):
    driver.find_element(type,value).click()