import sqlite3
import csv
import sys

# We would like to select wines that are easy to find all over the world. 
# Find the top 3 most common grapes all over the world and for each grape, 
# give us the the 5 best rated wines.

def query_common_grapes(cursor : sqlite3.Cursor) -> None:
    """Executes a SQL query to retrieve the top 3 most common grapes worldwide 
    and the 5 best-rated wines for each of these grapes.
    Args:
        cursor (sqlite3.Cursor): The cursor object to execute the SQL query.
    Returns:
        None
    Raises:
        sqlite3.Error: If a database error occurs.
        sqlite3.DatabaseError: If a database error occurs.
        Exception: If an unexpected error occurs."""
 
    query = """ 
    SELECT
            grapes.name,
            COUNT(DISTINCT most_used_grapes_per_country.country_code) AS country_count
    FROM 
            most_used_grapes_per_country
            JOIN grapes 
                ON most_used_grapes_per_country.grape_id = grapes.id 
            GROUP BY
                grapes.name
            ORDER BY
                country_count DESC,
                grapes.name;
    """
    try:
        most_to_least_common_grapes = [row[0] for row in cursor.execute(query)]
        nb_common_grapes = 3

        if not most_to_least_common_grapes:
            sys.exit("No rows found for query: {}".format(query))
        
        with open(f"./data/CSVs/common_grapes_best_wines.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Grape", "Country", "Wine name", "Wine rating average", "Wine ratings count"])
    
            for i in range(nb_common_grapes):
                best_wine_per_grape_query = f""" SELECT 
                                    grapes.name,
                                    regions.country_code,
                                    wines.name,
                                    wines.ratings_average,
                                    wines.ratings_count
                                FROM 
                                    wines
                                    JOIN regions ON wines.region_id = regions.id
                                    JOIN most_used_grapes_per_country AS mugc ON regions.country_code = mugc.country_code
                                    JOIN grapes ON mugc.grape_id = grapes.id
                                WHERE grapes.name = "{most_to_least_common_grapes[i]}"
                                ORDER BY wines.ratings_average DESC, ratings_count DESC
                                ;
                """
                cursor.execute(best_wine_per_grape_query)            
                for row in cursor.fetchall():
                    writer.writerow(row)
            
        print(f"OK : data for the top 3 common grapes written into CSV file.")

    except (sqlite3.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")        