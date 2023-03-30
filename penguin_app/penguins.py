import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from random import shuffle


st.title('Palmer\'s Penguins')

penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())

species_list = list(penguins_df['species'].unique())

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
# selected_species = st.selectbox('What species would you like to visualize?', species_list)

# selected_var = [n for n in penguins_df.columns 
#                 if n not in ['species', 'island', 'sex', 'year']]
# selected_x_var = st.selectbox('What do want the x variable to be?', selected_var)
# selected_y_var = st.selectbox('What about the y?', selected_var)

selected_x_var = st.selectbox('What do want the x variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 
                               'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', 
                              ['bill_depth_mm', 'bill_length_mm', 
                               'flipper_length_mm', 'body_mass_g'])
# penguins_df = penguins_df[penguins_df['species'] == selected_species]

sns.set_style('darkgrid')
markers = {'Adelie': 'X', 'Gentoo': 's', 'Chinstrap':'o'}

fig, ax = plt.subplots()

ax = sns.scatterplot(data = penguins_df, 
                     x = selected_x_var, 
                     y = selected_y_var, 
                     hue = 'species',
                     markers = markers,
                     style = 'species')

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)

# plt.title(f'Scatterplot of {selected_species} Penguins')
st.pyplot(fig)