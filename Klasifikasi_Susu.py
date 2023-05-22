import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Kualitas_susu.sav', 'rb'))

st.title('Klasifikasi Kualitas Susu')
kolom1, kolom2 = st.columns(2)

with kolom1:
    pH = st.number_input('Tingkat Keasaman Susu')
    Taste = st.number_input('Rasa Susu (0: Bad, 1: Good)')
    Fat  = st.number_input('Lemak Susu (0: Low, 1: High)')
    Colour = st.number_input('Warna Susu')

with kolom2:
    Temprature = st.number_input('Temperatur Susu')
    Odor = st.number_input('Aroma Susu (0: Bad, 1: Good)')
    Turbidity = st.number_input('Tingkat Kekentalan Susu (0: Low, 1: High)')

prediksi_susu = ''
if st.button('Hasil Prediksi'):
    prediksi_susu = model.predict([[pH, Temprature, Taste, Odor, Fat, Turbidity, Colour]])
    
    if (prediksi_susu [0] == 0):
        prediksi_susu = 'Kualitas Susu Baik'
    elif (prediksi_susu == 1):
        prediksi_susu = 'Kualitas Susu Buruk'
    else:
        prediksi_susu = 'Kualitas Susu Normal'
st.success(prediksi_susu)