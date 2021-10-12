from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(1)

#capture all the cookies
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#adding new cookie
cookie={'name':'Mycookie', 'value':'123456'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))

#deleting cookie
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print(len(cookies))

#delete all the coockies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))


driver.close()