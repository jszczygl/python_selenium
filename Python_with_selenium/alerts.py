from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(1)
driver.switch_to.alert.dismiss()