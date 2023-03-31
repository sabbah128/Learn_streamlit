import streamlit as st
import pandas as pd
from bokeh.plotting import figure
import altair as alt


st.title('SF Trees')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
st.subheader('Bokeh Chart')

trees_df = pd.read_csv('trees.csv')

scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)

# **********************************************************************
# Altair
st.title('SF Trees')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')

df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x ='caretaker', y = 'tree_count')
st.altair_chart(fig)