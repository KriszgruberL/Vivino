import sqlite3

def connect_to_db() : 
    """Establishes a connection to the database and returns the connection and cursor."""
    connexion = sqlite3.connect("./data/vivino.db")
    cursor = connexion.cursor()
    return connexion,cursor
    
def close_db(connexion) : 
    """Closes the provided database connection."""
    connexion.close()