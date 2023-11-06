from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    REGISTRATION_BUTTON = ".//a[text()='Зарегистрироваться']"
    INPUT_EMAIL = ".//label[text()='Email']/following-sibling::input"
    INPUT_PASSWORD = ".//label[text()='Пароль']/following-sibling::input"
    LOGIN_BUTTON = ".//button[text() = 'Войти']"

    def waiting_visibility_registration_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.REGISTRATION_BUTTON)))

    def click_registration_button(self):
        self.driver.find_element(By.XPATH, self.REGISTRATION_BUTTON).click()

    def fill_email(self, email):
        self.driver.find_element(By.XPATH, self.INPUT_EMAIL).send_keys(email)

    def waiting_visibility_email_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.INPUT_EMAIL)))

    def fill_password(self, password):
        self.driver.find_element(By.XPATH, self.INPUT_PASSWORD).send_keys(password)

    def waiting_visibility_login_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

