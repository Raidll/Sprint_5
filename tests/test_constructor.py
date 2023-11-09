from page_object.constructor_page import ConstructorPage
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from selenium import webdriver


class TestConstructor:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_select_bun_tab(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(self.driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        constructor_page = ConstructorPage(self.driver)
        constructor_page.waiting_visibility_sauce_selection()
        constructor_page.click_sauce_selection()
        constructor_page.waiting_visibility_bun_selection()
        constructor_page.click_bun_selection()

        assert "tab_tab_type_current" in constructor_page.get_bun_selection_web_element().get_attribute(
            "class")

    def test_select_sauce_tab(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(self.driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        constructor_page = ConstructorPage(self.driver)
        constructor_page.waiting_visibility_sauce_selection()
        constructor_page.click_sauce_selection()

        assert "tab_tab_type_current" in constructor_page.get_sauce_selection_web_element().get_attribute(
            "class")

    def test_select_filling_tab(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        home_page = HomePage(self.driver)

        home_page.waiting_visibility_login_button()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.waiting_visibility_email_input()
        login_page.fill_email("andrey_yakovlev_2_11@mail.ru")
        login_page.fill_password("TestPassword")
        login_page.click_login_button()

        constructor_page = ConstructorPage(self.driver)
        constructor_page.waiting_visibility_filling_selection()
        constructor_page.click_filling_selection()

        assert "tab_tab_type_current" in constructor_page.get_filling_selection_web_element().get_attribute(
            "class")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
