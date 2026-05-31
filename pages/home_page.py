from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):

    # SEARCH_BOX = (
    #     AppiumBy.XPATH, '//android.widget.TextView[@text="mobiles"]'
    # )
    #
    # SEARCH_INPUT = (
    #     AppiumBy.CLASS_NAME, 'android.widget.EditText'
    #
    # )

    def search_product(self, product_name):

        self.tap_by_coordinates(370, 450)


        self.driver.execute_script(
            "mobile: type",
            {
                "text": product_name
            }
        )

        self.driver.press_keycode(66)