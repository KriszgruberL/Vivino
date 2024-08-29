import sqlite3

def connect_to_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]: 
    """Establishes a connection to the database and returns the connection and cursor."""
    try:
        connexion = sqlite3.connect("./data/vivino.db")
        cursor = connexion.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
    return connexion,cursor
    
def close_db(connexion : sqlite3.Connection) -> None: 
    """Closes the provided database connection."""
    try:
        connexion.close()
    except sqlite3.Error as e:
        print(f"Error closing the database connection: {e}")