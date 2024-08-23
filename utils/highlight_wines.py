import csv
import sqlite3
import sys

from utils.connect_db import connect_to_db

# - We want to highlight 10 wines to increase our sales. 
# Which ones should we choose and why?

def query_highlight_wine(cursor) : 
    query = """
        SELECT wines.name,
            wines.ratings_average,
            SUM(wines.ratings_count) AS total_rating,
            countries.users_count
        FROM countries
        JOIN regions
            ON regions.country_code = countries.code
        JOIN wines
            ON wines.region_id = regions.id
        GROUP BY wines.name
        ORDER BY wines.ratings_average DESC,
            total_rating DESC
        """
                
    try : 
        cursor.execute(query)
        top_wine = cursor.fetchall()
    except (sqlite3.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

    # Continue only if there are rows returned.
    if top_wine:
        headers = [col[0] for col in cursor.description] # get headers
        top_wine.insert(0, tuple(headers))
        with open("./data/CSVs/highlight_wine.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(top_wine)
    else:
        sys.exit("No rows found for query: {}".format(query))

