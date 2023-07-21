from psycopg2 import connect, OperationalError
from database.connection import create_connection, execute_query 



def read_heroes():
    query = """
        SELECT * FROM heroes;
    """
    hero_list = execute_query(query) 
    for item in hero_list:
        print(item[1])
    
read_heroes()


    
