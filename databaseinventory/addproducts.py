import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def add_product(product_name, category, price, stock_level, reorder_level):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
        INSERT INTO Products (ProductName, Category, Price, StockLevel, ReorderLevel)
        VALUES (%s, %s, %s, %s, %s)
        ''', (product_name, category, price, stock_level, reorder_level))

        connection.commit()
        print(f"Product '{product_name}' added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
add_product("Wireless Mouse", "Electronics", 25.99, 50, 10)
