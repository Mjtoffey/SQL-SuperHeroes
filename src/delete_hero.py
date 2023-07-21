from database.connection import execute_query, create_connection
import psycopg2

def delete_hero(): 
    name = input("Who would you like to delete?: ")
    query = """
        DELETE FROM heroes 
        WHERE name = (%s);
        """
    execute_query(query, (name,))

delete_hero()

