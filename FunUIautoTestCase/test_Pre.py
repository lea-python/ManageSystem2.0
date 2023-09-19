# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger
from public import common
from selenium.webdriver.common.keys import Keys

"""
2023/5/6
By Lea
用于其他测试前的准备
"""
def test_pre():
    # driver = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    # driver.get("http://tracker.yit.life:8816/site_no/system/#/login")
    # common.wait(5)
    # driver.set_window_size(1552, 840)
    # driver.find_element(By.NAME, "username").click()
    # common.wait(1)
    # driver.find_element(By.NAME, "username").send_keys("admin")
    # driver.find_element(By.NAME, "password").click()
    # common.wait(1)
    # driver.find_element(By.NAME, "password").send_keys("Abc123456")
    # common.wait(1)
    # driver.find_element(By.CSS_SELECTOR, ".login-btn").click()
    # common.wait(1)
    # try:
    #     if driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/p").is_displayed() == False:
    #         logger.info("无警告弹窗")
    #     else:
    #         driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span").click()
    # except:
    #     pass
    # common.wait(5)
    # common.click_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span','系统管理')
    # common.click_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[3]/a/li/span','中心管理')
    # common.click_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div/button/span','新增')
    # common.edit_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input','auto_test','中心编号')
    # common.edit_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input','自动化测试','中心名称')
    # common.edit_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div[1]/input','auto_test','中心地址')
    # common.click_by_xpath(driver,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]/span','确定')
    # common.wait(5)
    # if common.status_code_url("http://tracker.yit.life:8816/site_no/auto_test/#/login") == 0:
    #     logger.info("新增中心成功")
    # else:
    #     logger.error("新增中心失败")

    """
    首次登录新建的测试中心进行密码初始化
    """
    # 开启浏览器不自动关闭模式
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach',True) 

    # driver2 = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    # driver2.get("http://tracker.yit.life:8816/site_no/auto_test/#/login")
    # common.wait(5)
    # driver2.set_window_size(1552, 840)
    # driver2.find_element(By.NAME, "username").click()
    # common.wait(1)
    # driver2.find_element(By.NAME, "username").send_keys("admin")
    # driver2.find_element(By.NAME, "password").click()
    # common.wait(1)
    # driver2.find_element(By.NAME, "password").send_keys("Pa55word6!")
    # common.wait(1)
    # driver2.find_element(By.CSS_SELECTOR, ".login-btn").click()
    # common.wait(1)
    # try:
    #     if driver2.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/p").is_displayed() == False:
    #         logger.info("无警告弹窗")
    #     else:
    #         driver2.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span").click()
    # except:
    #     pass
    # common.wait(5)
    # common.edit_by_xpath(driver2,'//*[@id="pane-resetPwd"]/form/div[1]/div/div[1]/input','Pa55word6!','旧密码')
    # common.edit_by_xpath(driver2,'//*[@id="pane-resetPwd"]/form/div[2]/div/div[1]/input','Abc123456','新密码')
    # common.edit_by_xpath(driver2,'//*[@id="pane-resetPwd"]/form/div[3]/div/div/input','Abc123456','重复新密码')
    # common.click_by_xpath(driver2,'//*[@id="pane-resetPwd"]/form/div[4]/div/label/span[1]/span','勾选协议')
    # common.click_by_xpath(driver2,'//*[@id="pane-resetPwd"]/form/div[5]/div/button/span','确定')

    """
    修改密码完成后登录，开启所有菜单栏
    """
    # 开启浏览器不自动关闭模式
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach',True) 
    driver3 = webdriver.Chrome(executable_path=r"C:\\Users\\UR-BJ-126\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
    driver3.get("http://tracker.yit.life:8816/site_no/auto_test/#/login")
    common.wait(5)
    driver3.set_window_size(1552, 840)
    driver3.find_element(By.NAME, "username").click()
    common.wait(1)
    driver3.find_element(By.NAME, "username").send_keys("admin")
    driver3.find_element(By.NAME, "password").click()
    common.wait(1)
    driver3.find_element(By.NAME, "password").send_keys('Abc123456')
    common.wait(1)
    driver3.find_element(By.CSS_SELECTOR, ".login-btn").click()
    common.wait(1)
    try:
        if driver3.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/p").is_displayed() == False:
            logger.info("无警告弹窗")
        else:
            driver3.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span").click()
    except:
        pass
    common.wait(5)

    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/div/span',"系统管理")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[2]/a/li/span',"角色管理")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div',"系统管理员")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/div[2]/button[1]/span',"全选")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/div[2]/button[3]/span',"保存修改")
    # common.wait(3)
    driver3.refresh()
    common.wait(10)

    """
    首页配置全部打开
    """
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/div/span',"系统管理")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[1]/a/li',"首页配置")
    #首页配置
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[1]/a/li/span',"首页配置")
    # common.click_by_selector(driver3,".is-opened .menu-wrapper:nth-child(1) span","首页配置")
    # driver3.find_element(By.CSS_SELECTOR, ".is-opened .menu-wrapper:nth-child(1) span").click()
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[1]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div',"系统管理员")
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/div[2]/table/thead/tr/th[1]/div',"第一次点击勾选框")
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/div[2]/table/thead/tr/th[1]/div',"第二次点击勾选框")
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[1]/div[2]/button/span',"保存")
    common.wait(3)
    driver3.refresh()
    common.wait(10)


    """
    新建用户,重置密码需要手动操作
    """
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/div/span',"系统管理")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[1]/div[2]/div[1]/div/ul/div[9]/li/ul/div[2]/a/li/span',"用户管理")
    # common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[1]/div[2]/div[1]/div/button/span',"新增")
    # common.edit_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div/div[2]/form/div/div[1]/div/div/div/input',"T2","输入用户名")
    # common.edit_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/input',"张三二","输入姓名")
    # input_01 = driver3.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/section/div/div[2]/div/div[2]/form/div/div[3]/div/div/div/div[1]/div[1]/div[1]')
    # input_01.send_keys("测试中心")
    # input_01.send_keys(Keys.ENTER)

    """
    退出登录
    """
    common.click_by_xpath(driver3,'//*[@id="app"]/div[1]/div/div[2]/div/div[1]/div/div[3]/div[1]/div/div',"右上角下拉菜单")
    common.wait(3)
    #点击<退出登录>
    common.click_by_selector(driver3,".el-dropdown-menu__item:nth-child(5) > span","退出登录")
    # driver3.find_element(By.CSS_SELECTOR, ".el-dropdown-menu__item:nth-child(5) > span").click()
    common.wait(3)
    common.click_by_xpath(driver3,'/html/body/div[2]/div/div[3]/button[2]/span',"确定")
    common.wait(5)




if __name__ ==  '__main__':
   test_pre()