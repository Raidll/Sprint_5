from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    PERSONAL_AREA = ".//p[text()='Личный Кабинет']"  # Кнопка "Личный кабинет" на главной странице
    LOGIN_BUTTON = ".//button[text()='Войти в аккаунт']" # Кнопка войти
    CREATE_ORDER_BUTTON = ".//button[text()='Оформить заказ']" # Кнопка создания заказа

    def waiting_visibility_personal_area_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.PERSONAL_AREA)))

    def click_personal_area(self):
        self.driver.find_element(By.XPATH, self.PERSONAL_AREA).click()

    def waiting_visibility_login_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def waiting_visibility_create_order_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.CREATE_ORDER_BUTTON)))

