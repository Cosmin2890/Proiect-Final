from behave import *
import time


@given('acount: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)


@given('acount: I fill in a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)


@given('acount: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@given('acount: Verify expected pages "{url}"')
def step_impl(context, url):
    context.login_page.curent_url(url)


@when('acount: I click the informatii personale button')
def step_impl(context):
    context.acount_page.click_informatii_persoanle_button()


@then('acount: I Change the lastname in "{nume}"')
def step_impl(context, nume):
    context.acount_page.field_name_change(nume)


@then('acount: I click the Trimite button')
def step_impl(context):
    context.acount_page.click_trimite_button()


@then('acount: I Change the firstname in "{prenume}"')
def step_impl(context, prenume):
    context.acount_page.field_firstname_change(prenume)


@when('acount: I click the Masinile mele button')
def step_impl(context):
    context.acount_page.click_masinile_mele_button()


@then('acount: I verify the message if I have the car registered "{msg}"')
def step_impl(context, msg):
    context.acount_page.verify_machine_mesage(msg)

