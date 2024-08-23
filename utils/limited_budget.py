import csv
import sqlite3
import sys

from utils.connect_db import connect_to_db

# - We have a limited marketing budget for this year. Which country should we prioritise and why?
def query_limited_budget(cursor) : 
    query = """
        SELECT countries.name,
            countries.users_count,
            wines.name AS wine_name,
            wines.ratings_average AS wine_ratings_avg,
            COUNT(wines.id) AS count_wines
        FROM countries
        JOIN regions
            ON regions.country_code = countries.code
        JOIN wines
            ON wines.region_id = regions.id
        GROUP BY countries.name,
            countries.users_count
        ORDER BY countries.users_count DESC
        """
        
    try : 
        cursor.execute(query)
        countries_top = cursor.fetchall()
    except (sqlite3.Error, sqlite3.DatabaseError)  as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

    # Continue only if there are rows returned.
    if countries_top:
        headers = [col[0] for col in cursor.description] # get headers
        countries_top.insert(0, tuple(headers))
        with open("./data/CSVs/limited_budget.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(countries_top)
    else:
        sys.exit("No rows found for query: {}".format(query))

