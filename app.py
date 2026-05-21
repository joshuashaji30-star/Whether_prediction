import streamlit as st
import pandas as pd

# Title
st.title("Weather Prediction App")

# Read CSV file
df = pd.read_csv("data/weather_data.csv")

# Show dataframe
st.subheader("Weather Data")
st.dataframe(df)

# Temperature Chart
st.subheader("Temperature Chart")
st.line_chart(df["temperature_2m"])

# Rain Chart
st.subheader("Rain Chart")
st.bar_chart(df["rain"])