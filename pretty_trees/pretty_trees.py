import streamlit as st
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt


@st.cache_data()
def Caretaker (trees_df):
    return trees_df['caretaker'].unique()

st.set_page_config(layout='wide')

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW. The '
         'histogram below is filtered by tree owner.')

trees_df = pd.read_csv('trees.csv')

trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

owners = st.sidebar.multiselect('Tree Owner Filter', Caretaker(trees_df))
graph_color = st.sidebar.color_picker('Graph Colors')

if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1, col2 = st.columns(2)

sns.set_style('darkgrid') # darkgrid, whitegrid, dark, white, tickscd

with col1:
    st.write('Trees by Width')
    fig_1, ax_1 = plt.subplots()
    ax_1 = sns.histplot(trees_df['dbh'], color=graph_color)
    plt.xlabel('Tree Width')
    st.pyplot(fig_1)
with col2:
    st.write('Trees by Age')
    fig_2, ax_2 = plt.subplots()
    ax_2 = sns.histplot(trees_df['age'], color=graph_color)
    plt.xlabel('Age (Days)')
    st.pyplot(fig_2)
