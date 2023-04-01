import streamlit as st
import pickle


rf_pickle = open('RF_penguin.pickle', 'rb')
map_pickle = open('out_penguin.pickle', 'rb')

rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
st.write(rfc)
st.write(unique_penguin_mapping)
