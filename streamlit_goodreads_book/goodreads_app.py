import streamlit as st
import pandas as pd


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