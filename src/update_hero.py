from database.connection import execute_query, create_connection
import psycopg2



def update_hero(about_me):
    about_me = input ("Any new developments?: ")
    query = """
        UPDATE heroes
        SET about_me = %s
        WHERE %s = name
        """
    execute_query(query(about_me))
    print("Heres your new info, now leave me alone")

update_hero("")