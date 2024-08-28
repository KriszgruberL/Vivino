import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder

# Load the data
data1 = pd.read_csv("./data/CSVs/highlight_wine.csv")
data2 = pd.read_csv("./data/CSVs/limited_budget.csv")
data3 = pd.read_csv("./data/CSVs/top_wineries.csv")
data4 = pd.read_csv("./data/CSVs/favorites_taste.csv")
data5 = pd.read_csv("./data/CSVs/common_grapes_best_wines.csv")
data6 = pd.read_csv("./data/CSVs/wine_by_taste_filtered.csv")
data7 = pd.read_csv("./data/CSVs/cabernet_by_rating.csv")

# Add custom CSS to center titles using Flexbox
st.markdown("""
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
        align-items: center;

        margin: 0 auto; /* Optional: to remove any default margin */
    }
    </style>
    </style>
    """, unsafe_allow_html=True)

# Main title
st.markdown("<h1 class='centered-title'>Vivino Data Dashboard</h1>", unsafe_allow_html=True)
    
# Center the second title
st.markdown("<h2 class='centered-title'>A comprehensive wine analysis</h2>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Summary")
pages = [
    "Project context📝",
    "Queries Overview🔎",
    "Top 10 wines 🍷",
    "Country to prioritise🌍",
    "Top 3 wineries 🏆",
    "Customer cluster 👥",
    "Most common grapes 📈",
    "Country leaderboard 📊",
    "Top 5 Cabernet Sauvignon🍇",
    "Top Wine by characteristics✨"
    
]   

page = st.sidebar.radio("Go to", pages)

def display_aggrid_table(df, title="Table", height=400):
    st.write(title)
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_side_bar()
    gb.configure_selection('single')
    gridOptions = gb.build()
    AgGrid(df, gridOptions=gridOptions, height=height, fit_columns_on_grid_load=True)


if page == "Project context📝":
    col1, col2, col3 = st.columns(3)
    with col1 : 
        pass
    with col2 : 
        st.image("./assets/vivono_logo.png", width=300)
    with col3 : 
        pass


    st.write("""
    ## Welcome to the Vivino Data Visualization Project!

    This initiative is dedicated to leveraging data insights to drive informed decision-making in the wine industry. Our aim is to use detailed wine data to identify key trends, uncover valuable insights, and provide actionable recommendations. Here's what we strive to achieve:

    **1. Highlight Top Wines** 🍷  
    Identify the best-performing wines based on average ratings and total ratings. This helps spotlight options with the highest customer satisfaction and guides consumers towards top choices.

    **2. Prioritize Marketing Efforts** 🌍  
    Determine which countries present the most potential for investment and marketing. By optimizing our budget allocation, we can target regions with the highest growth opportunities.

    **3. Recognize Leading Wineries** 🏆  
    Award and promote top wineries based on their average ratings. This fosters partnerships with high-quality producers and encourages excellence in winemaking.

    **4. Explore Customer Preferences** 👥  
    Analyze customer taste preferences to align our offerings with popular trends. This ensures we accurately target customer desires and enhance our product lineup.

    **5. Identify Must-Have Wines** 📈  
    Find wines that are globally popular and widely available. Catering to a broad audience helps us meet market demand and satisfy diverse customer tastes.

    **6. Create Leaderboards** 📊  
    Develop visualizations showcasing average wine ratings by country and vintage. These leaderboards provide a clear view of global and temporal trends, aiding in strategic planning and market analysis.
    
    **7. Recommend Top Cabernet Sauvignon Wines** 🍇
    Provide recommendations for the top Cabernet Sauvignon wines based on customer ratings. This helps cater to specific customer preferences and enhance the wine selection process.
    
    **8. Analyze Wine Characteristics** 🍇
    Explore the correlation between wine characteristics and average ratings. By identifying key features that influence ratings, we can enhance our understanding of customer preferences and optimize our product offerings.

    Through this project, we aim to enhance the wine selection process, optimize marketing strategies, and ultimately drive better business decisions. 

    Thank you for joining us on this data-driven journey through the world of wine!
    """)
elif page == "Queries Overview🔎":

    query1 = """
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
            HAVING COUNT(DISTINCT k.name) = 5;"""

    st.header("Overwiew of favorites taste query")
    
    st.write("We detected that a big cluster of customers likes a specific combination of tastes. ")
    
    st.write("The query below retrieves the wines that have the following taste keywords: 'coffee', 'toast', 'green apple', 'cream', 'citrus'. We checked that at least 10 customers confirm these keywords to ensure the accuracy of the selection.")
    st.write("Additionally, we identified an appropriate group name for this cluster : 'Balanced Flavor Profile'")
    
    st.code(query1, language="sql", line_numbers=True)
    
    st.subheader("How did the query was optimized?")
    st.write("Initially, I used an IN clause to filter wines based on specific taste keywords. However, this approach was inefficient because it required scanning the entire wines table. After some research, I discovered that the EXISTS clause is more efficient for this type of query. EXISTS stops processing as soon as it finds a match, unlike IN which requires a full table scan.")

    st.write("EXISTS checks if at least one row meets the specified condition and halts further processing once a match is found. This early exit strategy can significantly improve performance, especially with large datasets. By avoiding a full table scan, EXISTS is generally more efficient than IN in scenarios like this.")

    st.write("I also used the GROUP BY and HAVING clauses to ensure that each wine has all five taste keywords. This approach is more efficient than using a subquery with a COUNT function, as it reduces the number of times the subquery is executed. By grouping the results and filtering them based on the count of distinct taste keywords, I can efficiently identify wines that match all five keywords.")

    st.write("Overall, these optimizations help improve the query's performance and efficiency, making it faster and more reliable for retrieving wines based on specific taste keywords.")
    
    st.subheader("Results")
    st.write("The query returned the following results:")
    display_aggrid_table(data4.head(10), title="Wines with Taste Keywords")

elif page == "Top 10 wines 🍷":
    st.write("We want to highlight 10 wines to increase our sales. Which ones should we choose and why?")
    top_10_wines_df = data1.sort_values(by='total_rating', ascending=False).head(10)
    display_aggrid_table(top_10_wines_df, title="Top 10 Wines")

    st.write(data1.describe())
    
    # Grouping by 'name' and calculating the mean of 'ratings_average' and 'total_rating'
    dataAgg = data1.groupby('name')[['ratings_average', 'total_rating']].mean().reset_index().round(2)

    # Sorting by 'total_rating' in descending order and getting the top 10 wines
    top_10_wines = dataAgg.sort_values(by='total_rating', ascending=False).head(10)

    # Creating a bar chart with 'name' as labels and 'ratings_average' as values
    fig = px.bar(top_10_wines,
                 x='name',  # X-axis should be 'name'
                 y='ratings_average',  # Y-axis should be 'ratings_average'
                 color='total_rating',  # Color by 'total_rating'
                 color_continuous_scale='Reds',  # Blue color scale
                 title='Top 10 Wines by Average Rating count',  # Title
                 labels={'name': 'Wine', 'total_rating': 'Total Rating', 'ratings_average': 'Average Rating'},  # Axis labels
                 text='ratings_average')  # Display average rating on the bars
    
    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text='Wine',  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text='Average Rating',  # Y-axis title
            title_font=dict(size=16),  # Y-axis title font size
            range=[3.5, top_10_wines['ratings_average'].max() + 0.1]  # Adjust Y-axis range
        )
    )

    # Display the bar chart
    st.plotly_chart(fig)


elif page == "Country to prioritise🌍":
    st.write("We have a limited marketing budget for this year. Which country should we prioritize and why?")
    display_aggrid_table(data2.head(16), title="Number of Users by Country")

    st.write(data2.describe())

    # Group by 'name' and calculate the mean 'users_count'
    dataAgg = data2.groupby('name')[['users_count']].mean().reset_index().round(2)

    # Find top 5 countries based on users count
    top_5_countries = dataAgg.sort_values(by='users_count', ascending=False).head(5)

    # Create a bar chart with 'name' on x-axis and 'users_count' on y-axis
    fig = px.bar(top_5_countries,
                 x='name',
                 y='users_count',
                 color='users_count',
                 color_continuous_scale='Reds',  # Blue color scale
                 title='Top 5 Countries with the Highest Number of Users',
                 labels={'name': 'Country', 'users_count': 'Number of Users'},
                 text='users_count')  # Display number of users on the bars

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text='Country',  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text='Number of Users',  # Y-axis title
            title_font=dict(size=16)  # Y-axis title font size
        )
    )

    # Display the chart
    st.plotly_chart(fig)
    # Calculate the total number of users across the top 5 countries

    st.write("""
    📊 The bar chart displays the top 5 countries based on the number of users. Each bar represents a country, with the height showing the total number of users. The color intensity indicates the user count, with darker colors representing higher numbers. This chart helps identify which countries have the highest user engagement, making them prime targets for your marketing efforts.
    """)
    

    # Sort top 5 countries by 'users_count' in descending order to apply the deepest blue to the country with most users
    top_5_countries_sorted = top_5_countries.sort_values(by='users_count', ascending=False)

    # Define a custom color sequence where the first color is deep blue
    color_sequence = ['#8B0000', '#B22222', '#DC143C', '#FF6347', '#FFA07A']
    
    # Create the pie chart
    fig = px.pie(
        top_5_countries_sorted,
        names='name',
        values='users_count',
        title='Distribution of Users Across Top 5 Countries',
        labels={'name': 'Country', 'users_count': 'Number of Users'},
        color_discrete_sequence=color_sequence  # Apply custom color sequence
)

   



    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20)
    )

    st.plotly_chart(fig)

    # Calculate the total number of users across the top 5 countries
    total_users = top_5_countries_sorted['users_count'].sum()

    # Add the explanation with the total number of users
    st.write(f"""
        🥧 The pie chart illustrates the proportion of total users across the top 5 countries. Each slice of the pie represents a country’s share of the total user base. 
        This chart helps visualize how users are distributed among these countries, providing a quick overview of each country’s relative importance in the user landscape.

        **Total Users: {total_users:,}**
    """)


    # Display the top 5 countries data
    display_aggrid_table(top_5_countries, title="Top 5 Countries by Users Count")


elif page == "Top 3 wineries 🏆":
    st.write("We would like to give awards to the best wineries. Here are the top 3 wineries based on their ratings.")
    top_3_wineries_df = data3.sort_values(by='total_rating', ascending=False).head(3)
    display_aggrid_table(top_3_wineries_df, title="Top 3 Wineriesby average rating")

    st.write(data3.describe())

    # Group by 'winery_id' and calculate mean ratings
    dataAgg = data3.groupby('winery_id')[['average_rating', 'total_rating']].mean().reset_index().round(2)

    # Find top 3 wineries based on total rating
    top_3_wineries = dataAgg.sort_values(by='total_rating', ascending=False).head(3)

    # Create a mapping for top 3 winery_ids
    top_3_ids = top_3_wineries['winery_id'].tolist()
    winery_id_labels = {winery_id: f'Winery {winery_id}' for winery_id in top_3_ids}

    # Add a categorical column with labels only for top 3 wineries
    data3['winery_name'] = data3['winery_id'].map(winery_id_labels).fillna('Other Wineries')

    # Filter data to include only top 3 wineries
    filtered_data = data3[data3['winery_name'].isin(winery_id_labels.values())]

    # Group by 'winery_name' and calculate mean ratings
    top_3_wineries_filtered = filtered_data.groupby('winery_name')[['average_rating', 'total_rating']].mean().reset_index().round(2)

    # Create a bar chart with 'winery_name' on x-axis and 'average_rating' on y-axis
    fig = px.bar(
        top_3_wineries_filtered,
        x='winery_name',
        y='average_rating',
        color='total_rating',
        color_continuous_scale='Reds',
        title='Top 3 Wineries with the Highest Average Rating',
        labels={'winery_name': 'Winery Name', 'average_rating': 'Average Rating'},
        text='average_rating'  # Display average rating on the bars
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            tickfont=dict(size=14),
            title_text='Winery Name',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Average Rating',
            title_font=dict(size=16)
        )
    )

    # Adding annotations to highlight each bar
    for index, row in top_3_wineries_filtered.iterrows():
        fig.add_annotation(
            x=row['winery_name'],
            y=row['average_rating'],
            text=f"{row['average_rating']:.2f}",
            showarrow=True,
            arrowhead=2
        )

    st.plotly_chart(fig)

    st.write("""
    📊 The bar chart displays the top 3 wineries based on their average ratings. Each bar represents a winery, with the height of the bar indicating the average rating. The color of the bars reflects the total number of ratings, with darker shades representing higher totals. Annotations on the bars show the exact average ratings. This chart helps in identifying the wineries with the highest average ratings and gives insight into their popularity.
    """)
    


    # Display the top 3 wineries data
    display_aggrid_table(top_3_wineries_filtered, title="Top 3 Wineries by Average Rating")

elif page == "Customer cluster 👥":
    st.write("""
        We detected that a big cluster of customers likes a specific combination of tastes. 
        We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). 
        We would like you to find all the wines that are related to these keywords. 
        Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. 
        Additionally, identify an appropriate group name for this cluster.
    """)
    display_aggrid_table(data4.head(10), title="Wines with Taste Keywords")
    st.write(data4.describe())

    # Filter the data to include only rows where 'taste_keywords' contains the specific keywords
    cluster_data = data4[data4['taste_keywords'].str.contains('coffee|toast|green apple|cream|citrus', case=True)]

    # Further filter the wines to ensure at least 10 users have confirmed those keywords
    cluster_data = cluster_data[cluster_data['wine_ratings_count'] >= 10]

    # Sort the filtered data by 'wine_ratings_count' in descending order
    leader_board = cluster_data.sort_values(by='wine_ratings_count', ascending=False).head(10)

    # Create a bar chart with 'wine_name' on x-axis and 'wine_ratings_count' on y-axis
    fig = px.bar(
        leader_board,
        x='wine_name',
        y='wine_ratings_count',
        color='wine_ratings_count',
        color_continuous_scale='Reds',
        title='Top Wines with Specific Taste Keywords - Rating Count',
        labels={'wine_name': 'Wine Name', 'wine_ratings_count': 'Rating Count'},
        text='wine_ratings_count'  # Display rating count on the bars
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            tickfont=dict(size=14),
            title_text='Wine Name',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Rating Count',
            title_font=dict(size=16)
        )
    )

    st.plotly_chart(fig)

    st.write("""
        📊 The bar chart above displays the top wines that match the specified taste keywords (coffee, toast, green apple, cream, and citrus). 
        Each bar represents a wine, with the height of the bar indicating the number of ratings it has received. 
        This visualization helps identify which wines are most popular among customers who prefer these particular taste profiles.
    """)
    
    fig = px.bar(
        leader_board,
        x='wine_name',
        y='wine_rating_avg',
        color='wine_ratings_count',
        color_continuous_scale='Reds',
        title='Top Wines with Specific Taste Keywords - Average Rating',
        labels={'wine_name': 'Wine Name', 'wine_ratings_count': 'Rating Count'},
        text='wine_rating_avg'  # Display average rating on the bars
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            tickfont=dict(size=14),
            title_text='Wine Name',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Average Rating',
            title_font=dict(size=16)
        )
    )

    st.plotly_chart(fig)

    st.write("""
        ⭐ The second bar chart highlights the average ratings of the top wines that meet the taste keyword criteria. 
        Each bar represents a wine, with the height of the bar showing its average rating. 
        The color intensity indicates the number of ratings received. 
        This chart provides insight into which wines not only align with the specified taste keywords but also have high average ratings, helping to identify top-quality options in this flavor cluster.
    """)



elif page == "Most common grapes 📈":
    st.write("""
        We would like to select wines that are easy to find all over the world. 
        Find the top 3 most common grapes all over the world and for each grape, give us the 5 best rated wines.
    """)
    
    # Display the initial data and its description
    display_aggrid_table(data5.head(20), title="Wines by Common Grapes")
    
    st.write(data5.describe())

    # Group by 'Grape' and calculate the mean 'Wine rating average' and 'Wine ratings count'
    grapeAgg = data5.groupby('Grape')[['Wine rating average', 'Wine ratings count']].mean().reset_index().round(2)

    # Sort the grapes by 'Wine ratings count' in descending order to get the most common ones
    top_grapes = grapeAgg.sort_values(by='Wine ratings count', ascending=False).head(3)

    # Create a bar chart with 'Grape' on x-axis and 'Wine rating average' on y-axis
    fig = px.bar(
        top_grapes,
        x='Grape',
        y='Wine rating average',
        color='Wine ratings count',
        color_continuous_scale='Reds',
        title='Top 3 Most Common Grapes by Average Rating Count',
        labels={'Grape': 'Grape', 'Wine ratings count': 'Rating Count'},
        text='Wine rating average'  # Display average rating on the bars
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            tickfont=dict(size=14),
            title_text='Grape',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Average Rating',
            title_font=dict(size=16),
            range=[4, top_grapes['Wine rating average'].max() + 0.1]  # Adjust Y-axis range
        )
    )

    st.plotly_chart(fig)

    # For each top grape, find the top 5 wines by rating
    top_wines_per_grape = {}
    for grape in top_grapes['Grape']:
        top_wines = data5[data5['Grape'] == grape].sort_values(by='Wine rating average', ascending=False).head(5)
        top_wines_per_grape[grape] = top_wines

    # Display top 5 wines for each grape using AgGrid
    for grape, top_wines in top_wines_per_grape.items():
        st.write(f"**Top 5 Rated Wines for {grape}:**")
        
        # Configure AgGrid options
        gb = GridOptionsBuilder.from_dataframe(top_wines[['Wine name', 'Wine rating average', 'Wine ratings count']])
        gb.configure_pagination(paginationAutoPageSize=True)  # Enable pagination
        gb.configure_side_bar()  # Enable sidebar for options
        gridOptions = gb.build()

        # Display the grid with AgGrid
        AgGrid(top_wines[['Wine name', 'Wine rating average', 'Wine ratings count']], gridOptions=gridOptions)



elif page == "Country leaderboard 📊":

    # Group by 'Country' and calculate the mean 'wine_ratings_avg' and 'users_count'
    countryAgg = data2.groupby('name')[['wine_ratings_avg', 'users_count']].mean().reset_index().round(2)

    # Sort the leaderboard by 'wine_ratings_avg' in descending order
    leader_board = countryAgg.sort_values(by='wine_ratings_avg', ascending=False).head(10)

    # Create a bar chart with 'Country' on y-axis and 'wine_ratings_avg' on x-axis
    fig = px.bar(leader_board,  # Data
                x='name',  # X-axis should be 'wine_ratings_avg'
                y='wine_ratings_avg',  # Y-axis should be 'name' (Country)
                color='users_count',  # Color by 'users_count'
                color_continuous_scale='Reds',
                title='Average Wine Rating by Country',  # Title
                labels={'users_count': 'Number of Users', 'name': 'Country', 'wine_ratings_avg': 'Average Rating'},  # Axis labels  
                text='wine_ratings_avg')  # Display average ratings on the bars

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text='Average Rating',  # X-axis title should be 'Average Rating'
            title_font=dict(size=16)  # X-axis title font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text='Country',  # Y-axis title
            title_font=dict(size=16), # Y-axis title font size
            range=[4, leader_board['wine_ratings_avg'].max() + 0.1]  # Adjust Y-axis range
        ),
    )

    # Display the chart
    st.plotly_chart(fig)

    st.write("""
    🌍 The bar chart displays the average wine ratings for the top 10 countries. Each bar represents a country, with the length of the bar indicating the average rating of wines from that country. The color of the bars shows the number of users, where darker colors represent more users. This visualization helps in identifying which countries have the highest average wine ratings and their popularity.
    """)

    # Create a treemap with 'Country' as the labels, 'users_count' as the size, and 'wine_ratings_avg' as the color
    fig = px.treemap(leader_board,  # Data
                    path=['name'],  # Hierarchical path (in this case, just 'name' for country)
                    values='wine_ratings_avg',  # Size of the blocks (number of users)
                    color='users_count',  # Color of the blocks based on average rating
                    title='Treemap of Average Wine Ratings by Country',  # Title
                    labels={'name': 'Country', 'users_count': 'Number of Users', 'wine_ratings_avg': 'Average Rating'},  # Axis labels  
                    color_continuous_scale='Reds')  # Color scale for average rating

    # Adjust the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
    )

    # Display the chart
    st.plotly_chart(fig)

    st.write("""
    📦 The treemap provides a visual representation of average wine ratings by country. Each block represents a country, with the size of the block indicating the number of users from that country. The color of the blocks represents the average wine rating, with darker shades of blue indicating higher ratings. This helps to quickly identify countries with both high average ratings and a large number of users.
    """)

    # Display the leaderboard data
    display_aggrid_table(leader_board, title="Country Leaderboard")


elif page == "Top 5 Cabernet Sauvignon🍇":
    st.write("""One of our VIP clients enjoys Cabernet Sauvignon and has requested our top 5 recommendations. 
             Which wines would you recommend to him?""")
    
    # Displaying the top 5 Cabernet Sauvignon wines based on rating count
    top_5_cabernet_df = data7.sort_values(by='Wine rating count', ascending=False).head(5)
    display_aggrid_table(top_5_cabernet_df, title="Top 5 Cabernet Sauvignon Wines")

    st.write(data7.describe())

    # Aggregating by 'Country' and calculating the mean of 'Wine rating average' and 'Wine rating count'
    countryAgg = data7.groupby('Country')[['Wine rating average', 'Wine rating count']].mean().reset_index().round(2)

    # Sorting by 'Wine rating average' in descending order to find the top 5 countries
    top_5_countries = countryAgg.sort_values(by='Wine rating average', ascending=False).head(5)

    # Creating a bar chart with 'Country' on x-axis and 'Wine rating average' on y-axis
    fig = px.bar(
        top_5_countries, 
        x='Country', 
        y='Wine rating average', 
        color='Wine rating count',  # Color by rating average
        color_continuous_scale='Reds',  # Blue color scale for average ratings
        title='Top 5 Countries with the Highest Average Rating for Cabernet Sauvignon',
        labels={'Country': 'Country', 'Wine rating average': 'Average Rating'},
        text='Wine rating average'  # Display average ratings on the bars
    )

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text='Country',  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text='Average Rating',  # Y-axis title
            title_font=dict(size=16),  # Y-axis title font size
            range=[4, top_5_countries['Wine rating average'].max() + 0.1]  # Adjust Y-axis range
        )
    )

    # Display the bar chart
    st.plotly_chart(fig)

    st.write("""
    📊 The bar chart displays the top 5 countries with the highest average ratings for Cabernet Sauvignon. Each bar represents a country, with the height indicating the average rating of Cabernet Sauvignon wines from that country. The color of the bars reflects the average rating, with darker shades representing higher ratings. This visualization helps to identify the top-performing countries in terms of Cabernet Sauvignon quality.
    """)

    # Display the top 5 countries data
    display_aggrid_table(top_5_countries, title="Top 5 Countries by Cabernet Sauvignon Rating")

elif page == "Top Wine by characteristics✨":

    st.write("""
        We would like to select the top wine by characteristics.
        Find the top 5 wines that have the highest ratings for the following characteristics:
    """)
    display_aggrid_table(data6.head(5), title="Wines by Taste Characteristics")
    st.write(data6.describe())

    top_wine_by_characteristics = data6.sort_values(by='ratings_count', ascending=False).head(5)

    fig = px.bar(  
        top_wine_by_characteristics,
        x='name',
        y='ratings_average',
        color='ratings_count',
        color_continuous_scale='Reds',
        title='Top 5 Wines by Characteristics and average rating',
        labels={'name': 'Wine Name', 'ratings_count': 'Rating count', 'ratings_average': 'Average Rating'},
        text='ratings_average'
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            tickfont=dict(size=14),
            title_text='Wine Name',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Rating Average',
            title_font=dict(size=16),
            range=[3.5, top_wine_by_characteristics['ratings_average'].max() + 0.5]
        )
    )

    st.plotly_chart(fig)

    st.write("")    

    st.write("""🍷We asked ourself if the rate can be influenced by certain characteristics. 
             Here is the correlation matrix of the wine characteristics.""")
    
    from sklearn.preprocessing import LabelEncoder
    
    # Encode categorical columns
    categorical_columns = data6.select_dtypes(include=['object']).columns
    data6_encoded = data6.copy()

    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        data6_encoded[col] = le.fit_transform(data6_encoded[col])
        label_encoders[col] = le

    # Calculate correlation matrix
    corr_matrix = data6_encoded.corr().round(2)

    # Create a Plotly heatmap
    fig = px.imshow(
        corr_matrix,
        text_auto=True,  # Automatically adds text annotations to the heatmap
        color_continuous_scale='Reds',  # Use a red color scale
        labels=dict(x="Features", y="Features", color="Correlation"),  # Labels for axes and color bar
        title='Correlation Matrix of Wine Characteristics'
    )

    # Adjust the layout for better readability  

    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text='Features',  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text='Features',  # Y-axis title
            title_font=dict(size=16)  # Y-axis title font size
        )
    )
    # Display the heatmap in Streamlit
    st.plotly_chart(fig)
    
    # Encode categorical columns
    categorical_columns = data6.select_dtypes(include=['object']).columns
    data6_encoded = data6.copy()

    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        data6_encoded[col] = le.fit_transform(data6_encoded[col])
        label_encoders[col] = le

    # Calculate correlation with 'ratings_average'
    corr_with_rating = data6_encoded.corr()['ratings_average'].drop('ratings_average').reset_index()
    corr_with_rating.columns = ['Variable', 'Correlation']

    # Sort by absolute correlation
    corr_with_rating['Absolute Correlation'] = corr_with_rating['Correlation'].abs()
    corr_with_rating = corr_with_rating.sort_values(by='Absolute Correlation', ascending=False)

    # Display the top correlated variables in AgGrid
    st.write("### Variables Most Correlated with Average Rating")
    st.write("These are the variables most strongly correlated with the average rating of wines:")

    # Display the top 5 correlated variables
    display_aggrid_table(corr_with_rating[['Variable', 'Correlation']].head(5))




    
    


    

