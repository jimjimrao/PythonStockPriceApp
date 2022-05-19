from numpy import cumsum
import streamlit as st
from bonds import *
import pandas as pd 

def app():
    st.title('Bond Price Calculator')
     ###########
    # sidebar #
    ###########
    fv = float(st.sidebar.text_input('Future Value', 1000))
    c = float(st.sidebar.text_input('Coupon Rate', 0))
    n = int(st.sidebar.text_input('Years Until Maturity', 1))
    m = int(st.sidebar.text_input('Payments Per Year', 1))
    r = float(st.sidebar.text_input('Yield to Maturity', 0))

    cf = cashflow_times(n,m)
    bcf = bond_cashflows(fv,c,n,m)
    df = discount_factors(r,n,m)
    res = [bcf[i - 1] * df[i - 1] for i in cf]
    print(res)

    # print('cashflow:', res)
    # print(cumsum(res))
    pv = bond_price(fv,c,n,m,r)
    st.write('The Present Value of the Bond is: $', pv)
   
    
