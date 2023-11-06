from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    SAVE_BUTTON = ".//button[text()='Сохранить']"
    CONSTRUCTOR_BUTTON = ".//p[text()='Конструктор']"
    STELLAR_BURGERS_LOGO = ".//div[@class='AppHeader_header__logo__2D0X2']"
    LOGOUT_BUTTON = ".//button[text()='Выход']"

    def waiting_visibility_save_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.SAVE_BUTTON)))

    def waiting_visibility_constructor_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.CONSTRUCTOR_BUTTON)))

    def click_constructor_button(self):
        self.driver.find_element(By.XPATH, self.CONSTRUCTOR_BUTTON).click()

    def waiting_visibility_logo_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.STELLAR_BURGERS_LOGO)))

    def click_logo_button(self):
        self.driver.find_element(By.XPATH, self.STELLAR_BURGERS_LOGO).click()

    def waiting_visibility_logout_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LOGOUT_BUTTON)))

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.LOGOUT_BUTTON).click()
