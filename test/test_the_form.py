from model.pages.registration_page import RegistrationPage

def test_complete_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()


    registration_page.fill_first_name('Elena')
    registration_page.fill_last_name('Ladyzhets')
    registration_page.fill_email('eladyzhets@gmail.com')
    registration_page.select_gender('Female')
    registration_page.fill_phone_number('9405979553')
    registration_page.fill_date_of_birth(year='1997', month='November', day='05')
    registration_page.select_subject('Physics')
    registration_page.select_subject('Maths')
    registration_page.select_hobby('Sports')
    registration_page.select_hobby('Reading')
    registration_page.select_hobby('Music')
    registration_page.upload_avatar('1.jpg')
    registration_page.fill_address('825 W.Sycamore st.')
    registration_page.select_state('NCR')
    registration_page.select_city('Noida')
    registration_page.submit()


    registration_page.should_registered_user_with(
        full_name='Elena Ladyzhets',
        email='eladyzhets@gmail.com',
        gender='Female',
        phone='9405979553',
        date_of_birth='05 November,1997',
        subjects='Physics, Maths',
        hobbies='Sports, Reading, Music',
        file_name='1.jpg',
        address='825 W.Sycamore st.',
        state='NCR',
        city='Noida')

