from database.connection import execute_modify


def create_new_hero(name, about_me, biography):
    name = input ("New hero Name: ")
    about_me = input ("About new hero: ")
    biography = input ("New hero Biography: ")
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_modify(query, (name, about_me, biography))
    print(f"New Hero successfully created")

create_new_hero("","","")

