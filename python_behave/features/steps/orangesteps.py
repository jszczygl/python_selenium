from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')



@when('orange homepage is opened')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    context.driver.find_element_by_c

@then('verify that the logo is present')
def verify_logo(context):
    status = context.driver.find_element_by_xpath('//*[@id="divLogo"]//img').is_displayed()
    assert status is True

@then('close browser')
def close_browser(context):
    context.driver.close()