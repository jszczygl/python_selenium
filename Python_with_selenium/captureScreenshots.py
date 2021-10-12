from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

driver.save_screenshot("C:/Users/Kuba/PycharmProjects/python_selenium/Python_with_selenium/scrennshot.png")

driver.get_screenshot_as_file("C:/Users/Kuba/PycharmProjects/python_selenium/Python_with_selenium/scrennshot1.jpg")

driver.close()