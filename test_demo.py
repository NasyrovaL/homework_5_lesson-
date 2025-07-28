import os
from selene import browser, be, have


def test_form():
    file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').should(be.blank).type('Тестина')
    browser.element('#lastName').should(be.blank).type('Тестовая')
    browser.element('#userEmail').should(be.blank).type('testinaT@mail.ru')
    browser.element('[for=gender-radio-2]').should(be.visible).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').type('April')
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').type('1987')
    browser.element('.react-datepicker__day--016').click()
    browser.element('#subjectsInput').should(be.blank).type('Physics').press_enter()
    browser.all('.custom-control').element_by(have.exact_text('Reading')).click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').should(be.blank).type('Тестовая ул. 5')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').should(be.visible).press_enter()
    # проверка формы
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Тестина Тестовая',
        'testinaT@mail.ru',
        'Female',
        '1234567890',
        '15 April,1987',
        'Physics',
        'Reading',
        'file.txt',
        'Тестовая ул. 5',
        'Haryana Karnal'
    ))
