from database.connection import execute_query, create_connection
import psycopg2


def read_hero():
    query = """
        SELECT * 
        FROM heroes
        """
    read_list = execute_query(query).fetchall()
    for hero in read_list:
        print(hero[1])
    return read_list

read_hero()
    
