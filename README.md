
<p align="center">
    <br>
     <a href="https://github.com/KriszgruberL" target="_blank"> <img alt="Made with Frogs" src="./assets/made-with-🐸.svg" style="border-radius:0.5rem"></a>
    <br>
    <br><br>
    <a><img src="./assets/vivono_logo.png" width="350"  /></a>
    <h2 align="center">Using:
    <br>
    <br>
    <a href="https://www.python.org/downloads/release/python-3120/"><img alt="Python 3.12" src="https://img.shields.io/badge/Python_3.12%20-%20Python?style=for-the-badge&logo=python&logoSize=auto&labelColor=%23FFDAB9&color=%23FFDAB9
    " style="border-radius:0.5rem"></a>
    <a href="https://www.sqlite.org/docs.html"><img alt="SQLite3" src="https://img.shields.io/badge/SQLite3%20-%20SQLite3?style=for-the-badge&logo=sqlite&logoColor=white&logoSize=auto&labelColor=%23F08080&color=%23F08080
    " style="border-radius:0.5rem"></a>
    <a href="https://www.sqlite.org/docs.html"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit%20-%20Streamlit?style=for-the-badge&logo=streamlit&logoColor=white&logoSize=auto&labelColor=%23FF4B4B&color=%23FF4B4B
    " style="border-radius:0.5rem"></a>
    <br>
</p>

## 📚 Overview

Lorem ipsum

## 🕺 Collaborators
Thank you for your contributions to this project : 

- [AdrienPiette](https://github.com/AdrienPiette)
- [ness015618](https://github.com/ness015618)
- [RachaelShenRq](https://github.com/RachaelShenRq)
- [KriszgruberL](https://github.com/KriszgruberL)

## 🚧 Project Structure
```
Vivino/
├── assets/
│   ├── made-with-🐸.svg
│   ├── vivono_logo.png
├── data/
│   ├── CSVs/
│   │   ├── cabernet_by_rating.csv
│   │   ├── common_grapes_best_wines.csv
│   │   ├── favorites_taste.csv
│   │   ├── highlight_wine.csv
│   │   ├── limited_budget.csv
│   │   ├── top_wineries.csv
│   │   ├── vintage_rating_per_country.csv
│   │   ├── wine_by_taste_filtered.csv
│   │   ├── wine_by_taste.csv
│   │   ├── wines_rating_per_country.csv
│   ├── vivino.db
├── utils/
│   ├── __init__.py
│   ├── best_wineries.py
│   ├── best_wines_per_grape.py
│   ├── cabrernet_per_rating.py
│   ├── connect_db.py
│   ├── country_leaderboard.py
│   ├── favorites_taste.py
│   ├── highlight_wines.py
│   ├── limited_budget.py
│   ├── wines_by_taste.py
├── visualisations/
│   ├── __init__.py
│   ├── streamlit_vivino.py
├── main.py
├── .gitignore
├── README.md
└── requirements.txt

```

## ⚒️ Setup

1. **Clone the repository**:
    ```sh
    git clone git@github.com:KriszgruberL/Vivino.git
    cd Vivino
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## ⚙️ Usage

1. To run the queries and csv writing, execute the `main.py` script:
    ```sh
    python main.py
    ```

2. To run the streamlit, execute the `main.py` script:
    ```sh
    streamlit run visualisations/streamlit_vivino.py
    ```

---
## Visuals

S'il y en a

---

### 👀 Classes Overview

---
Here’s how you can include the classes overview for the `main.py` and `streamlit_vivino.py` files, making it concise and informative:

---

### 👀 Classes Overview

#### **main.py**
The entry point of the application. It orchestrates the execution of various data processing scripts that query the database and generate CSV files.

**Functions:**
- `main()`: Connects to the database, runs a series of query functions to generate CSV reports, and then closes the database connection. The specific queries executed include:
  - `query_limited_budget(cursor)`: Prioritizes marketing efforts by country based on user counts and wine ratings.
  - `query_highlight_wine(cursor)`: Identifies top wines to highlight for increased sales.
  - `query_top_wineries(cursor)`: Lists the best wineries based on wine ratings.
  - `query_favorites_taste(cursor)`: Finds wines that match specific taste profiles.
  - `query_common_grapes(cursor)`: Determines the most common grape varieties and their top-rated wines.
  - `query_wine_by_taste(cursor)`: Retrieves top wines based on taste characteristics.
  - `query_best_vintage_and_wine_per_country(cursor)`: Generates a leaderboard for countries based on wine and vintage ratings.


---
#### **utils/**
Contains utility scripts for querying the database, processing data, and generating CSV files.

- **connect_db.py**:
  - `connect_to_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]`: Establishes a connection to the SQLite database and returns both the connection and the cursor.
  - `close_db(connexion: sqlite3.Connection) -> None`: Closes the provided database connection.

- **carbernet_per_rating.py**:
  - `query_cabernet_by_rating(cursor: sqlite3.Cursor) -> None`: Retrieves data about Cabernet Sauvignon wines, focusing on their ratings, and saves the results to a CSV file.

- **wines_by_taste.py**:
  - `query_wine_by_taste(cursor: sqlite3.Cursor) -> None`: Extracts information about top-rated wines along with their taste characteristics and writes it to a CSV file.

- **limited_budget.py**:
  - `query_limited_budget(cursor: sqlite3.Cursor) -> None`: Identifies which country should be prioritized for marketing based on user counts and wine ratings, saving the findings to a CSV file.

- **highlight_wines.py**:
  - `query_highlight_wine(cursor: sqlite3.Cursor) -> None`: Highlights the top wines to promote, based on ratings and user counts, and outputs the data to a CSV file.

- **best_wineries.py**:
  - `query_top_wineries(cursor: sqlite3.Cursor) -> None`: Compiles a list of top wineries based on the average ratings of their wines and stores the results in a CSV file.

- **country_leaderboard.py**:
  - `query_best_vintage_and_wine_per_country(cursor: sqlite3.Cursor) -> None`: Creates a leaderboard for countries based on average vintage and wine ratings, exporting the data to CSV files.

- **best_wines_per_grape.py**:
  - `query_common_grapes(cursor: sqlite3.Cursor) -> None`: Identifies the most common grape varieties globally and lists the top-rated wines for each, saving the data to a CSV file.

- **favorites_taste.py**:
  - `query_favorites_taste(cursor: sqlite3.Cursor) -> None`: Finds wines that match specific taste profiles confirmed by user feedback and saves the results to a CSV file.

---

#### **visualisations/**

Contains scripts to create visualizations for analyzing and presenting the wine data.

- #### **streamlit_vivino.py**
   Powers the Streamlit dashboard, which visualizes wine data processed and stored in CSV files.

   **Main Features:**
   - **Data Loading**: Loads various CSV files into Pandas DataFrames for analysis.
   - **Sidebar Navigation**: Allows users to navigate between different visualizations and analysis pages.
   - **Pages**:
     - **Project Context**: Provides an overview of the project's goals and objectives.
     - **Query Overview**: Explains specific SQL queries used in the project, along with their optimization strategies.
     - **Top 10 Wines**: Visualizes the top 10 wines based on ratings and potential sales impact.
     - **Country to Prioritize**: Identifies which countries should be targeted for marketing based on user data.
     - **Top 3 Wineries**: Displays the highest-rated wineries.
     - **Customer Cluster**: Analyzes customer taste preferences and identifies wines matching those profiles.
     - **Most Common Grapes**: Showcases the most common grape varieties and their top-rated wines.
     - **Country Leaderboard**: Ranks countries based on their average wine ratings.
     - **Top 5 Cabernet Sauvignon**: Highlights the top 5 Cabernet Sauvignon wines.
     - **Top Wine by Characteristics**: Identifies wines with the highest ratings based on specific characteristics.

   **Functions:**
   - `display_aggrid_table(df, title="Table", height=400)`: Displays a DataFrame as an interactive table using AgGrid within the Streamlit application.
----

#### **data/**
Contains data files used and generated by the scripts.
- #### **CSVs/**: Directory containing the results CSVs from utils/

  This directory contains CSV files generated by the scripts in the `utils/` directory. Each CSV file holds specific data extracted and processed from the Vivino database.

  - **cabernet_by_rating.csv**:
    - Contains data about Cabernet Sauvignon wines, focusing on their ratings. The data includes grape name, country, region, wine name, average rating, and the number of ratings.

  - **common_grapes_best_wines.csv**:
    - Lists the top-rated wines associated with the three most common grape varieties globally. The data includes grape name, country, wine name, average rating, and the number of ratings.

  - **favorites_taste.csv**:
    - Contains data on wines that match specific taste keywords like coffee, toast, green apple, cream, and citrus. The file includes wine name, taste keywords, country, average rating, and the number of ratings.

  - **highlight_wine.csv**:
    - Highlights wines selected to increase sales based on their ratings. The data includes wine name, average rating, total ratings, and the number of users in the associated countries.

  - **limited_budget.csv**:
    - Provides insights into which country should be prioritized for marketing efforts based on user count and wine ratings. The data includes country name, user count, wine name, average rating, and the number of wines.

  - **top_wineries.csv**:
    - Contains information about the top wineries based on average wine ratings. The data includes winery ID, associated wines, average rating, number of wines, and total ratings.

  - **vintage_rating_per_country.csv**:
    - Shows the average vintage ratings per country. The data includes country code and the average rating of vintages.

  - **wines_rating_per_country.csv**:
    - Provides the average wine ratings per country. The data includes country code and the average rating of wines.

  - **wine_by_taste.csv**:
    - Lists wines along with their average ratings and specific taste characteristics such as acidity, fizziness, sweetness, and tannin. The data helps in analyzing how these characteristics influence wine ratings.

  - **wine_by_taste_filtered.csv**:
    - A filtered version of the `wine_by_taste.csv`, this file contains data focused on wines that meet certain taste and rating criteria, providing a more targeted analysis.
- **vivino.db**: 
    - The SQLite database containing the raw data used for generating the CSV files. This database includes tables with detailed information on wines, regions, grapes, ratings, and user interactions, serving as the primary data source for the project.
---
#### **Other Files**

- `.gitignore`: Specifies which files and directories to ignore in Git.
- `README.md`: Provides an overview and instructions for the project.
- `requirements.txt`: Lists required Python packages and their versions.

---

## 📃 Libraries documentation

- [Librarie](url_librarie)

## 🎯 Requirements

- `todo==version`
