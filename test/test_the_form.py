from data import users
from model.pages.registration_page import RegistrationPage

def test_complete_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.user)
    registration_page.should_registered_user_with(users.user)

