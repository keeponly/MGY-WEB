# _*_coding: utf-8 _*_
# @Time     :2020/1/9  11:18
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :Test_login.py
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

projectName ="//input[@placeholder='请输入项目名称']"
reportType = "//input[@placeholder='请选择评估报告类型']"
assessmentBaseDate = "//input[@placeholder='选择评估基准日']"
assessmentObjectiveId = "//input[@placeholder='请选择评估目的类型']"
projectExpenseExpect = "//input[@placeholder='请输入预期合同价']"
firstAppraiser = "//input[@placeholder='请选择第一签字评估师']"
secondAppraiser = "//input[@placeholder='请选择第二签字评估师']"
otherProject = "//input[@class='input frist-tr text-left']"
Establish = "//*[text()='创建']"
driver = Chrome()
driver.maximize_window()
driver.get("https://pg-bate.cailian.net/#/login")
'''设置等待时间为20秒，没1秒寻找一次知道找到 EC.方法名((定位方式，定位表达式))
显性等待函数'''


def wait_find_element(locator) -> WebElement: #用箭头确定会返回什么类型的数值，返回页面元素
    input_ele = WebDriverWait(driver, 40, 1).until(EC.visibility_of_element_located(locator))
    time.sleep(3)
    return input_ele


Account_number = "//input[@placeholder='请输入用户名']"
Password = "//input[@placeholder='请输入密码']"
Verification = "//input[@placeholder='请输入验证码']"
user_ele = wait_find_element((By.XPATH, Account_number))
user_ele.click()
user_ele.send_keys("18611815532")
pwd_ele = wait_find_element((By.XPATH, Password))
pwd_ele.click()
pwd_ele.send_keys("222222")
Verification_ele = wait_find_element((By.XPATH, Verification))
Verification_ele.click()
# code = input("shuru")
Verification_ele.send_keys('1111')
submit_elc = wait_find_element((By.CLASS_NAME, "submit-btn")).click()
'''
# 创建项目
add_project = wait_find_element((By.XPATH, "//a[text()= '快速创建项目']"))
# time.sleep(3)
add_project.click()

# 项目名称
project_Name = "wang001"
projectName_ele = wait_find_element((By.XPATH, projectName))
projectName_ele.click()
projectName_ele.send_keys(project_Name)
# 报告类型
reportType_ele = wait_find_element((By.XPATH, reportType))
reportType_ele.click()
# time.sleep(3)
type_01 = wait_find_element((By.XPATH, "//span[text()='土地估价报告']")).click()
# time.sleep(2)
# 评估基准日
assessmentBaseDate_ele = wait_find_element((By.XPATH, assessmentBaseDate))
# time.sleep(3)
assessmentBaseDate_ele.click()
time.sleep(3)
time_01 = wait_find_element((By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[1]/div/span"))
# time.sleep(3)
time_01.click()
# js_code = "arguments[0].readOnly = false"
# driver.execute_script(js_code, assessmentBaseDate_ele)
# js_code1 = "arguments[0].value = '2020-01-12'"
# driver.execute_script(js_code1, assessmentBaseDate_ele)
# time.sleep(3)
# 评估目的
assessmentObjectiveId_ele = wait_find_element((By.XPATH, assessmentObjectiveId))
assessmentObjectiveId_ele.click()
time.sleep(3)
type_01 = wait_find_element((By.XPATH, "//span[text()='改建']")).click()
# 预期合同价
projectExpenseExpect_ele = wait_find_element((By.XPATH, projectExpenseExpect))
projectExpenseExpect_ele.click()
projectExpenseExpect_ele.send_keys("1000")
# 第一评估师
firstAppraiser_ele = wait_find_element((By.XPATH, firstAppraiser))
firstAppraiser_ele.click()
time.sleep(3)
name_01 = "//*[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/span[2]"
first_name = wait_find_element((By.XPATH, name_01))
first_name.click()
firs_click = wait_find_element((By.XPATH, '//a[@class="search-btn"]'))
firs_click.click()
# js_01 = 'e =document.getElementsByClassName("el-input__inner")[8];'
# ele = driver.execute_script(js_01)
# time.sleep(3)
# js_02 = "e.readOnly = false;"
# driver.execute_script(js_02)
# time.sleep(3)
# js_03 = "e.value = '280'"
# driver.execute_script(js_03)
# time.sleep(3)
# 第二评估师
secondAppraiser_ele = wait_find_element((By.XPATH, secondAppraiser))
secondAppraiser_ele.click()
time.sleep(3)
name_02 = "//*[@id='app']/div[2]/div[3]/div/div[2]/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]"
second_name = wait_find_element((By.XPATH, name_02))
second_name.click()
second_click = wait_find_element((By.XPATH, '//a[@class="search-btn"]'))
second_click.click()
# secondAppraiser_ele = wait_find_element((By.XPATH, secondAppraiser))
# js_03 = "arguments[0].readOnly = false"
# driver.execute_script(js_03, secondAppraiser_ele)
# js_04 = "arguments[0].value = '281'"
# driver.execute_script(js_04, secondAppraiser_ele)
# 股权信息树
otherProject_ele = wait_find_element((By.XPATH, otherProject))
otherProject_ele.click()
otherProject_ele.send_keys("第一公司")
# 创建
Establish_ele = wait_find_element((By.XPATH, Establish))
Establish_ele.click()
Establish_ele_01 = wait_find_element((By.XPATH, '//div[@class="search-btn"]'))
Establish_ele_01.click()
time.sleep(5)
'''
# 主页项目搜索
res_name = wait_find_element((By.XPATH, "//input[@placeholder='请输入项目名称关键字']"))
res_name.click()
res_name.send_keys('wang001')
time.sleep(3)
res_name_01 = wait_find_element((By.XPATH, '//i[@class="iconfont icon-sousuo"]'))
res_name_01.click()
pro_name = wait_find_element((By.XPATH, '//span[@title="wang001"]'))
pro_name.click()
# 项目编辑
editor_1 = wait_find_element((By.XPATH, '//span[@class="search-btn marginRight0"]'))  # 点击编辑
editor_1.click()
'//input[@placeholder="请输入项目简称"]'
'//input[@placeholder="请选择项目其他负责人"]'
'//input[@placeholder="请选择项目性质"]'
'//input[@placeholder="请选择项目级别"]'
'//input[@placeholder="请选择评估对象类型"]'
'//input[@placeholder="请输入评估目的描述"]'
'//input[@placeholder="请选择具体经济行为"]'
'//input[@placeholder="请选择价值类型"]'
'//input[@placeholder="请选择项目联络人"]'
'//input[@placeholder="请选择评估报告类型"]'
'//input[@placeholder="请输入总资产账面值"]'
'//input[@placeholder="请选择现场工作时间"]'
# 项目特点
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[1]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[2]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[3]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[4]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[5]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[6]/div/div/label[2]/span[1]/span"
"//*[@id='pane-first']/div/div[1]/div/div/div[2]/div[2]/form/div[7]/div/div/label[2]/span[1]/span"
# 其他信息
'//*[@id="tab-contract"]'
'//input[@placeholder="请输入"]'
'//*[@id="pane-contract"]/div/div[1]/div/div/form/div[1]/div[2]/ul/div/li[2]/div/div/div[1]/div/div/div/div/label[2]/span[1]/span'
'//input[@placeholder="请输入详细地址"]'
'//input[@placeholder="请选择经济性质"]'
'//input[@placeholder="请输入评估对象"]'
'//input[@placeholder="请输入评估对象"]'
'//input[@placeholder="请输入评估范围"]'
'//input[@placeholder="请输入评估对象"]'
# 独立性自查
'//*[@id="tab-second"]'
'//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/label[2]/span[1]/span'
'//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/label[2]/span[1]/span'
'//*[@id="pane-second"]/div/div[1]/div/div/div[2]/div[2]/div[3]/div/label[2]/span[1]/span'
# 保存
'//button[@class="el-button saveBtn fs13 el-button--primary"]'
