# coding:utf-8

from selenium import webdriver
from selenium import webdriver
import os
from datetime import date
import yaml
import csv
import requests
from selenium.webdriver.common.by import By
import time
from loguru import logger

"""
20230321 By Lea
公共方法
"""


"""
基于网页的截图
"""
def screen_web(driver,filepath):
    driver.get_screenshot_as_file(filepath)

"""
创建当天的文件夹用于存放当天脚本运行的日志与截图
"""
def mkdir_logs():
    current_datetime = date.today()
    log_paths = os.path.abspath(os.path.join(os.getcwd(), '..'))+"\\Log\\"+str(current_datetime)+"_LOG"
    if os.path.exists(log_paths) == False:
        os.mkdir(log_paths)
    else:
        pass
    return log_paths


"""
打印错误日志到指定的日志文件中
"""
def print_log(log_paths,content):
    current_datetime = date.today()
    log_file_name = log_paths + "\\" + str(current_datetime) + "_log.txt"
    f = open(r"%s"%log_file_name,"a",encoding="utf-8")
    print("%s"%content,file=f)
    f.close()

"""
读取yml文件
"""
def read_yaml(config_name):
    yaml_paths = os.path.abspath(os.path.join(os.getcwd(), '..'))+"\\Config\\" + config_name + ".yml"
    try:
        with open(yaml_paths,"r",encoding="utf-8") as f:
            data = yaml.load(f,Loader=yaml.FullLoader)
            return data
    except:
        print("yaml-----wrong")


"""
csv
filepath:文件路径
title:表头,列表
List:数据,列表
"""
def write_to_csv(List):
    title = ['模块','用例名','测试数据','测试结果']
    filepath = os.path.abspath(os.path.join(os.getcwd(), '..'))+"\\Report\\" + str(date.today()) + "_AutoTestReport.csv"
    f = open(filepath,'w', encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(title)
    if len(List) != 0:
        for i in List:
            csv_writer.writerow(i)
        f.close()
    else:
        print("数据为空")
    return filepath


"""
判断网址的状态码
200:响应成功
403:服务器资源权限不够
404:服务器没有该资源
500:程序报错
"""

def status_code_url(url):
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    code = response.status_code
    if code == 200:
        return 0
    if code == 403:
        return 1
    if code == 404:
        return 2
    if code == 500:
        return 3
    

"""
使用xpath进行点击,等待,并打印对应log
"""

def click_by_xpath(driver,xpath,log_content):
    driver.find_element(By.XPATH, '%s'%xpath).click()
    time.sleep(1)
    logger.info("点击"+log_content)


"""
使用xpath进行输入框输入,等待,并打印对应log
"""

def edit_by_xpath(driver,xpath,value,log_content):
    driver.find_element(By.XPATH, '%s'%xpath).send_keys("%s"%value)
    time.sleep(1)
    logger.info("输入"+log_content)


"""
使用xpath进行点击,等待,并打印对应log
"""

def click_by_selector(driver,css_selector,log_content):
    driver.find_element(By.CSS_SELECTOR, '%s'%css_selector).click()
    time.sleep(1)
    logger.info("点击"+log_content)

"""
等待并打印日志
"""
def wait(t):
    logger.info("等待%s秒中......"%str(t))
    time.sleep(t)