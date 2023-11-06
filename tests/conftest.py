import pytest
from faker import Faker
from user_data import UserData
from selenium import webdriver


@pytest.fixture
def random_user_data():
    faker = Faker()
    return UserData(faker.name(), faker.email(), faker.password())


@pytest.fixture
def driver():
    new_driver = webdriver.Chrome()
    return new_driver
