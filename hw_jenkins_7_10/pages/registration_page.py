from selene import browser, have
import os
from tests.conftest import RESOURCE_PATH
from hw_jenkins_7_10.pages.user import User
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "artemtrunilin")
@allure.feature("Задачи в репозитории")
@allure.link("https://github.com", name="Testing")


class RegistartionPage:
    @allure.step('Открываем форму регистрации.')
    def open(self):
        browser.open('/')

    @allure.step('Вводим имя пользователя {value}.')
    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    @allure.step('Вводим фамилию пользователя {value}.')
    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    @allure.step('Вводим email {value}.')
    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    @allure.step('Выбираем пол')
    def fill_gendare(self):
        browser.element('[for="gender-radio-1"').click()

    @allure.step('Вводим телефонный номер {value}.')
    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    @allure.step('Вводим дату рождения {year}.{month}.{day}.')
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step('Выводим предмет {value}.')
    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.step('Выбор хобби')
    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    @allure.step('Прикрепляем файл {file_name}.')
    def choose_picture(self, file_name):
        browser.element('[id="uploadPicture"]').send_keys(os.path.join(RESOURCE_PATH, file_name))

    @allure.step('Вводим адрес {value}.')
    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)

    @allure.step('Ввод страны {value}.')
    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    @allure.step('Ввод города {value}.')
    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    @allure.step('Нажимаем кнопку Submit')
    def submit(self):
        browser.element('#submit').click()

    def fill(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gendare()
        self.fill_number(user.phone_number)
        self.fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
        self.fill_subject(user.subject)
        self.fill_hobbies()
        self.choose_picture(user.picture)
        self.fill_adress(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit()

    @allure.step('Проверяем корректность введенных данных')
    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}',
                             user.email,
                             user.gender,
                             user.phone_number,
                             f'{user.birth_day} {user.birth_month},{user.birth_year}',
                             user.subject,
                             user.hobby,
                             user.picture,
                             user.address,
                             f'{user.state} {user.city}'
                             )
        )
