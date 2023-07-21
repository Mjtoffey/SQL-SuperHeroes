from database.connection import execute_query, create_connection
import psycopg2


def read_hero(name):
    query = """
        SELECT * 
        FROM heroes
        WHERE name = %s
        """
    try:
        data = execute_query(query(name))
        output = data.fetchall()
        return output
    except psycopg2.InterfaceError as e:
        print(f"The error '{e}' occurred. The cursor might already be closed")
        return None
chosen_hero = input("Who goes there?: ")
hero_data = read_hero(chosen_hero)

if hero_data:
    print("Hero:")
    for hero in hero_data:
        print(hero)
else: print(f"You shall not pass, just kidding idk who you are")
    
#read_hero()