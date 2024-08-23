import sqlite3
import csv

conn = sqlite3.connect("./data/vivino.db")
cursor = conn.cursor()

cabernet_by_rating = """ 
                        SELECT 
                            grapes.name,
                            most_used_grapes_per_country.country_code,
                            regions.name,
                            wines.name,
                            wines.ratings_average,
                            wines.ratings_count
                        FROM most_used_grapes_per_country
                            JOIN grapes ON most_used_grapes_per_country.grape_id = grapes.id
                            JOIN regions ON most_used_grapes_per_country.country_code = regions.country_code
                            JOIN wines ON regions.id = wines.region_id
                            WHERE grapes.name = "Cabernet Sauvignon"
                        ORDER BY wines.ratings_average DESC, wines.ratings_count DESC;
"""

cursor.execute(cabernet_by_rating)

try:
    with open("./data/CSVs/cabernet_by_rating.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Grape Name", "Country", "Region", "Wine", "Wine rating average", "Wine rating count"])
        
        for row in cursor.fetchall():
            writer.writerow(row)
    print("OK. Data written into ./data/cabernet_by_rating.csv")

finally:
    conn.close()
    print("DB connection closed.")