from page_object.forgot_password_page import ForgotPassword
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.registration_page import RegistrationPage
from selenium import webdriver


class TestLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_login_from_home_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(self.driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*home_page.CREATE_ORDER_BUTTON).text

    def test_login_from_personal_area(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*home_page.CREATE_ORDER_BUTTON).text

    def test_login_from_registration_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        registration_page = RegistrationPage(self.driver)
        registration_page.waiting_visibility_login_button()
        registration_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*home_page.CREATE_ORDER_BUTTON).text

    def test_login_from_forgot_password_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        forgot_password_page = ForgotPassword(self.driver)
        forgot_password_page.waiting_visibility_login_button()
        forgot_password_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*home_page.CREATE_ORDER_BUTTON).text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
