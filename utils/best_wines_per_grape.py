import sqlite3
import csv

conn = sqlite3.connect("./data/vivino.db")
cursor = conn.cursor()

most_common_grapes = """ SELECT
                                grapes.name,
                                COUNT(DISTINCT most_used_grapes_per_country.country_code) AS country_count
                            FROM 
                                most_used_grapes_per_country
                                JOIN grapes ON most_used_grapes_per_country.grape_id = grapes.id 
                            GROUP BY
                                grapes.name
                            ORDER BY
                                country_count DESC,
                                grapes.name
                            ;
                            """

most_to_least_common_grapes = [row[0] for row in cursor.execute(most_common_grapes)]
#print(most_to_least_common_grapes)

nb_podium = 5
i = 0

try:
    while i < nb_podium:
        best_wine_per_grape = f""" SELECT 
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
        cursor.execute(best_wine_per_grape)
        # attention ligne suivante : si re-run, les cépages renommés risquent d'avoir les colonnes vides
        most_to_least_common_grapes[i] = most_to_least_common_grapes[i].replace(' ','_').replace('/','_')
        with open(f"./data/CSVs/common_grape_{i+1}_{most_to_least_common_grapes[i]}_best_wines.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Grape", "Country", "Wine name", "Wine rating average", "Wine ratings count"])
            for row in cursor.fetchall():
                writer.writerow(row)
        print(f"OK : {most_to_least_common_grapes[i]} data written into CSV file.")
        i += 1

finally:
    conn.close()
    print("DB connection closed.") 