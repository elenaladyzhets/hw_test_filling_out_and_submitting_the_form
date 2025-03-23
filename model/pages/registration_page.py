import allure,os
from selene import have, command, be
from selene.support.shared import browser

import test
from data.users import user
from model.resource import path


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#gender-radio-2 + .custom-control-label')
        self.user_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.all(".custom-control-label")
        self.upload_picture = browser.element("#uploadPicture")
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#state')
        self.city = browser.element('#city')

    @allure.step("Открытие страницы")
    def open(self):
        browser.open('/automation-practice-form')

        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    @allure.step("Ввод имени")
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    @allure.step("Ввод фамилии")
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    @allure.step("Ввод почты")
    def fill_email(self, value):
        self.email.type(value)
        return self

    @allure.step("Выбор пола")
    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    @allure.step("Ввод телефона")
    def fill_mobile_number(self, value):
        self.user_number.type(value)
        return self

    @allure.step("Выбор даты рождения")
    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.year.click().element(f'[value="{year}"]').click()
        self.month.click().element(f'[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    @allure.step("Выбор предмета")
    def fill_subject(self, value):
        self.subjects_input.type(value).press_enter()
        return self

    @allure.step("Выбор хобби")
    def select_hobby(self, value):
        self.hobbies.element_by(have.text(value)).click()
        return self

    @allure.step("Загрузка картинки")
    def set_upload_picture(self, value):
        self.upload_picture.type(os.path.abspath(os.path.join(os.path.dirname(test.__file__), f'resources/{value}')))
        return self

    @allure.step("Ввод адреса проживания")
    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    @allure.step("Выбор штата")
    def fill_state(self, value):
        self.state.click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Выбор города")
    def fill_city(self, value):
        self.city.click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    @allure.step("Нажатие на кнопку Подтвердить")
    def click_submit_button(self):
        browser.element('#submit').should(be.visible).click()
        return self

    @allure.step("Проверка отображения данных о пользователе")
    def should_have_registered(self, first_name, last_name, email, gender, phone_number, date_of_birth, subject,
                               hobbie, picture, address, state, city):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{first_name} {last_name}', email, gender, phone_number, date_of_birth,
            subject, hobbie, picture, address, f'{state} {city}'.strip()))
        return self

    @allure.step("Скролл страницы")
    def scroll_page(self):
        browser.execute_script('window.scrollBy(0, 400);')
        return self

