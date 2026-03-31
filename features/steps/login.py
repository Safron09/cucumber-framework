from behave import given, when, then
from features.pages.login_page import LoginPage


@given('Open the login page')
def open_login(context):
    context.page = LoginPage(context.driver)
    context.page.open_login()


@when('Enter username "{username}"')
def enter_username(context, username):
    context.page.enter_username(username)


@when('Enter password "{password}"')
def enter_password(context, password):
    context.page.enter_password(password)


@when('Click login button')
def click_login(context):
    context.page.submit()


@then('Player is logged in successfully')
def verify_login_success(context):
    assert context.page.is_logged_in(), "Expected player to be logged in"


@then('Error message is displayed')
def verify_error_message(context):
    error = context.page.get_error_message()
    assert error, "Expected an error message but none was displayed"
