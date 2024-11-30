import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def delete_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
        DELETE FROM Products WHERE ProductID = %s
        ''', (product_id,))

        connection.commit()
        print(f"Product with ID {product_id} deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
delete_product(1)  # Replace with the actual ProductID to delete
