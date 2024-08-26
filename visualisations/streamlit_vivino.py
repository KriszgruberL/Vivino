import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder

# Load your data
data1 = pd.read_csv("highlight_wine.csv")
data2 = pd.read_csv("limited_budget.csv")
data3 = pd.read_csv("top_wineries.csv")
data7 = pd.read_csv("cabernet_by_rating.csv")

# Main title
st.title("Vivino Data Dashboard: A Comprehensive Wine Analysis")

# Sidebar
st.sidebar.title("Summary")
pages = [
    "Project context",
    "Top 10 wines",
    "Country to prioritise",
    "Top 3 wineries",
    "Customer cluster",
    "Most common grapes",
    "Country leaderboard",
    "Top 5 Cabernet Sauvignon"
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

if page == "Project context":
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

    Through this project, we aim to enhance the wine selection process, optimize marketing strategies, and ultimately drive better business decisions. 

    Thank you for joining us on this data-driven journey through the world of wine!
    """)


elif page == "Top 10 wines":
    st.write("We want to highlight 10 wines to increase our sales. Which ones should we choose and why?")
    top_10_wines_df = data1.sort_values(by='total_rating', ascending=False).head(10)
    display_aggrid_table(top_10_wines_df, title="Top 10 Wines")

    st.write(data1.describe())
    
    # Grouping by 'name' and calculating the mean of 'ratings_average' and 'total_rating'
    dataAgg = data1.groupby('name')[['ratings_average', 'total_rating']].mean().reset_index()

    # Sorting by 'total_rating' in descending order and getting the top 10 wines
    top_10_wines = dataAgg.sort_values(by='total_rating', ascending=False).head(10)

    # Creating a bar chart with 'name' as labels and 'ratings_average' as values
    fig = px.bar(top_10_wines,
                 x='name',  # X-axis should be 'name'
                 y='ratings_average',  # Y-axis should be 'ratings_average'
                 color='total_rating',  # Color by 'total_rating'
                 title='Top 10 Wines by Rating',  # Title
                 labels={'name': 'Wine', 'total_rating': 'Total Rating', 'ratings_average': 'Average Rating'},  # Axis labels
                 text='ratings_average')  # Display average rating on the bars
    
    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        title_font=dict(size=20),  # Increase title font size
    )

    # Display the bar chart
    st.plotly_chart(fig)

    st.write("""
    📊 The bar chart highlights the top 10 wines based on their average ratings. Each bar represents a wine, with the height showing its average rating. The color of the bars indicates the total number of ratings received, where a darker color signifies more ratings. This chart helps to identify which wines are not only highly rated but also popular among consumers.
    """)

    fig = px.scatter(
        top_10_wines,
        x='name',
        y='ratings_average',
        size='total_rating',
        color='ratings_average',
        size_max=60,
        title='Top 10 Wines by Ratings and Total Rating Count',
        labels={'name': 'Wine', 'ratings_average': 'Average Rating', 'total_rating': 'Total Rating'},
        text='ratings_average'
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis_title='Wine',
        yaxis_title='Average Rating'
    )

    # Display the scatter plot
    st.plotly_chart(fig)

    st.write("""
    ✨ The scatter plot provides a visualization of the top 10 wines with respect to their average ratings and the number of total ratings. Each dot represents a wine, with the size of the dot indicating the total number of ratings (popularity) and the color reflecting the average rating. Larger and darker dots signify wines that are highly rated and widely reviewed.
    """)

    fig = px.treemap(
        top_10_wines,
        path=['name'],
        values='total_rating',
        color='ratings_average',
        color_continuous_scale='Blues',
        title='Treemap of Top 10 Wines by Total Rating Count and Average Rating',
        labels={'name': 'Wine', 'total_rating': 'Total Rating', 'ratings_average': 'Average Rating'}
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20)
    )

    # Display the treemap
    st.plotly_chart(fig)

    st.write("""
    📦 The treemap visually represents the top 10 wines where the size of each box corresponds to the total number of ratings each wine has received. The color gradient, ranging from light to dark blue, indicates the average rating of each wine. Darker shades of blue represent higher average ratings. This helps in quickly assessing which wines are both popular and highly rated.
    """)

    fig = px.box(
        top_10_wines,
        x='name',
        y='ratings_average',
        color='name',
        title='Distribution of Ratings for Top 10 Wines',
        labels={'name': 'Wine', 'ratings_average': 'Average Rating'}
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20)
    )

    # Display the box plot
    st.plotly_chart(fig)

    st.write("""
    📈 The box plot provides a detailed view of the rating distribution for each of the top 10 wines. Each box represents the spread of average ratings for a particular wine, showing the median rating, quartiles, and any potential outliers. This plot helps to understand the consistency of ratings among the top wines, highlighting any wines with significant variations in customer feedback.
    """)

    # Display the top 10 wines data
    display_aggrid_table(top_10_wines, title="Top 10 Wines by Rating")


elif page == "Country to prioritise":
    st.write("We have a limited marketing budget for this year. Which country should we prioritize and why?")
    display_aggrid_table(data2.head(16), title="Number of Users by Country")

    st.write(data2.describe())

    # Group by 'name' and calculate the mean 'users_count'
    dataAgg = data2.groupby('name')[['users_count']].mean().reset_index()

    # Find top 5 countries based on users count
    top_5_countries = dataAgg.sort_values(by='users_count', ascending=False).head(5)

    # Create a bar chart with 'name' on x-axis and 'users_count' on y-axis
    fig = px.bar(top_5_countries,
                 x='name',
                 y='users_count',
                 color='users_count',
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

    st.write("""
    📊 The bar chart displays the top 5 countries based on the number of users. Each bar represents a country, with the height showing the total number of users. The color intensity indicates the user count, with darker colors representing higher numbers. This chart helps identify which countries have the highest user engagement, making them prime targets for your marketing efforts.
    """)

    fig = px.scatter(
        top_5_countries,
        x='name',
        y='users_count',
        size='users_count',
        color='users_count',
        size_max=60,
        title='Bubble Chart of Top 5 Countries by Number of Users',
        labels={'name': 'Country', 'users_count': 'Number of Users'}
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20),
        xaxis_title='Country',
        yaxis_title='Number of Users'
    )

    st.plotly_chart(fig)

    st.write("""
    ✨ The scatter plot (bubble chart) shows the top 5 countries with respect to the number of users. Each bubble represents a country, with its size corresponding to the number of users and color reflecting the same metric. Larger and darker bubbles indicate countries with a higher number of users. This visualization highlights which countries have the largest user base and may offer the most potential for marketing impact.
    """)

    fig = px.pie(
        top_5_countries,
        names='name',
        values='users_count',
        title='Proportion of Users by Country',
        labels={'name': 'Country', 'users_count': 'Number of Users'},
        color_discrete_sequence=px.colors.sequential.Blues  # Blue color scale
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20)
    )

    st.plotly_chart(fig)

    st.write("""
    🥧 The pie chart illustrates the proportion of total users across the top 5 countries. Each slice of the pie represents a country’s share of the total user base. This chart helps visualize how users are distributed among these countries, providing a quick overview of each country’s relative importance in the user landscape.
    """)

    fig = px.treemap(
        top_5_countries,
        path=['name'],
        values='users_count',
        color='users_count',
        color_continuous_scale='Blues',
        title='Treemap of Top 5 Countries by Number of Users',
        labels={'name': 'Country', 'users_count': 'Number of Users'}
    )

    fig.update_layout(
        width=900,
        height=600,
        title_font=dict(size=20)
    )

    st.plotly_chart(fig)

    st.write("""
    📦 The treemap provides a hierarchical view of the top 5 countries based on the number of users. Each box’s size represents the number of users, and the color intensity shows the count as well, with darker shades of blue indicating higher numbers. This visualization helps quickly identify which countries dominate the user base and should be prioritized for marketing efforts.
    """)

    # Display the top 5 countries data
    display_aggrid_table(top_5_countries, title="Top 5 Countries by Users Count")


elif page == "Top 3 wineries":
    st.write("We would like to give awards to the best wineries. Here are the top 3 wineries based on their ratings.")
    top_3_wineries_df = data3.sort_values(by='total_rating', ascending=False).head(3)
    display_aggrid_table(top_3_wineries_df, title="Top 3 Wineries")

    st.write(data3.describe())

    # Group by 'winery_id' and calculate mean ratings
    dataAgg = data3.groupby('winery_id')[['average_rating', 'total_rating']].mean().reset_index()

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
    top_3_wineries_filtered = filtered_data.groupby('winery_name')[['average_rating', 'total_rating']].mean().reset_index()

    # Create a bar chart with 'winery_name' on x-axis and 'average_rating' on y-axis
    fig = px.bar(
        top_3_wineries_filtered,
        x='winery_name',
        y='average_rating',
        color='total_rating',
        color_continuous_scale='Blues',
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

    # Create a horizontal bar chart for better readability
    fig = px.bar(
        top_3_wineries_filtered,
        y='winery_name',  # Switch axes for horizontal bar chart
        x='average_rating',
        color='total_rating',
        color_continuous_scale='Blues',
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
            title_text='Average Rating',
            title_font=dict(size=16)
        ),
        yaxis=dict(
            tickfont=dict(size=14),
            title_text='Winery Name',
            title_font=dict(size=16)
        )
    )

    st.plotly_chart(fig)

    st.write("""
    📈 The horizontal bar chart provides a clearer view of the top 3 wineries by their average ratings. By displaying the wineries on the y-axis and their average ratings on the x-axis, this chart emphasizes the differences in ratings more clearly. The color gradient shows the total number of ratings, and the text labels indicate the exact average rating for each winery.
    """)

    # Display the top 3 wineries data
    display_aggrid_table(top_3_wineries_filtered, title="Top 3 Wineries by Average Rating")

elif page == "Customer cluster":
    st.write("""
        We detected that a big cluster of customers likes a specific combination of tastes. 
        We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). 
        We would like you to find all the wines that are related to these keywords. 
        Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. 
        Additionally, identify an appropriate group name for this cluster.
    """)
    # Uncomment and define when data is ready
    # st.dataframe(data4) 
    # st.dataframe(data4.head(5))
    # st.write(data4.describe())

elif page == "Most common grapes":
    st.write("""
        We would like to select wines that are easy to find all over the world. 
        Find the top 3 most common grapes all over the world and for each grape, give us the 5 best rated wines.
    """)
    # Uncomment and define when data is ready
    # st.dataframe(data5) 
    # st.dataframe(data5.head(5))
    # st.write(data5.describe())


elif page == "Country leaderboard":

    # Group by 'Country' and calculate the mean 'wine_ratings_avg' and 'users_count'
    countryAgg = data2.groupby('name')[['wine_ratings_avg', 'users_count']].mean().reset_index()

    # Sort the leaderboard by 'wine_ratings_avg' in descending order
    leader_board = countryAgg.sort_values(by='wine_ratings_avg', ascending=False).head(10)

    # Create a bar chart with 'Country' on y-axis and 'wine_ratings_avg' on x-axis
    fig = px.bar(leader_board,  # Data
                x='name',  # X-axis should be 'wine_ratings_avg'
                y='wine_ratings_avg',  # Y-axis should be 'name' (Country)
                color='users_count',  # Color by 'users_count'
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
            title_font=dict(size=16)  # Y-axis title font size
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
                    values='users_count',  # Size of the blocks (number of users)
                    color='wine_ratings_avg',  # Color of the blocks based on average rating
                    title='Treemap of Average Wine Ratings by Country',  # Title
                    labels={'name': 'Country', 'users_count': 'Number of Users', 'wine_ratings_avg': 'Average Rating'},  # Axis labels  
                    color_continuous_scale='Blues')  # Color scale for average rating

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


elif page == "Top 5 Cabernet Sauvignon":
    st.write("""One of our VIP clients enjoys Cabernet Sauvignon and has requested our top 5 recommendations. 
             Which wines would you recommend to him?""")
    
    # Displaying the top 5 Cabernet Sauvignon wines based on rating count
    top_5_cabernet_df = data7.sort_values(by='Wine rating count', ascending=False).head(5)
    display_aggrid_table(top_5_cabernet_df, title="Top 5 Cabernet Sauvignon Wines")

    st.write(data7.describe())

    # Aggregating by 'Country' and calculating the mean of 'Wine rating average' and 'Wine rating count'
    countryAgg = data7.groupby('Country')[['Wine rating average', 'Wine rating count']].mean().reset_index()

    # Sorting by 'Wine rating average' in descending order to find the top 5 countries
    top_5_countries = countryAgg.sort_values(by='Wine rating average', ascending=False).head(5)

    # Creating a bar chart with 'Country' on x-axis and 'Wine rating average' on y-axis
    fig = px.bar(
        top_5_countries, 
        x='Country', 
        y='Wine rating average', 
        color='Wine rating average',  # Color by rating average
        color_continuous_scale='Blues',  # Blue color scale for average ratings
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
            range=[0, top_5_countries['Wine rating average'].max() + 1]  # Adjust Y-axis range
        )
    )

    # Display the bar chart
    st.plotly_chart(fig)

    st.write("""
    📊 The bar chart displays the top 5 countries with the highest average ratings for Cabernet Sauvignon. Each bar represents a country, with the height indicating the average rating of Cabernet Sauvignon wines from that country. The color of the bars reflects the average rating, with darker shades representing higher ratings. This visualization helps to identify the top-performing countries in terms of Cabernet Sauvignon quality.
    """)

    # Display the top 5 countries data
    display_aggrid_table(top_5_countries, title="Top 5 Countries by Cabernet Sauvignon Rating")
