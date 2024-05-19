import streamlit as st 
import numpy as np
import pickle

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()


st.title('Heart Disease Prediction')
st.write('Enter the following information')

st.image(r"C:\Users\ali\Downloads\pngegg2.png", width=190, use_column_width=False)

age = st.number_input('Age', 0, 120)

st.sidebar.image(r"C:\Users\ali\Downloads\serious-female-doctor-with-stethoscope.png")

anaemia = st.number_input('anaemia', 0, 1)

creatinine_phosphokinase = st.number_input('creatinine_phosphokinase', min_value=0, max_value=5000)

diabetes = st.number_input('diabetes', min_value=0, max_value=1)

ejection_fraction = st.number_input('ejection_fraction', min_value=0, max_value=120)

high_blood_pressure = st.number_input('high_blood_pressure', min_value=0, max_value=1)

platelets = st.number_input('platelets', min_value=0, max_value=5000000)

serum_creatinine = st.number_input('serum_creatinine', min_value=0, max_value=120)

serum_sodium = st.number_input('serum_sodium', min_value=0, max_value=200)

sex = st.number_input('sex', 0, 1)

smoking = st.number_input('smoking', min_value=0, max_value=1)

time = st.number_input('time', min_value=0, max_value=1000)

st.sidebar.title(':memo: Author')

st.sidebar.subheader('Mohammad Ali')

st.sidebar.title('Connect :link:')

st.sidebar.link_button('Linkdin :large_blue_diamond:', url='https://www.linkedin.com/in/mohdali02/')
st.sidebar.link_button('Git-hub :black_large_square:', url='github.com/Mohd-Ali2')


input_data = (age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time)

if st.button('Predict'):
    st.spinner('wait')
    np_arr = np.asarray(input_data)
    rehsape = np_arr.reshape(1, -1)
    prediction = model.predict(rehsape)
    if prediction == 1:
        st.warning('Might be in Danger')
    else:
        st.success('Might not be in Danger')