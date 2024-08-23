import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv("your_data.csv")

# Main title
st.title("Data Visualization Vivino")

# Display the data
st.subheader("Raw Data")
st.dataframe(data)

# Data visualization
st.subheader("Data Visualization")

# Example: Bar chart
st.subheader("Bar Chart")
bar_data = data.groupby("category")["value"].sum()
plt.bar(bar_data.index, bar_data)
st.pyplot()

# Example: Line chart
st.subheader("Line Chart")
line_data = data.groupby("date")["value"].sum()
plt.plot(line_data.index, line_data)
st.pyplot()