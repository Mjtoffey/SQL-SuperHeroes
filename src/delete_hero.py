from database.connection import execute_modify

def delete_hero(): 
    name = input("Who would you like to delete?: ")
    query = """
        DELETE FROM heroes 
        WHERE name = (%s);
        """
    execute_modify(query, (name,))

delete_hero()

