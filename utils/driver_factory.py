from appium import webdriver
from config.capabilities import get_capabilities


def initialize_driver():

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=get_capabilities()
    )

    return driver