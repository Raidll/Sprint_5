import pytest
from faker import Faker
from user_data import UserData


@pytest.fixture
def random_user_data():
    faker = Faker()
    return UserData(faker.name(), faker.email(), faker.password())
