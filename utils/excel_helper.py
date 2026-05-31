from openpyxl import Workbook
import os
import json


class ExcelHelper:

    def create_excel(self, product_data):

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Flipkart Products"

        headers = [
            "Product Name",
            "Selected Color",
            "Deals Tag",
            "Listing Price",
            "Promo Price",
            "Discount",
            "Rating",
            "Rating Count",
            "Description",
            "Product Highlights",
            "Specifications",

        ]

        sheet.append(headers)

        row = [
            product_data["product_name"],
            product_data["selected_color"],
            product_data["deals_tag"],
            product_data["listing_price"],
            product_data["promo_price"],
            product_data["discount"],
            product_data["rating"],
            product_data["rating_count"],
            product_data["description"],
            json.dumps(
                product_data["product_highlights"]
            ),

            json.dumps(
                product_data["specifications"]
            ),

        ]

        sheet.append(row)

        workbook.save(
            "data/products.xlsx"
        )

        print("\nExcel file created successfully")