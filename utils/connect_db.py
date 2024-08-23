import sqlite3

def connect_to_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]: 
    """Establishes a connection to the database and returns the connection and cursor."""
    connexion = sqlite3.connect("./data/vivino.db")
    cursor = connexion.cursor()
    return connexion,cursor
    
def close_db(connexion : sqlite3.Connection) -> None: 
    """Closes the provided database connection."""
    connexion.close()