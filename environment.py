from browser import Browser
from pages.login_page import LoginPage
from pages.ai_uitat_parola import AiUitatParolaPage
from pages.acount_page import AcountPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.ai_uitat_parola = AiUitatParolaPage()
    context.acount_page = AcountPage()



def after_all(context):
    context.browser.close()