import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# st.set_page_config(layout="wide")

lottie_penguin = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json')
st_lottie(lottie_penguin, speed=1.5, width = 800, height = 150)

st.title(":blue[Palmer's Penguins] :sunglasses:")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

col1, col2 = st.columns(2)
with col1:
    selected_x_var = st.selectbox('What do want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 
                               'flipper_length_mm', 'body_mass_g'])

with col2:
    selected_y_var = st.selectbox('What about the y?',
                              ['bill_depth_mm', 'bill_length_mm', 
                               'flipper_length_mm', 'body_mass_g'])

penguin_file = st.file_uploader('Select Your Local PenguinsCSV')

if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')

sns.set_style('darkgrid')

markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var,
y = selected_y_var, hue = 'species', markers = markers, style = 'species')

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)

# st.title('Pandas Profiling of Penguin Dataset')
# penguin_profile = ProfileReport(penguins_df, explorative=True)
# st_profile_report(penguin_profile)