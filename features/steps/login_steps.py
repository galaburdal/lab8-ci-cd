from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I open the Swag Labs login page")
def open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("I should be redirected to the inventory page")
def verify_redirect(context):
    assert "inventory.html" in context.driver.current_url
    assert context.driver.find_element(By.CLASS_NAME, "title").text == "Products"
