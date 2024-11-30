import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Manar2222$',
        database='inventory_db'  # Replace with your actual database name
    )
    return connection


def fetch_supplier_product_report():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        # SQL query to join Products and Suppliers and concatenate product details
        cursor.execute('''
        SELECT 
            Suppliers.SupplierName,
            GROUP_CONCAT(
                CONCAT(Products.ProductName, ' (', Products.Category, ') - Stock: ', Products.StockLevel)
                ORDER BY Products.ProductName
            ) AS ProductDetails
        FROM 
            Suppliers
        INNER JOIN 
            Products ON Suppliers.SupplierID = Products.SupplierID
        WHERE 
            Products.StockLevel > 0  # Optional: To only show products in stock
        GROUP BY 
            Suppliers.SupplierID
        ''')

        results = cursor.fetchall()

        # Print the report
        print("Supplier Product Report:")
        for row in results:
            print(f"Supplier: {row[0]}")
            print(f"Products: {row[1]}")
            print("=" * 50)

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


# Example usage
fetch_supplier_product_report()
