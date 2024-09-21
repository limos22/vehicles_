import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Vehicles Breakdown App')

st.markdown("""
            This app...
            """)

vehicles= pd.read_csv('vehicles_us.csv')