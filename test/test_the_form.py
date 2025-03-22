from selene import browser, have, be
import allure

def test_practice_form(setup_browser):
    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element('[id="firstName"]').should(be.blank).type('Elena')
        browser.element('[id="lastName"]').should(be.blank).type('Ladyzhets')
        browser.element('[id="userEmail"]').should(be.blank).type('eladyzhets@gmail.com')
        browser.element('[for="gender-radio-2"]').click()
        browser.element('[id="userNumber"]').should(be.blank).type('9405979554')
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click().element('[value="10"]').click()
        browser.element('[class="react-datepicker__year-select"]').click().element('[value="1997"]').click()
        browser.element('[class="react-datepicker__day react-datepicker__day--005"]').click()
        browser.element('[id="subjectsInput"]').set_value('ma').element('//*[contains(text(),"Maths")]').click()
        browser.element('[for="hobbies-checkbox-1"]').click()
        #browser.element('[id="uploadPicture"]').type(os.path.abspath('../data/1.jpg'))
        browser.element('[id="currentAddress"]').should(be.blank).type('825 W. Sycamore st.')
        browser.element('[id="react-select-3-input"]').set_value('Hary').element('//*[contains(text(),"Haryana")]').click()
        browser.element('[id="react-select-4-input"]').set_value('Kar').element('//*[contains(text(),"Karnal")]').click()
        browser.element('[id="submit"]').click()

    with allure.step("Check form results"):
        browser.element('[class="modal-content"]').should(be.visible)
        browser.element('[class="modal-content"]').should(have.text('Elena Ladyzhets')) #Student Name
        browser.element('[class="modal-content"]').should(have.text('eladyzhets@gmail.com')) #Student Email
        browser.element('[class="modal-content"]').should(have.text('Female')) #Gender
        browser.element('[class="modal-content"]').should(have.text('9405979554')) #Mobile
        browser.element('[class="modal-content"]').should(have.text('05 November,1997')) #Date of Birth
        browser.element('[class="modal-content"]').should(have.text('Maths')) #Subjects
        browser.element('[class="modal-content"]').should(have.text('Sport')) #Hobbies
        #browser.element('[class="modal-content"]').should(have.text('1.jpg'))
        browser.element('[class="modal-content"]').should(have.text('825 W. Sycamore st.'))
        browser.element('[class="modal-content"]').should(have.text('Haryana Karnal'))