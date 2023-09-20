from hw_jenkins_7_10.pages.registration_page import RegistartionPage
from hw_jenkins_7_10.pages import user


def test_registration_form(setup_browser):
    registartion_page = RegistartionPage()
    registartion_page.open()
    student = user.student


    # When
    registartion_page.fill(student)

    # Then
    registartion_page.should_have_registered(student)
