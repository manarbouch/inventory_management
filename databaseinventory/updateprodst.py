import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def update_product_stock(product_id, quantity_change):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
        UPDATE Products
        SET StockLevel = StockLevel + %s
        WHERE ProductID = %s
        ''', (quantity_change, product_id))

        connection.commit()
        print(f"Product stock updated successfully for ProductID {product_id}.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
update_product_stock(1, 20)  # Increase stock by 20 for ProductID 1
