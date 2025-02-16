from selene import browser, have, be, command, query, by
import os

def test_valid_form():
    browser.open('/')
    browser.element("#fixedban").should(be.visible)

#удаление банеров
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    browser.driver.execute_script("$('header').remove()")

    browser.element("#firstName").type("Elena")
    browser.element("#lastName").type("Ladyzhets")
    browser.element("#userEmail").type("eladyzhets@gmail.com")
    browser.element("label[for='gender-radio-2']").click()
    browser.element("#userNumber").type("9405979553")

#дата рождения
    browser.element("#dateOfBirthInput").click()

    browser.element(".react-datepicker__year-select").click()
    browser.element(".react-datepicker__year-select").element("option[value='1997']").click()

    browser.element(".react-datepicker__month-select").click()
    browser.element(".react-datepicker__month-select").element("[value='10']").click()

    browser.element(".react-datepicker__day--005").click()

    browser.element("#subjectsInput").type("Physics").press_enter()

    browser.element("label[for='hobbies-checkbox-2']").should(have.exact_text('Reading')).click()
    browser.element("label[for='hobbies-checkbox-1']").should(have.exact_text('Sports')).click()

    # Загрузка изображения
    browser.element('#uploadPicture').type(os.path.abspath('images/1.jpg'))


    browser.element("#currentAddress").type("825 W. Hickory st., apt.145")

    browser.element("#state").click()
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()
    browser.element("#city").click()
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Panipat')).click()

    browser.element("#submit").click()

#Проверки по всем эоементам
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.table').should(have.text('Elena Ladyzhets'))
    browser.element('.table').should(have.text('eladyzhets@gmail.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('9405979553'))
    browser.element('.table').should(have.text('05 November,1997'))
    browser.element('.table').should(have.text('Physics'))
    browser.element('.table').should(have.text('Reading, Sports'))
    browser.element('.table').should(have.text('1.jpg'))
    browser.element('.table').should(have.text('825 W. Hickory st., apt.145'))
    browser.element('.table').should(have.text('Haryana Panipat'))

    browser.element('#closeLargeModal').should(be.visible).click()






