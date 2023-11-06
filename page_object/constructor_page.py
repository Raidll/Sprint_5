from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConstructorPage:

    def __init__(self, driver):
        self.driver = driver

    CREATE_ORDER = ".//button[text()='Оформить заказ']"
    BUN_SELECTION = ".//span[text()='Булки']/parent::div"
    SAUCE_SELECTION = ".//span[text()='Соусы']/parent::div"
    FILLINGS_SELECTION = ".//span[text()='Начинки']/parent::div"

    def get_bun_selection_web_element(self):
        return self.driver.find_element(By.XPATH, self.BUN_SELECTION)

    def get_sauce_selection_web_element(self):
        return self.driver.find_element(By.XPATH, self.SAUCE_SELECTION)

    def get_filling_selection_web_element(self):
        return self.driver.find_element(By.XPATH, self.FILLINGS_SELECTION)

    def waiting_visibility_create_order_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.CREATE_ORDER)))

    def waiting_visibility_bun_selection(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.BUN_SELECTION)))

    def click_bun_selection(self):
        self.driver.find_element(By.XPATH, self.BUN_SELECTION).click()

    def waiting_visibility_sauce_selection(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.SAUCE_SELECTION)))

    def click_sauce_selection(self):
        self.driver.find_element(By.XPATH, self.SAUCE_SELECTION).click()

    def waiting_visibility_filling_selection(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.FILLINGS_SELECTION)))

    def click_filling_selection(self):
        self.driver.find_element(By.XPATH, self.FILLINGS_SELECTION).click()

    def is_bun_selected(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_attribute_to_include((By.XPATH, self.BUN_SELECTION), "class"))

    def is_bun_selected2(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, self.FILLINGS_SELECTION), "class", "tab_type_current"))
