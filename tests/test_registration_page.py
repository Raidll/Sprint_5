from page_object.registration_page import RegistrationPage
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.constructor_page import ConstructorPage


class TestRegistrationPage:
    def test_registration_user_success(self, random_user_data, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_registration_button()
        login_page.click_registration_button()

        registration_page = RegistrationPage(driver)
        registration_page.waiting_visibility_name_input()
        registration_page.fill_name(random_user_data.get_name())
        registration_page.fill_email(random_user_data.get_email())
        registration_page.fill_password(random_user_data.get_password())
        registration_page.click_registration_button()

        login_page.waiting_visibility_login_button()
        login_page.fill_email(random_user_data.get_email())
        login_page.fill_password(random_user_data.get_password())
        login_page.click_login_button()

        constructor_page = ConstructorPage(driver)
        constructor_page.waiting_visibility_create_order_button()

        driver.quit()

    def test_registration_user_password_less_6_characters(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_registration_button()
        login_page.click_registration_button()

        registration_page = RegistrationPage(driver)
        registration_page.waiting_visibility_name_input()
        registration_page.fill_name("TestName")
        registration_page.fill_email("TestEmail@mail.ru")
        registration_page.fill_password("12345")
        registration_page.click_registration_button()
        registration_page.waiting_visibility_incorrect_password_notification()

        driver.quit()


