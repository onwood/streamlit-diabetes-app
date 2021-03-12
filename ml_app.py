import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
# from xgboost import XGBClassifier
import joblib
from tensorflow.keras import Model
from sklearn.ensemble import RandomForestClassifier

def run_ml_app():
    st.title('당뇨병 예측')
    st.write('출산 횟수(Pregnancies), 포도당(Glucose), 혈압(Blood Pressure), 피부 두께(SkinThickness), 인슐린(Insulin), BMI, 당뇨병 혈통 기능(Diabetes Pedigree Function), 나이(Age)를 직접 입력해서 당뇨병 가능성을 예측해보세요.')
    
    preg= st.number_input('출산 횟수(Pregnancies)', 0)
    glucose = st.number_input('포도당(Glucose)', 0.0)
    bp = st.number_input('혈압(Blood Pressure)', 0.0)
    skin = st.number_input('피부 두께(SkinThickness)',0.0)
    insulin = st.number_input('인슐린(Insulin)', 0.0)
    bmi = st.number_input('BMI', 0.0)
    dpf = st.number_input('당뇨병 혈통 기능(Diabetes Pedigree Function)', 0.0)
    age = st.number_input('나이(Age)', 0)

    input_data_list=[preg, glucose, bp, skin, insulin, bmi, dpf, age]

    model = joblib.load('data/GS_best_estimator.pkl')

    new_data = np.array(input_data_list).reshape(1,-1)  
    new_data_pred = model.predict(new_data)

    print(new_data_pred)
    if st.button('결과'):
        if new_data_pred == 0:
            st.write('당뇨병을 의심하지 않아도 됩니다')
        if new_data_pred == 1:
            st.write('당뇨병을 의심해보세요')