import csv
import sqlite3
import sys

# - We want to highlight 10 wines to increase our sales. 
# Which ones should we choose and why?

def query_top_wineries(cursor : sqlite3.Cursor) -> None: 
    """Executes a SQL query to retrieve the top wineries based on average rating.
    Args:
        cursor: The database cursor object.
    Returns:
        None
    Raises:
        sqlite3.Error: If a database error occurs.
        sqlite3.DatabaseError: If a database error occurs.
        Exception: If an unexpected error occurs."""

    query = """
            SELECT wines.winery_id,
                GROUP_CONCAT(wines.name) AS wines_name,
                AVG(wines.ratings_average) AS average_rating,
                COUNT(wines.id) AS number_of_wines,
                SUM(wines.ratings_count) AS total_rating,
                AVG(wines.ratings_count) AS avg_rating_count
            FROM wines
            GROUP BY wines.winery_id
            ORDER BY average_rating DESC
            """
                
    try : 
        cursor.execute(query)
        top_wineries = cursor.fetchall()
    except (sqlite3.Error, sqlite3.DatabaseError)  as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

    # Continue only if there are rows returned.
    if top_wineries:
        headers = [col[0] for col in cursor.description] # get headers
        top_wineries.insert(0, tuple(headers))
        try : 
            with open("./data/CSVs/top_wineries.csv", 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerows(top_wineries)
        except IOError as e:
            print(f"An error occurred when writing the file: {e}")
    else:
        sys.exit("No rows found for query: {}".format(query))

