# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:54:56 2023

@author: Ajith
"""

import numpy as np
import pickle
import streamlit as st

loaded_model= pickle.load(open('D:/Work\ML/Deploying ML model/trained_model.sav', 'rb'))

#creating a function for prediction

def MobilePricePrediction(input_data):
    

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshape= input_data_as_numpy_array.reshape(1,-1)
    pred= loaded_model.predict(input_data_reshape)
    print(pred)
    if int(pred[0]) == 0:
      return "The mobile price range is 'LOW COST'"
    elif int(pred[0]) == 1:
      return "The mobile price range is 'MEDIUM COST'"
    elif int(pred[0]) == 2:
      return "The mobile price range is 'HIGH COST'"
    else:
      return "The mobile price range is 'VERY HIGH COST'"
  

def main():
    
    
    #giving a title
    st.title("Mobile Price Prediction Web App")
    
    #getting the input data from user
    #battery_power	int_memory	mobile_wt	n_cores	px_height	px_width	ram	sc_h	sc_w	talk_time	price_range
    battery_power = st.slider('Battery Power in mAh', 501,1998)
    int_memory = st.slider("Internal Memory in GigaBytes", 2,64)
    mobile_wt = st.slider("Mobile Weight ", 80,200)
    n_cores = st.slider("Number of cores of processor", 1,8)
    px_height = st.slider("Pixel Resolution Height", 0,1960)
    px_width = st.slider("Pixel Resolution Width", 500,1998)
    ram = st.slider("Ram in MegaBytes", 256,3998)
    sc_h = st.slider("Screen Height in cm", 5,19)
    sc_w = st.slider("Screen Width in cm", 0,18)
    talk_time = st.slider(" longest time that a single battery charge will last",2,20)
    
    #code for prediction
    price_range=""
    
    #creating a button for prediction
    if st.button("Price Range Test Results"):
        price_range = MobilePricePrediction((battery_power,int_memory,mobile_wt,n_cores,px_height,px_width,ram,sc_h,sc_w,talk_time))
    
    st.success(price_range)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    