
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("house_price_model.pkl","rb"))

st.title("House Price Predictor")

OverallQual = st.slider("Overall Quality",1,10,5)
GrLivArea = st.number_input("Living Area",500,5000,1500)
GarageCars = st.slider("Garage Cars",0,4,2)
TotalBsmtSF = st.number_input("Basement Area",0,3000,800)
FullBath = st.slider("Bathrooms",0,4,2)

if st.button("Predict Price"):
    features = np.array([[OverallQual,GrLivArea,GarageCars,TotalBsmtSF,FullBath]])
    prediction = model.predict(features)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
