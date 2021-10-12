import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
print(driver.title)

ele = driver.find_element_by_name("userName")
print(ele.is_enabled())
print(ele.is_displayed())

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()
time.sleep(2)

driver.find_element_by_xpath("//*[contains(text(),'Flights')]").click()
time.sleep(2)
ele1 = driver.find_element_by_xpath("//input[@value='roundtrip']")
print(ele1.is_selected())
ele2 = driver.find_element_by_xpath("//input[@value='oneway']")
print(ele2.is_selected())

driver.close()