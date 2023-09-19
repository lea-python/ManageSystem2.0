# coding:utf-8
"""
2023/2/14
By Lea
登录模块
UI方式:正确账号密码登录
接口方式：
1.正确账号密码
2.正确账号错误密码
3.未注册账号错误密码
4.账号正确,密码为空
5.账号密码都为空
6.特殊字符、非法字符
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from public import webelement2
from public import common
from public import emailUtils
import os

# 正确账号密码
def test_login01(name,pwd):
    driver = webdriver.Chrome()
    driver.get("http://tracker.yit.life:8816/site_no/2/#/login")
    #等待网页加载完成
    time.sleep(3)
    
    driver.maximize_window()
    webelement2.click_by_element(driver,By.NAME,"username")
    driver.find_element(By.NAME, "username").send_keys(name)
    webelement2.click_by_element(driver,By.NAME,"password")
    driver.find_element(By.NAME, "password").send_keys(pwd)
    webelement2.click_by_element(driver,By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/form/button/span/span')
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/form/button/span/span').click()
    time.sleep(3)
    if driver.find_element(By.ID,"tags-view-container"):
        Result = "PASS"
    else:
        Result = "FAIL"
        log_paths = common.mkdir_logs()
        currenttime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        filepath = log_paths + "\\" + str(currenttime) + ".png"
        common.screen_web(driver,filepath)
        common.print_log(log_paths,"%s:登录失败")
    return Result
        #截图到log
        
    # driver.find_element(By.CSS_SELECTOR, "span > span").click()
    # driver.find_element(By.CSS_SEL.ECTOR, ".el-button--default:nth-child(2) > span").click()
    # element = driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2)")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()

if __name__ == "__main__":
        Result_all = []
        data = common.read_yaml("login")
        if data is not None:
            test_data = data["test_data"]
            for k,v in test_data.items(): # type: ignore
                result1 = ['登录']
                if "01" in k:
                    result1.append(k)
                    result1.append(v)
                    test_result = test_login01(v[0],v[1])
                    result1.append(test_result)
                    print(result1)
                    Result_all.append(result1)
                else:
                    pass
        else:
            print("配置文件为空")
           
        print(Result_all)
        filepath = common.write_to_csv(Result_all)

        #发送邮件
        title = ['模块','用例名','测试数据','测试结果']
        html_path = os.getcwd()+"\\public\\EmailHtml.html"
        content = emailUtils.html_generate(html_path,Result_all,title)
        emailUtils.send_email(receivers=['lixt@yit.life'],content=content,filepath=filepath,emailtype="smtphz.qiye.163.com")

                
    
