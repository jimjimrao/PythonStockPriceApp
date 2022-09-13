from numpy import cumsum
import streamlit as st
from bonds import *
import pandas as pd 

def app():
    st.title('Bond YTM Calculator')
     ###########
    # sidebar #
    ###########
    fv = float(st.sidebar.text_input('Future Value', 1000))
    c = float(st.sidebar.text_input('Coupon Rate', 0.05))
    n = int(st.sidebar.text_input('Years Until Maturity', 5))
    m = int(st.sidebar.text_input('Payments Per Year', 1))
    price = float(st.sidebar.text_input('Present Value', 1100))

 
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    st.write('The Yield to Maturity of the Bond is:', "{:.2%}".format(ytm))
   
    
