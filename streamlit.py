import streamlit as st
from streamlit import components

st.set_page_config(layout="wide") # make app wide

page = st.sidebar.selectbox('Select page',
  ['Hinds','Delta Counties', 'Claiborne and Jefferson Counties'])

# st.title('MS Maps')

if (page=='Hinds'):
    st.title('Hinds Census Tracts')
    components.v1.html(open('maps/hinds_tracts_map.html').read(), height=700)

if (page=='Delta Counties'):
    st.title('Delta Counties')
    components.v1.html(open('maps/delta_counties_map.html').read(), height=700)

if (page=='Claiborne and Jefferson Counties'):
    st.title('Claiborne and Jefferson Counties')
    components.v1.html(open('maps/other_counties_map.html').read(), height=700)

