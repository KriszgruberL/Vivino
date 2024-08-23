import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load your data
data1 = pd.read_csv("your_data.csv")
data2 = pd.read_csv("your_data.csv")
data3 = pd.read_csv("your_data.csv")
data4 = pd.read_csv("your_data.csv")
data5 = pd.read_csv("your_data.csv")
data6 = pd.read_csv("your_data.csv")
data7 = pd.read_csv("cabernet_by_rating.csv")


# Main title
st.title("Data Visualization Vivino")

# Sidebar
st.sidebar.title("Summary")
pages = ["Project context","Must have 1", "Must have 2", "Must have 3", "Must have 4", "Must have 5", "Must have 6", "Must have 7"]   

page = st.sidebar.radio("Go to", pages)

if page == "Project context":
    st.write("This is the project context")

elif page == "Must have 1":
    st.write("This is the first must have")
    st.dataframe(data1) 
    st.dataframe(data1.head(5))
    st.write(data1.describe())

elif page == "Must have 2":
    st.write("This is the second must have")
    st.dataframe(data2) 
    st.dataframe(data2.head(5))
    st.write(data2.describe())

elif page == "Must have 3":
    st.write("This is the third must have")
    st.dataframe(data3) 
    st.dataframe(data3.head(5))
    st.write(data3.describe())

elif page == "Must have 4":
    st.write("This is the fourth must have")
    st.dataframe(data4) 
    st.dataframe(data4.head(5))
    st.write(data4.describe())

elif page == "Must have 5":
    st.write("This is the fifth must have")
    st.dataframe(data5) 
    st.dataframe(data5.head(5))
    st.write(data5.describe())

elif page == "Must have 6":
    st.write("This is the sixth must have")
    st.dataframe(data6) 
    st.dataframe(data6.head(5))
    st.write(data6.describe())

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
    print(top_5_countries)



