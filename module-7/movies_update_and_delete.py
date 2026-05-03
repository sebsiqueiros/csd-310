import mysql.connector

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rockypoint10",  
    database="movies"
)

cursor = db.cursor()

# function to display films
def show_films(cursor, title):

    print("\n-- {} --".format(title))

    query = """
     SELECT film_name, film_director, genre_name, studio_name
     FROM film
     INNER JOIN genre ON film.genre_id = genre.genre_id
     INNER JOIN studio ON film.studio_id = studio.studio_id
     ORDER BY film_id
     """

    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print("Film Name:", film[0])
        print("Director:", film[1])
        print("Genre Name:", film[2])
        print("Studio Name:", film[3])
        print()


# DISPLAY FILMS

show_films(cursor, "DISPLAYING FILMS")


# INSERT NEW FILM

# This is to prevent duplicates
cursor.execute("DELETE FROM film WHERE film_name = 'Inception'")
db.commit()

cursor.execute("""
INSERT INTO film 
(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES ('Inception', 2010, 148, 'Christopher Nolan', 2, 1);
""")

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


# UPDATE Alien → Horror

cursor.execute("""
UPDATE film
SET genre_id = 2
WHERE film_name = 'Alien'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")


# DELETE Gladiator

cursor.execute("""
DELETE FROM film
WHERE film_name = 'Gladiator'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor.close()
db.close()
