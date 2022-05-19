#app.py
import app1
import app2
import app3
import streamlit as st
PAGES = {
    "Stocks": app1,
    "Bond Price Calculator": app2,
    "Bond YTM Calculator" : app3
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()