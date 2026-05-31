import sqlite3
import pandas as pd

DB_NAME = "flipkart_scraper"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT UNIQUE,
            selected_color TEXT,
            available_colors TEXT,
            deals_tag TEXT,
            listing_price TEXT,
            promo_price TEXT,
            discount TEXT,
            outer_material TEXT,
            occasion TEXT,
            type_for_sports TEXT,
            description TEXT,
            rating TEXT,
            rating_counts TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_product_to_sql(data_dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = '''
        INSERT OR IGNORE INTO products (
            product_name, selected_color, available_colors, deals_tag, 
            listing_price, promo_price, discount, outer_material, 
            occasion, type_for_sports, description, rating, rating_counts
        ) VALUES (
            :product_name, :selected_color, :available_colors, :deals_tag, 
            :listing_price, :promo_price, :discount, :outer_material, 
            :occasion, :type_for_sports, :description, :rating, :rating_counts
        )
    '''
    try:
        cursor.execute(query, data_dict)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database insertion failure: {e}")
    finally:
        conn.close()


def export_db_to_excel(excel_path="scraped_output.xlsx"):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    df.to_excel(excel_path, index=False)
    conn.close()
    print(f"Data successfully compiled into {excel_path}!")