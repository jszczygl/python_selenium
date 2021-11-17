from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(1)

# scroll down by pixels
# driver.execute_script("window.scrollBy(0,1000)","")

#sscroll until ele is visible
# ele = driver.find_element_by_xpath("//*[@id='content']//td[contains(text(), 'Palestine')]")
# driver.execute_script("arguments[0].scrollIntoView();", ele)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


driver.close()