import sqlite3
import csv
import sys

# We would like to create a country leaderboard. 
# Come up with a visual that shows the average wine rating for each country. 
# Do the same for the vintages.

def query_best_vintage_and_wine_per_country (cursor : sqlite3.Cursor) -> None:
    """
    Executes SQL queries to retrieve the average vintage ratings and average wine ratings per country, 
    then writes the results to separate CSV files.
    Args:
        cursor (sqlite3.Cursor): The cursor object to execute SQL queries.
    Writes:
        - "./data/CSVs/vintage_rating_per_country.csv": CSV file containing the average vintage rating per country.
        - "./data/CSVs/wines_rating_per_country.csv": CSV file containing the average wine rating per country.
    Raises:
        sqlite3.Error: If a database error occurs.
        sqlite3.DatabaseError: If a database error occurs.
        Exception: If an unexpected error occurs.
    """
    
    vintage_rating_per_country_query = """
        SELECT 
            regions.country_code,
            round(avg(vintages.ratings_average),1)
        FROM
            vintages
            JOIN wines ON vintages.wine_id = wines.id
            JOIN regions ON wines.region_id = regions.id
        GROUP BY regions.country_code
        ;"""

    wines_rating_per_country_query = """
        SELECT
            regions.country_code,
            round(avg(wines.ratings_average),1)
        FROM
            wines
            JOIN regions ON wines.region_id = regions.id
        GROUP BY regions.country_code
        ;"""

    try:
        cursor.execute(vintage_rating_per_country_query)
        with open("./data/CSVs/vintage_rating_per_country.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Country", "Vintage rating average"])
            for row in cursor.fetchall():
                writer.writerow(row)
        print("OK. Data written into ./data/CSVs/vintage_rating_per_country.csv")    

        cursor.execute(wines_rating_per_country_query)
        with open("./data/CSVs/wines_rating_per_country.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Country", "Wine rating average"])
            for row in cursor.fetchall():
                writer.writerow(row)
        print("OK. Data written into ./data/CSVs/wines_rating_per_country.csv")

    except (sqlite3.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  

