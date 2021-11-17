from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

rows = driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr")
print(len(rows))

cols = driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")
print(len(cols))

for r in range(2, len(rows)+1):
    for c in range(1, len(cols)+1):
        value = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)

driver.close()