import csv
import sqlite3
import sys

from .connect_db import close_db, connect_to_db

def query_top_wineries() : 
    co, cursor = connect_to_db()

    query = """
            select  wines.winery_id,
                    avg(wines.ratings_average) as average_rating,
                    count(wines.id) as number_of_wines
            from wines
            group by wines.winery_id
            order by average_rating desc
            """
                
    try : 
        cursor.execute(query)
        top_wineries = cursor.fetchall()
    except (sqlite3.connector.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

    # Continue only if there are rows returned.
    if top_wineries:
        headers = [col[0] for col in cursor.description] # get headers
        top_wineries.insert(0, tuple(headers))
        with open("./data/CSVs/top_wineries.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(top_wineries)
    else:
        sys.exit("No rows found for query: {}".format(query))

