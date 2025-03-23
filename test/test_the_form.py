import allure
from model.pages.registration_page import RegistrationPage


@allure.tag("allure test #1")
@allure.label("owner", "EL")
@allure.feature('Регистрация пользователя')
@allure.story('Регистрация пользователя с заполнением всех полей')
@allure.link("https://github.com", name='Testing')
def test_registers_user():
    registration_page = RegistrationPage()
    (registration_page.open()
     .fill_first_name('Elena')
     .fill_last_name('Ladyzhets')
     .fill_email('eladyzhets@mail.com')
     .select_gender('Female')
     .fill_mobile_number('9405979885')
     .fill_date_of_birth(1997, 10, 15)
     .fill_subject('Maths')
     .scroll_page()
     .select_hobby('Sports')
     .set_upload_picture('1.jpg')
     .fill_current_address('825 W. Sycamore st.')
     .fill_state('NCR')
     .fill_city('Delhi')
     .click_submit_button()
     .should_have_registered('Elena', 'Ladyzhets', 'eladyzhets@mail.com', 'Female', '9405979885', '15 November,1997',
                             'Maths', 'Sports', '1.jpg', '825 W. Sycamore st.', 'NCR', 'Delhi'))