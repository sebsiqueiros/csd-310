import mysql.connector

try:
    db = mysql.connector.connect(
        user="root",
        password="Rockypoint10",
        host="localhost",
        database="movies"
    )

    print("Connected to MySQL!")
    print("User: root")
    print("Database: movies")

    input("Press Enter to continue...")

except mysql.connector.Error as err:
    print(err)

finally:
    if 'db' in locals():
        db.close()



