from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CategoryPage(BasePage):

    ADIDAS_SHOE = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="4.1, | 48k, 66% , ₹3,599 , ₹1,195 ,  ₹1,025 , with Bank offer + more,  2 day delivery"]/android.view.ViewGroup[1]'


    )

    def scroll_to_shoes(self):

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )

    PRODUCT_NAMES = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text,'GlideEase M Running Shoes For Men')]"
    )

    PRODUCT_PRICES = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text,'₹1,258')]"
    )

    def get_category_products(self):
        names = self.get_elements(self.PRODUCT_NAMES)

        prices = self.get_elements(self.PRODUCT_PRICES)

        products = []

        for name, price in zip(names, prices):
            product = {

                "product_name": name.text,
                "listing_price": price.text
            }

            products.append(product)

        return products


    def open_shoe_product(self):

        self.click(self.ADIDAS_SHOE)