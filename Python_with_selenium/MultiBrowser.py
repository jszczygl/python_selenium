from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
# driver = webdriver.Firefox('driver_path')

driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()