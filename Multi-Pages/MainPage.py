import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    # st.sidebar.markdown("# Main page 🎈")

def page1():
    st.markdown("# Page 1 ❄️")
    # st.sidebar.markdown("# Page 1 ❄️")

def page2():
    st.markdown("# Page 2 🎉")
    # st.sidebar.markdown("# Page 2 🎉")

page_names_to_funcs = {
    'Main Page': main_page,
    'Page 1': page1,
    'Page 2': page2,
}

selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()