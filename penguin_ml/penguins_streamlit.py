import streamlit as st
import pickle


rf_pickle = open('RF_penguin.pickle', 'rb')
map_pickle = open('out_penguin.pickle', 'rb')

rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)

rf_pickle.close()
map_pickle.close()

island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass = st.number_input('Body Mass (g)', min_value=0)

st.write('the user inputs are {}'.format([island, sex, bill_length, 
                                          bill_depth, flipper_length, body_mass]))

island_code = {'Biscoe' : 0, 'Dream' : 1, 'Torgerson' : 2}
sex_code = {'Female' : 0, 'Male' : 1}
