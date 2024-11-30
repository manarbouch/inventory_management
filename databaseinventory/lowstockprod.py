import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def view_low_stock():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
        SELECT ProductID, ProductName, StockLevel, ReorderLevel
        FROM Products
        WHERE StockLevel <= ReorderLevel
        ''')

        low_stock_products = cursor.fetchall()

        if low_stock_products:
            print("Low-stock products:")
            for product in low_stock_products:
                print(f"Product ID: {product[0]}, Name: {product[1]}, Stock: {product[2]}, Reorder Level: {product[3]}")
        else:
            print("No low-stock products.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
view_low_stock()
