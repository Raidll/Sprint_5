from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    INPUT_NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input" # Поле ввода имени
    INPUT_EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input" # Поле ввода email
    INPUT_PASSWORD = By.XPATH, "//*[text()='Пароль']/following-sibling::input" # Поле ввода пароля
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    INCORRECT_PASSWORD_NOTIFICATION = By.XPATH, ".//p[@class='input__error text_type_main-default']" #Уведомление о некорректной пароле
    LOGIN_BUTTON = By.XPATH, ".//a[text()='Войти']"

    def waiting_visibility_name_input(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.INPUT_NAME))

    def fill_name(self, text):
        self.driver.find_element(*self.INPUT_NAME).send_keys(text)

    def fill_email(self, email):
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_registration_button(self):
        self.driver.find_element(*self.REGISTRATION_BUTTON).click()

    def waiting_visibility_incorrect_password_notification(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.INCORRECT_PASSWORD_NOTIFICATION))

    def waiting_visibility_login_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.LOGIN_BUTTON))

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

