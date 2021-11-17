from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("http://demo.guru99.com/test/newtours/")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "submit")))

assert "Welcome: Mercury Tours" in driver.title
driver.maximize_window()

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()

driver.close()