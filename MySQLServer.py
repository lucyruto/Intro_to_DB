import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (no DB selected yet)
        connection = mysql.connector.connect(
            host="localhost",       # or your server IP
            user="root",            # replace with your MySQL username
            password="yourpassword" # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Unable to connect or create database. Details: {err}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            # connection was never established
            pass

if __name__ == "__main__":
    create_database()