import json
import mysql.connector


class DatabaseHelper:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ravi@123",
            database="flipkart_scraper"
        )

        self.cursor = self.connection.cursor()

    def insert_product(self, product_data):

        query = """
        INSERT INTO products(

            product_name,
            selected_color,
            deals_tag,
            listing_price,
            promo_price,
            discount,
            product_highlights,
            specifications,
            description,
            rating,
            rating_count

        )

        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            product_data["product_name"],

            product_data["selected_color"],

            product_data["deals_tag"],

            product_data["listing_price"],

            product_data["promo_price"],

            product_data["discount"],

            json.dumps(
                product_data["product_highlights"]
            ),

            json.dumps(
                product_data["specifications"]
            ),

            product_data["description"],

            product_data["rating"],

            product_data["rating_count"]
        )
        print(values)

        self.cursor.execute(query, values)

        self.connection.commit()