from behave import *
from selenium import webdriver

@given('Open chrome browser')
def open_browser(context):
    context.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')

@when('Open orange homepage')
def open_orange_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)

@when('Click on login button')
def click_login_button(context):
    context.driver.find_element_by_id("btnLogin").click()

@then('Successfully login')
def verify_login(context):
    try:
        text=context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test passed"
