import csv
import sqlite3
import sys

from utils.connect_db import connect_to_db

#  We detected that a big cluster of customers likes a specific combination of tastes. 
#  We identified a few keywords that match these tastes: 
# _coffee_, _toast_, _green apple_, _cream_, and _citrus_ (note that these keywords are case sensitive ⚠️). 
#  We would like you to find all the wines that are related to these keywords. 
#  Check that **at least 10 users confirm those keywords**, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.
def query_favorites_taste(cursor) : 
    query = """
        SELECT DISTINCT w.name AS wine_name,
	GROUP_CONCAT(DISTINCT k.name) AS taste_keywords,
	COUNT(DISTINCT kw.keyword_id) AS nb_keywords,
	c.name As country_name,
	c.users_count
    FROM keywords_wine kw
    JOIN keywords k
        ON kw.keyword_id = k.id
    JOIN wines w
        ON kw.wine_id = w.id
    JOIN regions r
        ON w.region_id = r.id
    JOIN countries c
        ON r.country_code = c.code
    WHERE k.name IN (
            'coffee',
            'toast',
            'green apple',
            'cream',
            'citrus'
            )
        AND c.users_count >= 10
    GROUP BY w.name,
        w.id
    HAVING COUNT(DISTINCT k.name) = 5;
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
        headers = [col[0] for col in cursor.description] # get headers
        favorites_taste.insert(0, tuple(headers))
        with open("./data/CSVs/favorites_taste.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerows(favorites_taste)
    else:
        sys.exit("No rows found for query: {}".format(query))

