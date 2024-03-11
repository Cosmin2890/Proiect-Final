from behave import *
import time


@then('logout: I click the logout button')
def step_impl(context):
    context.acount_page.click_logout_button()
    time.sleep(10)


