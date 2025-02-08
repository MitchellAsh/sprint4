import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

# Load the dataset
df = pd.read_csv('vehicles_us_data.csv')

# Data Cleaning
df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(subset=['model_year', 'price'], inplace=True)

# App Title
st.header('Vehicles in the US')

# Sidebar for Filters
st.sidebar.title("Filter Options")
vehicle_types = df['type'].dropna().unique()
selected_types = st.sidebar.multiselect("Select vehicle types:", options=vehicle_types, default=vehicle_types)

# Filter the DataFrame
filtered_df = df[df['type'].isin(selected_types)]

# Days Listed Histogram
st.subheader("Days Listed Distribution")
fig_hist = px.histogram(df, x='days_listed', nbins=30, title='Days Listed Distribution')
st.plotly_chart(fig_hist)

# Scatter Plot: Price vs. Model Year
if len(selected_types) > 0:
    st.subheader("Price vs. Model Year by Vehicle Type")
    fig_scatter = px.scatter(
        filtered_df,
        x='model_year',
        y='price',
        color='type',
        title='Price vs. Model Year by Vehicle Type',
        labels={'model_year': 'Model Year', 'price': 'Price ($)'},
        hover_data=['model', 'condition', 'odometer']
    )
    fig_scatter.update_layout(template='plotly_white')
    st.plotly_chart(fig_scatter)
else:
    st.warning("Please select at least one vehicle type to display the scatter plot.")



