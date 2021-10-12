from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
time.sleep(1)

links = driver.find_elements_by_tag_name("a")
print(len(links))

for link in links:
    print(link.text)

driver.find_element_by_link_text("REGISTER").click()
