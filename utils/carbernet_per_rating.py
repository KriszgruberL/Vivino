import sqlite3
import csv

def query_cabernet_by_rating(cursor : sqlite3.Cursor) -> None : 
    
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
    
    try : 
        cursor.execute(cabernet_by_rating)
    except (sqlite3.Error, sqlite3.DatabaseError) as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    try:
        with open("./data/CSVs/cabernet_by_rating.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            writer.writerow(["Grape Name", "Country", "Region", "Wine", "Wine rating average", "Wine rating count"])
            
            for row in cursor.fetchall():
                writer.writerow(row)
                
        print("OK. Data written into ./data/cabernet_by_rating.csv")
    except IOError as e:
        print(f"An error occurred when writing the file: {e}")
    
    