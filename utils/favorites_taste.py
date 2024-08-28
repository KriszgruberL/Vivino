import csv
import sqlite3
import sys

#  We detected that a big cluster of customers likes a specific combination of tastes. 
#  We identified a few keywords that match these tastes: 
# _coffee_, _toast_, _green apple_, _cream_, and _citrus_ (note that these keywords are case sensitive ⚠️). 
#  We would like you to find all the wines that are related to these keywords. 
#  Check that **at least 10 users confirm those keywords**, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.

def query_favorites_taste(cursor : sqlite3.Cursor) -> None: 
    """Executes a SQL query to retrieve the favorite tastes of wines based on specific keywords.
    Args:
        cursor (sqlite3.Cursor): The cursor object to execute the SQL query.
    Returns:
        None
    Raises:
        sqlite3.Error: If a database error occurs.
        sqlite3.DatabaseError: If a database error occurs.
        Exception: If an unexpected error occurs."""
        
    query = """
    SELECT DISTINCT w.name AS wine_name,
        GROUP_CONCAT(DISTINCT k.name) AS taste_keywords,
        COUNT(DISTINCT kw.keyword_id) AS nb_keywords,
        c.name As country_name,
        w.ratings_average AS wine_rating_avg, 
        w.ratings_count AS wine_ratings_count 
    FROM keywords_wine kw
    JOIN keywords k
        ON kw.keyword_id = k.id
    JOIN wines w
        ON kw.wine_id = w.id
    JOIN regions r
        ON w.region_id = r.id
    JOIN countries c
        ON r.country_code = c.code
    WHERE 
        EXISTS (
            SELECT 1
            FROM keywords_wine kw2
            JOIN keywords k2 ON kw2.keyword_id = k2.id
            WHERE kw2.wine_id = w.id
            AND k2.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
            GROUP BY kw2.wine_id
            HAVING COUNT(DISTINCT k2.name) = 5
        )
        AND c.users_count >= 10
    GROUP BY w.name
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
        try : 
            with open("./data/CSVs/favorites_taste.csv", 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerows(favorites_taste)
        except IOError as e:
            print(f"An error occurred when writing the file: {e}")
    else:
        sys.exit("No rows found for query: {}".format(query))

