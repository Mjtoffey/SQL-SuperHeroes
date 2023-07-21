from database.connection import execute_query, create_connection
import psycopg2


def read_hero():
    query = """
        SELECT * 
        FROM heroes
        """
    optupt = execute_query(query)
    if optupt:
        for row in optupt:
            id, name, about_me, biography = row
            print(f"ID: {id}, Name: {name}, About me: {about_me}, Bio: {biography}")
    
read_hero()