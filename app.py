import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

st.title('Vehicles Breakdown App Explorer')

st.markdown("""
            This app gives a fresh look to a database of cars for sale in 2018.
            * **python libraries:** pandas, streamlit, plotly-express
            """)
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed))