# vins, avg rate, count et les gouts


import csv
import sqlite3
import sys

def query_wine_by_taste(cursor : sqlite3.Cursor) -> None: 
    """Executes a SQL query to retrieve the top wines based on average rating and their tastes.
    Args:
        cursor (sqlite3.Cursor): The cursor object to execute the SQL query.
    Returns:
        None
    Raises:
        sqlite3.Error: If a database error occurs.
        sqlite3.DatabaseError: If a database error occurs.
        Exception: If an unexpected error occurs."""
        
    query = """
    SELECT DISTINCT w.name,
        w.ratings_average,
        w.ratings_count,
        w.acidity,
        w.fizziness,
        w.sweetness,
        w.tannin
    FROM WINES w
    ORDER BY w.ratings_average DESC,
        w.ratings_count DESC
    """
                
    try : 
        cursor.execute(query)
        favorites_taste = cursor.fetchall()
    except (sqlite3.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    # Continue only if there are rows returned.
    if favorites_taste:
        headers = [col[0] for col in cursor.description] # get headers from query
        favorites_taste.insert(0, tuple(headers))
        try : 
            with open("./data/CSVs/wine_by_taste.csv", 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerows(favorites_taste)
        except IOError as e:
            print(f"An error occurred when writing the file: {e}")
    else:
        sys.exit("No rows found for query: {}".format(query))

