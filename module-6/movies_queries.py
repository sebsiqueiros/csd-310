import mysql.connector

# database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rockypoint10",
    database="movies"
)

# cursor
cursor = db.cursor()

# DISPLAYING Studio Records
print("\n -- DISPLAYING Studio RECORDS --")

cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()

for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}\n")

# DISPLAYING Genre Records
print("\n -- DISPLAYING Genre RECORDS --")

cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()

for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}\n")

# DISPLAYING Short Film Records
print("\n -- DISPLAYING Short Film RECORDS --")

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

films = cursor.fetchall()

for film in films:
    print(f"Film Name: {film[0]}")
    print(f"Runtime: {film[1]}\n")

# DISPLAYING Director Records in Order
print("\n -- DISPLAYING Director RECORDS in Order --")

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

directors = cursor.fetchall()

for director in directors:
    print(f"Film Name: {director[0]}")
    print(f"Director: {director[1]}\n")

db.close()


