import pytest

from utils.driver_factory import initialize_driver


@pytest.fixture(scope="function")
def driver():

    driver = initialize_driver()

    yield driver

    driver.quit()