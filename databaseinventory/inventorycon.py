import mysql.connector

def create_connection():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',  # Replace with your MySQL username
            password='Manar2222$',  # Replace with your MySQL password
            database='inventory_db'  # Add your database name here (optional)
        )
        if connection.is_connected():
            print("Connected to MySQL Server")
            return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Connection closed")

# Example of using the connection
if __name__ == "__main__":
    conn = create_connection()

    if conn:
        # You can now perform operations on the database (queries, inserts, etc.)
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")  # Sample query to list all databases
        databases = cursor.fetchall()
        print("Databases:", databases)

        # Don't forget to close the connection after operations
        close_connection(conn)
