import csv
import sqlite3
import sys

from .connect_db import close_db, connect_to_db

def query_limited_budget() : 
    co, cursor = connect_to_db()

    query = """
        select countries.name, countries.users_count
        from countries
        order by countries.users_count desc
        """

    countries_top = cursor.fetchall()   
    try : 
        cursor.execute(query)
        countries_top = cursor.fetchall()
    except (sqlite3.connector.Error, sqlite3.DatabaseError) as e:
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

