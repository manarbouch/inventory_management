import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def add_supplier(supplier_name, contact_info, address):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
        INSERT INTO Suppliers (SupplierName, ContactInfo, Address)
        VALUES (%s, %s, %s)
        ''', (supplier_name, contact_info, address))

        connection.commit()
        print(f"Supplier '{supplier_name}' added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
add_supplier("ABC Electronics", "abc@electronics.com", "123 Tech St.")
