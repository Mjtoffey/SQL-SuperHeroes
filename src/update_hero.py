from database.connection import execute_query, create_connection
import psycopg2




chosen_hero = input("Who goes there?: ")
new_name = input("How about a new alias?: ")
new_about_me = input("New profile?: ")
new_biography = input("Might wanna make a new backstory while were at it: ")

def update_hero(chosen_hero, name, about_me, biography):
    query = """
        UPDATE heroes
        SET name = %s, about_me = %s, biography = %s
        WHERE name = %s
        """
    execute_query(quit,(chosen_hero, name, about_me, biography))

update_hero(chosen_hero, new_name, new_about_me, new_biography)