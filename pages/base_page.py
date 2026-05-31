from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def handle_popup_if_present(self, locator):

        try:

            popup = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )

            popup.click()

            print("Popup handled successfully")

        except TimeoutException:

            print("Popup not displayed")

    def tap_by_coordinates(self, x, y):

        finger = PointerInput("touch", "finger")

        actions = ActionChains(self.driver)

        actions.w3c_actions = ActionBuilder(
            self.driver,
            mouse=finger
        )

        actions.w3c_actions.pointer_action.move_to_location(x, y)

        actions.w3c_actions.pointer_action.pointer_down()

        actions.w3c_actions.pointer_action.pause(1)

        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()