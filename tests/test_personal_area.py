from page_object.constructor_page import ConstructorPage
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.profile_page import ProfilePage
from selenium import webdriver


class TestPersonalArea:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_go_to_personal_area(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(self.driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        profile_page = ProfilePage(self.driver)
        profile_page.waiting_visibility_save_button()

        assert "https://stellarburgers.nomoreparties.site/account/profile" == self.driver.current_url

    def test_go_to_constructor(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        profile_page = ProfilePage(self.driver)
        profile_page.waiting_visibility_save_button()
        profile_page.waiting_visibility_constructor_button()
        profile_page.click_constructor_button()

        constructor_page = ConstructorPage(self.driver)
        constructor_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*constructor_page.CREATE_ORDER).text

    def test_go_to_constructor_click_on_logo(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        profile_page = ProfilePage(self.driver)
        profile_page.waiting_visibility_save_button()
        profile_page.waiting_visibility_logo_button()
        profile_page.click_logo_button()

        constructor_page = ConstructorPage(self.driver)
        constructor_page.waiting_visibility_create_order_button()

        assert "Оформить заказ" in self.driver.find_element(*constructor_page.CREATE_ORDER).text

    def test_logout_from_personal_area(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        home_page = HomePage(self.driver)
        home_page.waiting_visibility_personal_area_button()
        home_page.click_personal_area()

        profile_page = ProfilePage(self.driver)
        profile_page.waiting_visibility_logout_button()
        profile_page.click_logout_button()

        login_page.waiting_visibility_login_button()

        assert "https://stellarburgers.nomoreparties.site/login" == self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
