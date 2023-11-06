from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPassword:
    def __init__(self, driver):
        self.driver = driver

    LOGIN_BUTTON = ".//a[@class='Auth_link__1fOlj']"

    def waiting_visibility_login_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
