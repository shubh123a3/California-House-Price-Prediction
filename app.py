import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('California House Price Predictor')
st.write('This app predicts the house price in California based on the features' )
st.write('The data used for this app is from the California Housing Dataset')
model=pickle.load(open('model.pkl','rb'))
col1, col2 = st.columns(2)
housing_median_age = col1.number_input('Enter the housing median age',min_value=0.0, value=0.0)
total_rooms = col2.number_input('Enter the total rooms',min_value=0.0, value=0.0)
col3, col4 = st.columns(2)
total_bedrooms = col3.number_input('Enter the total bedrooms',min_value=0.0, value=0.0)
median_income = col4.number_input('Enter the median income',min_value=0.0, value=0.0)
ocean_proximity = st.selectbox('Select the ocean proximity',['ONE HOUR', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])
if st.button('Predict'):
       input_df=pd.DataFrame({
              'housing_median_age':[housing_median_age],
              'total_rooms':[total_rooms],
              'total_bedrooms':[total_bedrooms],
              'median_income':[median_income],
              'ocean_proximity':[ocean_proximity]
       })
       result=model.predict(input_df)
       st.header('The predicted house price is:')
       st.header(str(round(result[0],2)))



