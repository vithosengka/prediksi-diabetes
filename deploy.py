import pickle
import streamlit as st
import os

# Define the path to the model file
model_file = 'diabetes_model.sav'
model_path = os.path.join(os.path.dirname(__file__), model_file)

# Check if the model file exists
if not os.path.exists(model_path):
    st.error(f"Model file not found: {model_path}")
    st.stop()

# Load the model
with open(model_path, 'rb') as file:
    diabetes_model = pickle.load(file)

# The rest of your code follows...


# Web title
st.title('Cek Prediksi Diabetes')

# User inputs
Pregnancies = st.text_input('Input nilai Pregnancies')
Glucose = st.text_input('Input nilai Glucose')
BloodPressure = st.text_input('Input nilai Blood Pressure')
SkinThickness = st.text_input('Input nilai Skin Thickness')
Insulin = st.text_input('Input nilai Insulin')
BMI = st.text_input('Input nilai BMI')
DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')
AGE = st.text_input('Input nilai AGE')

# Predict button
if st.button('Test Prediksi Diabetes'):
    try:
        # Ensure all inputs are converted to float
        input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), 
                      float(SkinThickness), float(Insulin), float(BMI), 
                      float(DiabetesPedigreeFunction), float(AGE)]

        # Prediction
        diab_prediction = diabetes_model.predict([input_data])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'

        st.success(diab_diagnosis)
    except ValueError:
        st.error("Pastikan semua input berupa angka.")

