import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests


@st.cache_data()
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.sidebar.title('Answering the Questions.')
n_q = st.sidebar.radio('Select number of questions:', ['Q1', 'Q2'])

if n_q == 'Q1':
    lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_jhu1lqdz.json')
    st_lottie(lottie_airplane, speed=1, height=200, key="initial")

    st.title('Major US Airline Job Application')
    st.write('by H.KianAra')
    st.subheader('Question 1: Airport Distance')

    '''
    The first exercise asks us 'Given the table of airports and
    locations (in latitude and longitude) below,
    write a function that takes an airport code as input and
    returns the airports listed from nearest to furthest from
    the input airport.' There are three steps here:

    1. Load Data
    2. Implement Distance Algorithm
    3. Apply distance formula across all airports other than the input
    4. Return sorted list of airports Distance
    '''

    with st.echo():
        airport_distance_df = pd.read_csv('airport_location.csv')

    '''
    From some quick googling, I found that the haversine distance
    is a good approximation for distance. At least good enough to get
    the distance between airports! Haversine distances can be off by up
    to .5%, because the earth is not actually a sphere. It looks like the
    latitudes and longitudes are in degrees, so I'll make sure to have a way
    to account for that as well. The haversine distance formula is labeled
    below, followed by an implementation in python
    '''

    st.image('haversine.png')

    with st.echo():
        from math import radians, sin, cos, atan2, sqrt

        def haversine_distance(long1, lat1, long2, lat2, degrees=False):
            if degrees == True:
                long1 = radians(long1)
                lat1 = radians(lat1)
                long2 = radians(long2)
                lat2 = radians(lat2)
                a = sin((lat2-lat1) / 2)**2 + cos(lat1) * cos(lat2) * sin((long2-long1) / 2)**2
                c = 2*atan2(sqrt(a), sqrt(1-a))
                distance = 6371 * c
                return distance
            return None

    '''
    Now, we need to test out our function! The
    distance between the default points is
    18,986 kilometers, but feel free to try out
    your own points of interest.
    '''

    col1, col2 = st.columns(2)
    with col1:
        long1 = st.number_input('Longitude 1', value = 2.55)
        long2 = st.number_input('Longitude 2', value = 172.00)
    with col2:
        lat1 = st.number_input('Latitude 1', value = 49.01) 
        lat2 = st.number_input('Latitude 2', value = -43.48)

    test_distance = haversine_distance(long1 = long1, 
                                    long2 = long2, 
                                    lat1 = lat1, 
                                    lat2 = lat2, 
                                    degrees=True)

    st.write(f'Your distance is: :blue[**{int(test_distance)} km**]')

    '''
    We have the Haversine distance implemented, and we also have
    proven to ourselves that it works reasonably well.
    Our next step is to implement this in a function!
    '''

    with st.echo():
        def get_distance_list(airport_dataframe, airport_code):
            df = airport_dataframe.copy()
            row = df[df.loc[:,'Airport Code'] == airport_code]
            lat = row['Lat']
            long = row['Long']
            df = df[df['Airport Code'] != airport_code]
            df['Distance'] = df.apply(lambda x: haversine_distance(lat1=lat, 
                                                                long1=long, 
                                                                lat2 = x.Lat, 
                                                                long2 = x.Long, 
                                                                degrees=True), axis=1)
            return(df.sort_values(by='Distance').reset_index()['Airport Code'])

    '''
    To use this function, select an airport from the airports
    provided in the dataframe and this application will find 
    the distance between each one, and return a list of the 
    airports closest to furthest.
    '''

    selected_airport = st.selectbox('Airport Code', airport_distance_df['Airport Code'])

    distance_airports = get_distance_list(airport_distance_df, selected_airport)

    st.write(f'Your closest airports in order are {list(distance_airports)}')

    '''
    This all seems to work just fine! There are a few ways I would
    improve this if I was working on this for a longer period of time.

    1. I would implement the [Vincenty Distance](https://en.wikipedia.org/wiki/Vincenty%27s_formulae)
    instead of the Haversine distance, which is much more accurate
    but cumbersome to implement.

    2. I would vectorize this function and make it more efficient
    overall. Because this dataset is only 7 rows long, it wasn't
    particularly important, but if this was a crucial function that 
    was run in production we would want to vectorize it for speed.
    '''
    st.subheader('Completed first question.')

else:
    # answering Q2
    st.title('Question 2:')
    st.write('by H.KianAra')
    st.subheader('Question 2:')
    st.subheader('Completed second question.')
