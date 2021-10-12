from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)
actions = ActionChains(driver)

hov = driver.find_element_by_id("age")
driver.execute_script("arguments[0].scrollIntoView();", hov)
actions.move_to_element(hov).perform()
time.sleep(2)

doubleC = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
driver.execute_script("arguments[0].scrollIntoView();", doubleC)
actions.double_click(doubleC).perform()
time.sleep(2)

rightC = driver.find_element_by_id("field2")
actions.context_click(rightC).perform()
time.sleep(2)

drag = driver.find_element_by_id("draggable")
drop = driver.find_element_by_id("droppable")
actions.drag_and_drop(drag, drop).perform()
time.sleep(2)
driver.close()