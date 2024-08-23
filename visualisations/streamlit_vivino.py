import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
data1 = pd.read_csv("highlight_wine.csv")
data2 = pd.read_csv("limited_budget.csv")
data3 = pd.read_csv("top_wineries.csv")
data7 = pd.read_csv("cabernet_by_rating.csv")

# Main title
st.title("Data Visualization Vivino")

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

if page == "Project context":
   # st.image("assets/Untitled.png", caption='Project Overview Image', use_column_width=True)

    st.write("""

Welcome to the Vivino Data Visualization project! This initiative aims to leverage data insights to drive better decision-making in the wine industry. Our goal is to utilize detailed wine data to identify key trends, uncover valuable insights, and provide actionable recommendations. 

We have gathered comprehensive datasets covering various aspects of the wine market, including ratings, sales, and winery performance. By analyzing this data, we aim to:

- **Highlight Top Wines**: Identify the best-performing wines based on average ratings and total ratings, helping to spotlight options with the highest customer satisfaction.
- **Prioritize Marketing Efforts**: Determine which countries offer the most potential for investment and marketing, optimizing our budget allocation.
- **Recognize Leading Wineries**: Award and promote the top wineries based on their average ratings, fostering partnerships with high-quality producers.
- **Explore Customer Preferences**: Analyze customer taste preferences to align our offerings with popular trends and ensure accuracy in targeting.
- **Identify Must-Have Wines**: Find wines that are globally popular and easily available, catering to a wide audience.
- **Create Leaderboards**: Develop visualizations showing average wine ratings by country and vintage, offering a clear view of global and temporal trends.

Through this project, we aim to enhance the wine selection process, optimize marketing strategies, and ultimately drive better business decisions. 

Thank you for joining us on this data-driven journey through the world of wine!""")

elif page == "Top 10 wines":
    st.write("We want to highlight 10 wines to increase our sales. Which ones should we choose and why?")
    st.dataframe(data1.head(10))
    st.write(data1.describe())

    # Grouping by 'name' and calculating the mean of 'ratings_average' and 'total_rating'
    dataAgg = data1.groupby('name')[['ratings_average', 'total_rating']].mean().reset_index()

    # Sorting by 'total_rating' and getting the top 10 wines
    top_10_wines = dataAgg.sort_values(by='total_rating', ascending=False).head(10)

    # Creating a bar chart with 'name' on x-axis and 'ratings_average' on y-axis
    fig = px.bar(top_10_wines, 
                 x='name', 
                 y='ratings_average', 
                 color='name', 
                 title='Top 10 Wines with the Highest Average Rating')

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        yaxis=dict(
            range=[0, top_10_wines['ratings_average'].max() + 0.5],  # Adjust Y-axis range
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text="Average Rating",  # Y-axis title
            title_font=dict(size=16)  # Y-axis title font size
        ),
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text="Wine Name",  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        title_font=dict(size=20),  # Increase title font size
    )

    # Display the chart
    st.plotly_chart(fig)

    # Display the top 10 wines data
    st.write(top_10_wines)


elif page == "Country to prioritise":
    st.write("We have a limited marketing budget for this year. Which country should we prioritise and why?")
    st.dataframe(data2.head(5))
    st.write(data2.describe())

elif page == "Top 3 wineries":
    st.write("We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?")
    st.dataframe(data3.head(3))
    st.write(data3.describe())

    # Grouping by 'winery_id' and calculating the mean 'average_rating'
    dataAgg = data3.groupby('winery_id')["average_rating, total_rating"].mean().reset_index()

    # Sorting by 'average_rating' in descending order to find the top 3 wineries
    top_3_wineries = dataAgg.sort_values(by='total_rating', ascending=False).head(3)

    # Creating a bar chart with 'winery_id' on x-axis and 'average_rating' on y-axis
    fig = px.bar(top_3_wineries, 
                 x='winery_id', 
                 y='average_rating', 
                 color='winery_id', 
                 title='Top 3 Wineries with the Highest Average Rating')

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        yaxis=dict(
            range=[0, top_3_wineries['average_rating'].max() + 0.5],  # Adjust Y-axis range
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text="Average Rating",  # Y-axis title
            title_font=dict(size=16)  # Y-axis title font size
        ),
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text="Winery ID",  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        title_font=dict(size=20),  # Increase title font size
    )

    # Display the chart
    st.plotly_chart(fig)

    # Display the top 3 wineries data
    st.write(top_3_wineries)


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
    st.write("""
        We would like to create a country leaderboard. 
        Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.
    """)
    # Uncomment and define when data is ready
    # st.dataframe(data6) 
    # st.dataframe(data6.head(5))
    # st.write(data6.describe())

elif page == "Top 5 Cabernet Sauvignon":
    st.write("This is the seventh must have")
    st.dataframe(data7.head(5))
    st.write(data7.describe())

    # Aggregating by 'Country' and calculating the mean of 'Wine rating average'
    countryAgg = data7.groupby('Country')['Wine rating average'].mean().reset_index()

    # Sorting by 'Wine rating average' in descending order to find the top 5 countries
    top_5_countries = countryAgg.sort_values(by='Wine rating average', ascending=False).head(5)

    # Creating a bar chart with 'Country' on x-axis and 'Wine rating average' on y-axis
    fig = px.bar(top_5_countries, 
                 x='Country', 
                 y='Wine rating average', 
                 color='Country', 
                 title='Top 5 Countries with the Highest average rating for Cabernet Sauvignon')

    # Adjusting the layout for better readability
    fig.update_layout(
        width=900,  # Increase width
        height=600,  # Increase height
        yaxis=dict(
            range=[0, top_5_countries['Wine rating average'].max() + 0.5],  # Adjust Y-axis range
            tickfont=dict(size=14),  # Increase Y-axis tick font size
            title_text="Average Rating",  # Y-axis title
            title_font=dict(size=16)  # Y-axis title font size
        ),
        xaxis=dict(
            tickfont=dict(size=14),  # Increase X-axis tick font size
            title_text="Country",  # X-axis title
            title_font=dict(size=16)  # X-axis title font size
        ),
        title_font=dict(size=20),  # Increase title font size
    )

    # Display the chart
    st.plotly_chart(fig)

    # Display the top 5 countries
    st.write(top_5_countries)



