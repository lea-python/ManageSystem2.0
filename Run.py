# # coding:utf-8

"""
2023/4/14 By Lea
程序主入口
"""
from loguru import logger
import sys
sys.path.append("D:\\ManageSystem2.0\\FunUIautoTestCase\\public")
from common import status_code_url
sys.path.append("D:\\ManageSystem2.0\\FunUIautoTestCase")
from test_Pre import test_pre

# 判断是否要创建新的中心
if status_code_url("http://tracker.yit.life:8816/site_no/auto_test/#/login") == 0:
    logger.info("自动化测试中心已创建")
else:
    logger.error("开始创建自动化测试中心")
    test_pre()


