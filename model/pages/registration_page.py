
from selene import have, command, be
from selene.support.shared import browser
from data.users import User
from model import resource
from model.resource import path


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    @staticmethod
    def register(user:User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[for="gender-radio-2"]').click()
        browser.element('#userNumber').type(user.phone_number)

        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker").should(be.visible)
        browser.element(".react-datepicker__year-select").click().element(f'option[value="{user.date_of_birth.year}"]').click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f'.react-datepicker__month-select option[value="{user.date_of_birth.month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()

        browser.element('#subjectsInput').type(user.subject1).press_enter()
        browser.element('#subjectsInput').type(user.subject2).press_enter()
        browser.element('[for^="hobbies-checkbox-1"]').click()
        browser.element('[for^="hobbies-checkbox-2"]').click()
        browser.element('[for^="hobbies-checkbox-3"]').click()

        print(resource.path(user.picture))
        browser.element("#uploadPicture").set_value(resource.path(user.picture))

        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click().all('[id^=react-select-1-option]').element_by(have.text(user.state)).click()
        browser.element('#city').click().all('[id^=react-select-3-option]').element_by(have.text(user.city)).click()
        browser.element('#submit').click()

    @staticmethod
    def should_registered_user_with(user: User):
        browser.element('.table-responsive').should(have.text(f'Student Name {user.first_name} {user.last_name}'))
        browser.element('.table-responsive').should(have.text(f'Student Email {user.email}'))
        browser.element('.table-responsive').should(have.text(f'Gender {user.gender}'))
        browser.element('.table-responsive').should(have.text(f'Mobile {user.phone_number}'))
        browser.element('.table-responsive').should(
            have.text(f'Date of Birth {user.date_of_birth.year}.{user.date_of_birth.month}.{user.date_of_birth.day}'))
        browser.element('.table-responsive').should(have.text(f'Subjects {user.subject1} {user.subject2}'))
        browser.element('.table-responsive').should(have.text(f'Hobbies {user.hobby1} {user.hobby2} {user.hobby3}'))
        browser.element('.table-responsive').should(have.text(f'Picture {user.picture}'))
        browser.element('.table-responsive').should(have.text(f'Address {user.address}'))
        browser.element('.table-responsive').should(have.text(f'State and City {user.state} {user.city}'))