import sqlite3
import csv

conn = sqlite3.connect("./data/vivino.db")
cursor = conn.cursor()

vintage_rating_per_country = """
    SELECT 
        regions.country_code,
        round(avg(vintages.ratings_average),1)
    FROM
        vintages
        JOIN wines ON vintages.wine_id = wines.id
        JOIN regions ON wines.region_id = regions.id
    GROUP BY regions.country_code
    ;
"""

wines_rating_per_country = """
    SELECT
        regions.country_code,
        round(avg(wines.ratings_average),1)
    FROM
        wines
        JOIN regions ON wines.region_id = regions.id
    GROUP BY regions.country_code
    ;
"""

try:
    cursor.execute(vintage_rating_per_country)
    with open("./data/CSVs/vintage_rating_per_country.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "Vintage rating average"])
        for row in cursor.fetchall():
            writer.writerow(row)
    print("OK. Data written into ./data/CSVs/vintage_rating_per_country.csv")    

    cursor.execute(wines_rating_per_country)
    with open("./data/CSVs/wines_rating_per_country.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "Wine rating average"])
        for row in cursor.fetchall():
            writer.writerow(row)
    print("OK. Data written into ./data/CSVs/wines_rating_per_country.csv")

finally:
    conn.close()
    print("DB connection closed.")    