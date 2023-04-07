import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

file_url = 'https://assets4.lottiefiles.com/temp/lf20_aKAfIn.json'

lottie_book = load_lottieurl(file_url)
st_lottie(lottie_book, speed=1, height=200, key="initial")

st.title('Analyzing Your Goodreads Reading Habits')
st.subheader('A Web App by [Tyler Richards](http://www.tylerjrichards.com)')

'''
Hey there! Welcome to Tyler's Goodreads Analysis App. This app
analyzes (and never stores!)
the books you've read using the popular service Goodreads,
including looking at the distribution
of the age and length of books you've read. Give it a go by
uploading your data below!
'''

goodreads_file = st.file_uploader('Please Import Your GoodreadsData')

if goodreads_file is None:
    books_df = pd.read_csv('goodreads_history.csv')
    st.write("Analyzing Tyler's Goodreads history")
else:
    books_df = pd.read_csv(goodreads_file)
    st.write('Analyzing your Goodreads history')

st.write(books_df.head())

import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

books_df['Year Finished'] = pd.to_datetime(books_df['Date Read']).dt.year
books_per_year = books_df.groupby('Year Finished')['Book Id'].count().reset_index()
books_per_year.columns = ['Year Finished', 'Count']

fig, ax = plt.subplots()

ax = sns.barplot(data=books_per_year, 
                            x='Year Finished', 
                            y='Count')

st.pyplot(fig)

books_df['days_to_finish'] = (
    pd.to_datetime(books_df['Date Read']) - pd.to_datetime(books_df['Date Added'])
    ).dt.days

books_finished_filtered = books_df[
    (books_df['Exclusive Shelf'] == 'read') & (books_df['days_to_finish'] >= 0)]

fig_days_finished = px.histogram(books_finished_filtered, 
                                 x='days_to_finish',
                                 title='Time Between Date Added And DateFinished',
                                 labels={'days_to_finish':'days'})

st.plotly_chart(fig_days_finished)

books_rated = books_df[books_df['My Rating'] != 0]
fig_my_rating = px.histogram(books_rated, x='My Rating', title='User Rating')
st.plotly_chart(fig_my_rating)
fig_avg_rating = px.histogram(books_rated, x='Average Rating', title='Average Goodreads Rating')
st.plotly_chart(fig_avg_rating)