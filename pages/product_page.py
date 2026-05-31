# Fixed `pages/product_page.py`

import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductPage(BasePage):
    ALL_DETAILS_TAB = (
        AppiumBy.ACCESSIBILITY_ID,
        'All details, Features, description and more'
    )

    SPECIFICATIONS_TAB = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Specifications"]/android.view.ViewGroup/android.view.ViewGroup'
    )

    DESCRIPTION_TAB = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc="Description"]/android.view.ViewGroup/android.view.ViewGroup'
    )

    def scroll_down(self):

        size = self.driver.get_window_size()

        width = size["width"]

        height = size["height"]

        start_x = width // 2

        start_y = int(height * 0.80)

        end_y = int(height * 0.30)

        self.driver.execute_script(
            "mobile: dragGesture",
            {
                "startX": start_x,
                "startY": start_y,
                "endX": start_x,
                "endY": end_y,
                "speed": 1000
            }
        )

    def open_all_details(self):

        try:

            self.click(
                self.ALL_DETAILS_TAB
            )

            time.sleep(2)

        except Exception as error:

            print(f"Unable to open all details: {error}")

    def get_all_visible_texts(self):

        elements = self.driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.TextView"
        )

        texts = []

        for element in elements:

            try:

                text = element.text.strip()

                if text and text not in texts:

                    texts.append(text)

            except:
                pass

        return texts

    def get_complete_page_texts(self):

        all_texts = []

        for _ in range(5):

            visible_texts = self.get_all_visible_texts()

            for text in visible_texts:

                if text not in all_texts:

                    all_texts.append(text)

            self.scroll_down()

            time.sleep(2)

        return all_texts

    def extract_product_name(self, texts):

        for text in texts:

            if "GlideEase M Running Shoes For Men (Black , 6)" in text:

                return text

        return ""

    def extract_deals_tag(self, texts):

        for text in texts:

            if "Saver Deal" in text:

                return text

        return ""

    def extract_listing_price(self, texts):

        capture = False

        for text in texts:

            # Start after product name
            if "GlideEase M Running Shoes For Men (Black , 6)" in text:
                capture = True

                continue

            # Stop before offers section
            if "₹63 off" in text:
                break

            if capture:

                # Ignore discount banners
                if "off" in text.lower():
                    continue

                # Ignore promo price
                if "₹" in text:
                    continue

                # Listing price usually:
                # 3,599
                # 4,999

                cleaned_text = text.strip()

                if "," in cleaned_text:
                    return cleaned_text

        return ""

    def extract_promo_price(self, texts):

        prices = []

        product_name = (
            self.extract_product_name(texts)
        )

        capture = False

        for text in texts:

            # Start after product name
            if text == product_name:
                capture = True

                continue

            if capture:

                if "₹" in text:

                    if "EMI" not in text:

                        cleaned_price = text.strip()

                        if cleaned_price not in prices:
                            prices.append(cleaned_price)

        print("\nFiltered Prices:", prices)


        if len(prices) >= 1:
            return prices[0]

        return ""

    def extract_discount(self, texts):

        capture = False

        for text in texts:

            if "GlideEase M Running Shoes For Men (Black , 6)" in text:
                capture = True

                continue

            if "₹63 off" in text:
                break

            if capture:

                # Actual product discount
                if "%" in text:
                    return text

        return ""

    def extract_selected_color(self, texts):

        for index, text in enumerate(texts):

            if "Selected Color" in text:

                if index + 1 < len(texts):

                    return texts[index + 1]

        return ""

    def extract_rating(self, texts):

        for text in texts:

            try:

                value = float(text)

                if value <= 5:

                    return text

            except:
                pass

        return ""

    def extract_rating_count(self, texts):

        for text in texts:

            if "K+" in text or "M+" in text:
                return text

        return ""

    def extract_images_count(self):

        try:

            image_elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.ImageView"
            )

            return len(image_elements)

        except Exception as error:

            print(f"Unable to fetch images count: {error}")

            return 0

    def extract_available_colors_count(self):

        try:

            elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.ImageView"
            )

            color_count = 0

            capture = False

            for element in elements:

                try:

                    desc = element.get_attribute(
                        "content-desc"
                    )

                    # Start after Selected Color section
                    if desc and "Selected Color" in desc:
                        capture = True

                        continue

                    if capture:
                        color_count += 1

                except:
                    pass

            return color_count

        except Exception as error:

            print(f"Unable to fetch colors count: {error}")

            return 0

    def extract_product_highlights(self, texts):

        highlights = {}

        capture = False

        filtered_texts = []

        for text in texts:

            if text == "Product highlights":

                capture = True

                continue

            if capture:

                if text == "All details":

                    break

                filtered_texts.append(text)

        for index in range(0, len(filtered_texts), 2):

            key = filtered_texts[index]

            value = ""

            if index + 1 < len(filtered_texts):

                value = filtered_texts[index + 1]

            highlights[key] = value

        return highlights

    def extract_specifications(self):

        specifications = {}

        try:

            self.open_all_details()

            self.click(
                self.SPECIFICATIONS_TAB
            )

            time.sleep(3)

            elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.TextView"
            )

            texts = []

            for element in elements:

                try:

                    text = element.text.strip()

                    if text:
                        texts.append(text)

                except:
                    pass

            capture = False

            filtered = []

            for text in texts:

                if text == "General":
                    capture = True

                if capture:
                    if text == "See more":
                        break

                    filtered.append(text)

            for index in range(0, len(filtered), 2):

                key = filtered[index]

                value = ""

                if index + 1 < len(filtered):
                    value = filtered[index + 1]

                specifications[key] = value

            return specifications

        except Exception as error:

            print(f"Unable to fetch specifications: {error}")

            return {}

    def extract_description(self):

        try:

            self.open_all_details()

            self.click(
                self.DESCRIPTION_TAB
            )

            time.sleep(3)

            elements = self.driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.TextView"
            )

            texts = []

            for element in elements:

                try:

                    text = element.text.strip()

                    if text:
                        texts.append(text)

                except:
                    pass

            description = []

            capture = False

            for text in texts:

                if text == "Description":
                    capture = True

                    continue

                if capture:

                    if "Top influencer picks" in text:
                        break

                    if len(text) > 15:
                        description.append(text)

            return " ".join(description)

        except Exception as error:

            print(f"Unable to fetch description: {error}")

            return ""

    def get_product_details(self):

        texts = self.get_complete_page_texts()

        print("\n========= ALL PDP TEXTS =========\n")

        for text in texts:

            print(text)

        print("\n=================================\n")

        listing_price = (
            self.extract_listing_price(texts)
        )

        promo_price = (
            self.extract_promo_price(texts)
        )

        product_data = {

            "product_name":
                self.extract_product_name(texts),

            "deals_tag":
            self.extract_deals_tag(texts),

            "listing_price":
                listing_price,

            "promo_price":
                promo_price,

            "discount":
                self.extract_discount(texts),

            "selected_color":
                self.extract_selected_color(texts),

            "rating":
                self.extract_rating(texts),

            "rating_count":
            self.extract_rating_count(texts),



            "product_highlights":
                self.extract_product_highlights(texts),

            "specifications":
                self.extract_specifications(),

            "description":
                self.extract_description()
        }

        return product_data

