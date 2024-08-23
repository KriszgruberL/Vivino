import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
pages = ["Project context","Must have 1", "Must have 2", "Must have 3", "Must have 4", "Must have 5", "Must have 6", "Top 5 Cabernet Sauvignon"]   

page = st.sidebar.radio("Go to", pages)

if page == "Project context":
    st.write("This is the project context")

elif page == "Must have 1":
    st.write("Top 10 wines to increase sales")
    st.dataframe(data1.head(10))
    st.write(data1.describe())

    # Grouping by 'name' and calculating the mean of 'ratings_average' and 'total_rating'
    dataAgg = data1.groupby('name')[['ratings_average', 'total_rating']].mean().reset_index()

    # Sorting by 'ratings_average' and getting the top 10 wines
    top_10_wines = dataAgg.sort_values(by='ratings_average', ascending=False).head(10)

    # Creating a bar chart with 'name' on x-axis and 'ratings_average' on y-axis
    fig = px.bar(top_10_wines, x='name', y='ratings_average', color='name', title='Top 10 Wines with the Highest Average Rating')

    # Display the chart
    st.plotly_chart(fig)

    # Display the top 10 wines data
    st.write(top_10_wines)

elif page == "Must have 2":
    st.write("Country to prioritise")
    st.dataframe(data2.head(5))
    st.write(data2.describe())

elif page == "Must have 3":
    st.write("Top 3 wineries")
    st.dataframe(data3.head(3))
    st.write(data3.describe())

    # Grouping by 'winery_id' and getting the mean 'average_rating'
    dataAgg = data3.groupby('winery_id')["average_rating"].mean().reset_index()

    # Sorting by 'average_rating' in descending order to find the top 3 wineries
    top_3_wineries = dataAgg.sort_values(by='average_rating', ascending=False).head(3)

    # Creating a bar chart to visualize the top 3 wineries
    fig = px.bar(top_3_wineries, x='winery_id', y='average_rating', color='winery_id', title='Top 3 Wineries with the Highest Average Rating')

    # Displaying the chart
    st.plotly_chart(fig)

    # Displaying the top 3 wineries data
    st.write(top_3_wineries)



elif page == "Must have 4":
    st.write("This is the fourth must have")
    # Uncomment and define when data is ready
    # st.dataframe(data4) 
    # st.dataframe(data4.head(5))
    # st.write(data4.describe())

elif page == "Must have 5":
    st.write("This is the fifth must have")
    # Uncomment and define when data is ready
    # st.dataframe(data5) 
    # st.dataframe(data5.head(5))
    # st.write(data5.describe())

elif page == "Must have 6":
    st.write("This is the sixth must have")
    # Uncomment and define when data is ready
    # st.dataframe(data6) 
    # st.dataframe(data6.head(5))
    # st.write(data6.describe())

elif page == "Top 5 Cabernet Sauvignon":
    st.write("This is the seventh must have")
    st.dataframe(data7) 
    st.dataframe(data7.head(5))
    st.write(data7.describe())

    # Grouping by 'Wine rating average' and getting the most common 'Country'
    dataAgg = data7.groupby('Wine rating average')['Country'].agg(lambda x: x.mode()[0]).reset_index()

    # Aggregating by 'Country' and calculating the mean of 'Wine rating average'
    countryAgg = data7.groupby('Country')['Wine rating average'].mean().reset_index()

    # Sorting by 'Wine rating average' in descending order to find the top 5 countries
    top_5_countries = countryAgg.sort_values(by='Wine rating average', ascending=False).head(5)

    fig = px.bar(top_5_countries, x='Country', y='Wine rating average', color='Country', title='Top 5 countries with the highest average wine rating')
    st.plotly_chart(fig)

    # Display the top 5 countries
    st.write(top_5_countries)

# Sections 4, 5, and 6 are not yet defined

