from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

curr = driver.current_window_handle
all_win = driver.window_handles
time.sleep(1)
driver.switch_to.window(all_win[0])

driver.quit()