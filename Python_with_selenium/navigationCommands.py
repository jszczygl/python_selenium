import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
time.sleep(2)
print(driver.title)

driver.close()