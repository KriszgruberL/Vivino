import csv
import sqlite3
import sys

from utils.connect_db import connect_to_db

# - We want to highlight 10 wines to increase our sales. 
# Which ones should we choose and why?
def query_top_wineries(cursor) : 

    # count(wineries) as number_of_wineries

    query = """
            select  wines.winery_id,
                    group_concat(wines.name) as wines_name,
                    avg(wines.ratings_average) as average_rating,
                    count(wines.id) as number_of_wines,
                    sum(wines.ratings_count) as total_rating,
                    avg(wines.ratings_count) as avg_rating_count
            from wines
            group by wines.winery_id
            order by average_rating desc
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
        with open("./data/CSVs/top_wineries.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(top_wineries)
    else:
        sys.exit("No rows found for query: {}".format(query))

