from hw_jenkins_7_10.pages.registration_page import RegistartionPage
from hw_jenkins_7_10.pages import user


def test_registration_form():
    registartion_page = RegistartionPage()

    @allure.step('Открываем главную страницу')
    registartion_page.open()
    student = user.student

    # When
    @allure.step'Заполняем форму'
    registartion_page.fill(student)

    # Then
    @allure.step'Проверяем регистрацию формы'
    registartion_page.should_have_registered(student)
