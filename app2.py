import streamlit as st
from bonds import *

def app():
    st.title('Bond Pricing')
     ###########
    # sidebar #
    ###########
    fv = float(st.sidebar.text_input('Future Value', 1000))
    c = float(st.sidebar.text_input('Coupon Rate', 0))
    n = int(st.sidebar.text_input('Years Until Maturity', 5))
    m = int(st.sidebar.text_input('Payments Per Year', 2))
    r = float(st.sidebar.text_input('Yield to Maturity', 0.1))

    pv = bond_price(fv,c,n,m,r)
    st.write('The Present Value of the Bond is: $', pv)
    
