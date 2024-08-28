<p align="center">
    <br>
    <a href="https://github.com/KriszgruberL" target="_blank">
        <img alt="Made with Frogs" src="./assets/made-with-🐸.svg" style="border-radius:0.5rem">
    </a>
    <a href="https://github.com/AdrienPiette" target="_blank">
        <img alt="Made with AdrienPiette" src="assets/with-adrienpiette.svg" style="border-radius:0.5rem">
    </a>
    <br>
    <a href="https://github.com/ness015618" target="_blank">
        <img alt="Made with ness015618" src="assets/with-ness015618.svg" style="border-radius:0.5rem">
    </a>
    <a href="https://github.com/RachaelShenRq" target="_blank">
        <img alt="Made with RachaelShenRq" src="assets/with-rachaelshenrq.svg" style="border-radius:0.5rem">
    </a>
    <br>
    <br>
    <a><img src="./assets/vivono_logo.png" width="350" /></a>
    <br>
    <a href="dotdotdot" target="_blank">
        <img alt="Deployed on streamlit" src="https://img.shields.io/badge/Deployed_on_Streamlit%20-%20Streamlit?style=for-the-badge&logo=streamlit&logoColor=black&logoSize=auto&labelColor=%23F6A296&color=%23FFDAB9" style="border-radius:0.5rem">
    </a>
    <br>
    <h2 align="center">Using:</h2>
</p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3120/">
        <img alt="Python 3.12" src="https://img.shields.io/badge/Python_3.12%20-%20Python?style=for-the-badge&logo=python&logoSize=auto&labelColor=%23FFDAB9&color=%23FFDAB9" style="border-radius:0.5rem">
    </a>
    <a href="https://www.sqlite.org/docs.html">
        <img alt="SQLite3" src="https://img.shields.io/badge/SQLite3%20-%20SQLite3?style=for-the-badge&logo=sqlite&logoColor=white&logoSize=auto&labelColor=%23F08080&color=%23F08080" style="border-radius:0.5rem">
    </a>
    <a href="https://docs.streamlit.io/" target="_blank">
        <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit%20-%20Streamlit?style=for-the-badge&logo=streamlit&logoColor=white&logoSize=auto&labelColor=%23B45F5F&color=%23B45F5F" style="border-radius:0.5rem">
    </a>
</p>



## 📚 Overview

  This initiative is dedicated to leveraging data insights to drive informed decision-making in the wine industry. Our aim is to use detailed wine data to identify key trends, uncover valuable insights, and provide actionable recommendations. 

## 🕺 Collaborators
Thank you for your contributions to this project : 

- [AdrienPiette](https://github.com/AdrienPiette)
- [ness015618](https://github.com/ness015618)
- [RachaelShenRq](https://github.com/RachaelShenRq)
- [KriszgruberL](https://github.com/KriszgruberL)


## 🎙️ Deployed
to add 

## 🚧 Project Structure
```
Vivino/
├── assets/
│   ├── all that is displayed in the README.md
├── data/
│   ├── CSVs/
│   │   ├── .csv generated by the /utils/*.py
│   ├── vivino.db
├── utils/
│   ├── __init__.py
│   ├── scripts to generate .csv using queries
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

2. To run the streamlit, execute the `streamlit_vivino.py` script:
    ```sh
    streamlit run visualisations/streamlit_vivino.py
    ```

---
## Visuals

<p align="center">
    <strong>Correlation Matrix of Wine Characteristics</strong>
    <br>
    <img src="/assets/image.png" alt="Correlation Matrix" width="60%">
</p>
<br>

<p align="center">
    <strong>Top 3 Wineries with the Highest Average Rating</strong>
    <br>
    <img src="/assets/image2.png" alt="Top 3 Wineries" width="60%">
</p>
<br>
<p align="center">
    <strong>Top 10 Wines by Average Rating Count</strong>
    <br>
    <img src="/assets/image3.png" alt="Top 10 Wines" width="60%">
</p>

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

The rest of the files are the same with different queries

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
     - **Queries Overview**: Explains specific SQL queries used in the project, along with their optimization strategies.
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

- **vivino.db**: 
    - The SQLite database containing the raw data used for generating the CSV files. This database includes tables with detailed information on wines, regions, grapes, ratings, and user interactions, serving as the primary data source for the project.
---
#### **Other Files**

- `.gitignore`: Specifies which files and directories to ignore in Git.
- `README.md`: Provides an overview and instructions for the project.
- `requirements.txt`: Lists required Python packages and their versions.

---

## 📃 Libraries documentation

- **[Sqlite3](https://docs.python.org/3/library/sqlite3.html)**
- **[Pandas](https://pandas.pydata.org/docs/)**
- **[Streamlit](https://docs.streamlit.io/)**
- **[Plotly](https://plotly.com/python/)**
- **[Streamlit-aggrid](https://pypi.org/project/streamlit-aggrid/)**

## 🎯 Requirements

- `pandas`
- `streamlit`
- `plotly`
- `streamlit-aggrid`

