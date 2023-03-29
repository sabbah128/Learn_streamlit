import streamlit as st
import pandas as pd


st.title("Palmer's Penguins")
penguins_df = pd.read_csv('penguins.csv', index_col=0)
st.write(penguins_df.head())