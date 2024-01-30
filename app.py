# -*- coding:utf-8 -*-

import streamlit as st 
import seaborn as sns 
import pandas as pd

@st.chche_data
def load_data():
    df=sns.load_dataset('iris')
    return df

def main():
    st.title("Hello World on Streamlit.io")
    iris=load_data()
    
if __name__ == "__main__":
    main()