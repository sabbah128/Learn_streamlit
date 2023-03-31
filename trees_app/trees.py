import streamlit as st
import pandas as pd
import numpy as np


st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')

trees_df = pd.read_csv('trees.csv')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
st.write(trees_df.head())
# trees_df = trees_df.sample(n = 10)
# st.map(trees_df)
