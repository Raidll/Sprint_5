from page_object.forgot_password_page import ForgotPassword
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.registration_page import RegistrationPage


class TestLogin:

    def test_login_from_home_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page.waiting_visibility_create_order_button()
        driver.quit()

    def test_login_from_personal_area(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page = LoginPage(driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(driver)
        home_page.waiting_visibility_create_order_button()
        driver.quit()

    def test_login_from_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        registration_page = RegistrationPage(driver)
        registration_page.waiting_visibility_login_button()
        registration_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(driver)
        home_page.waiting_visibility_create_order_button()
        driver.quit()

    def test_login_from_forgot_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        forgot_password_page = ForgotPassword(driver)
        forgot_password_page.waiting_visibility_login_button()
        forgot_password_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(driver)
        home_page.waiting_visibility_create_order_button()
        driver.quit()
