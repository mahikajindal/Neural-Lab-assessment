from datetime import time
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Visualizer')

def findUnique(df):
    return df['Function'].unique()

@st.cache_data
def load(num_of_rows):
    df = pd.read_csv("stats_full_stack_dev.csv", nrows = num_of_rows) 
    return df

st.text_input("Enter number of rows", key="num_rows")

rows = st.session_state.num_rows
rows = int(rows)

df = load(rows)

if df is not None:
    cols = st.columns(2)
    unique = findUnique(df)
    
    for i in range(len(unique)):
        graph_df = df[ df['Function'] == unique[i]][['time_stamp','Time']]
        
        if i % 2 == 0:
            line = px.line(graph_df.sort_values("time_stamp"), x="time_stamp", y="Time", title=unique[i])
            cols[0].plotly_chart(line, use_container_width=True)
            
        if i % 2 == 1:
            line = px.line(graph_df.sort_values("time_stamp"), x="time_stamp", y="Time", title=unique[i])
            cols[1].plotly_chart(line, use_container_width=True)