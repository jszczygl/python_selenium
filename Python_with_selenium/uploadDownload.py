from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:/Users/Kuba/Desktop"})

driver = webdriver.Chrome(executable_path='C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe', options=chromeOptions)
# driver.get("http://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(1)
#
# #upload
# driver.switch_to.frame(0)
# ele = driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']")
# driver.execute_script("arguments[0].scrollIntoView();", ele)
# ele.send_keys("C:/Users/Kuba/Desktop/lala.txt")


#download
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id("textbox").send_keys("testing")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
