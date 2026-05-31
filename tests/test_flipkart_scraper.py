import time


from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.database_helper import DatabaseHelper
from utils.excel_helper import ExcelHelper



def test_search_adidas_product(driver):

    home_page = HomePage(driver)
    category_page = CategoryPage(driver)
    product_page = ProductPage(driver)
    database=DatabaseHelper()
    excel = ExcelHelper()


    home_page.search_product("ADIDAS")
    category_page.scroll_to_shoes()

    time.sleep(3)

    category_page.open_shoe_product()

    time.sleep(3)

    product_data = ( product_page.get_product_details() )
    print("\n")
    print("\n========= FINAL PRODUCT DATA =========\n")

    for key, value in product_data.items():
        print(f"{key} : {value}")

    print("\n======================================")

    database.insert_product(product_data)

    excel.create_excel(product_data)

    print("Search completed successfully")