import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

st.title('Vehicles Breakdown Explorer')

st.markdown("""
            This app gives a fresh look to a database of cars for sale in 2018.
            * **python libraries:** pandas, streamlit, plotly-express
            """)
st.header('Filter by Make and Color through Sidebar Selections:')
#loading data
def car_data():
    vehicles = pd.read_csv('vehicles_us.csv')
    vehicles['Make'] = vehicles['model'].str.split().str[0]
    vehicles['Model'] = vehicles['model'].str.split().str[~0]
    return vehicles
vehicles = car_data()
#sidebar
st.sidebar.header('User Input Features')
with st.sidebar:
    selected = st.multiselect('Select Make', vehicles['Make'].unique())
    colors = st.multiselect("Select Color", vehicles['paint_color'].unique())
    

    fil_vehicles= vehicles[
    (vehicles['Make'].isin(selected)) & 
    (vehicles['paint_color'].isin(colors))
    ]
st.dataframe(fil_vehicles)

st.header('Brouse through:')
#checkbox to show full dataframe
if st.checkbox('Full Dataframe'):
    vehicles
#checkbox to show scatterplots
if st.checkbox('Scatterplots'):
    #scatterplots
    st.header('Scatterplots')
    fig = px.scatter(vehicles, x='odometer', y= 'price', title= 'Price vs Odometer')
    st.plotly_chart(fig)

    fig = px.scatter(vehicles, x="model_year", y="odometer", size="price", color="model",
           hover_name="condition", log_x=True, size_max=60, title='Odometer vs Model Year by Price')
    st.write(fig)
#useful histograms and charts for the dataframe
if st.checkbox('Histograms'):
    st.header('Histograms')

    fig = px.histogram(vehicles, x='price', color= 'Make', title='Car Prices')
    st.plotly_chart(fig)

    fig = px.histogram(vehicles, x='Make', color= 'model_year', title='Car Make')
    st.plotly_chart(fig)

    fig = px.histogram(vehicles, x='Model', title='Car Model')
    st.plotly_chart(fig)

    fig = px.histogram(vehicles, x='odometer', color= 'Make', title='Car Odometer')
    st.plotly_chart(fig)

st.header('Price Distribution Comparision')
