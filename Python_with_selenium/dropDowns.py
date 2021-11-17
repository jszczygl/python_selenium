import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(1)

element = driver.find_element_by_id("dropdown")
drop = Select(element)

drop.select_by_visible_text("Option 2")
time.sleep(1)
drop.select_by_value("1")
time.sleep(1)
drop.select_by_index(2)

print(len(drop.options))
for option in drop.options:
    print(option.text)
driver.close()