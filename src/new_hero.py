from database.connection import execute_query, create_connection
import psycopg2

def create_new_hero(name, about_me, biography):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, (name, about_me, biography))

create_new_hero("Aang", "Appa, yip yip!", "Just a kid trying to save the world and learn about the elements")

