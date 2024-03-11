from behave import *
import time


@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()



@given('login: I accept all cookies')
def step_impl(context):
    context.login_page.click_accept_cookie()
    time.sleep(2)

@when('login: I click on the Ai uitat parola link')
def step_impl(context):
    context.login_page.click_ai_uitat_parola()


@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('login: I fill in a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('login: It shown an error message "{msg}"')
def step_impl(context, msg):
    context.login_page.verify_mesaj_eroare(msg)


@then('login: Verify expected pages "{url}"')
def step_impl(context, url):
    context.login_page.curent_url(url)

