import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

df = pd.read_csv('vehicles_us_data.csv')

st.header('Vehicles in the US')

fig = px.histogram(df, x='days_listed', nbins=30, title='Days Listed Distribution')

st.title('Days Listed Distribution')
st.write('This is a histogram of the number of days each vehicle was listed for sale.')
st.plotly_chart(fig)

st.title('Price vs. Model Year by Vehicle Type')
st.write('This scatter plot shows the relationship between the price and model year of vehicles, colored by vehicle type.')

# Unique vehicle types
vehicle_types = df['type'].unique()

# Create checkboxes for each vehicle type
selected_types = []
for vehicle_type in vehicle_types:
    if st.checkbox(vehicle_type, value=True):  # Default is checked
        selected_types.append(vehicle_type)

# Filter the DataFrame based on selected types
filtered_df = df[df['type'].isin(selected_types)]

# Create the scatter plot based on the filtered DataFrame
fig = px.scatter(
    filtered_df,
    x='model_year',
    y='price',
    color='type',
    title='Price vs. Model Year by Vehicle Type',
    labels={
        'model_year': 'Model Year',
        'price': 'Price ($)'
    },
    hover_data=['model', 'condition', 'odometer']
)
fig.update_layout(template='plotly_white')

st.plotly_chart(fig)



