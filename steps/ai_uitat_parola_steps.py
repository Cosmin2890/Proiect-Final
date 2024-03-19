from behave import *
import time


@when('ai_uitat_parola: I fill in my email "{email}"')
def step_impl(context, email):
    context.ai_uitat_parola.set_email(email)


@when('ai_uitat_parola: I click on the Trimite button')
def step_impl(context):
    context.ai_uitat_parola.click_buton_trimite()



@then('ai_uitat_parola: I verify the invalid email validation message "{msg}"')
def step_impl(context, msg):
    context.ai_uitat_parola.verify_mesaj_eroare(msg)



@when ('ai_uitat_parola: I make sure the email input is cleared')
def step_impl(context):
    context.ai_uitat_parola.clean_email_text_field()
