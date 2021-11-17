import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

ele = driver.find_elements_by_xpath("//input")
print(len(ele))
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.close()