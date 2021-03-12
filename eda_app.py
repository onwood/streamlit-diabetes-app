import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf


def run_eda_app():
    df = pd.read_csv('data/diabetes.csv')
    # X = df.iloc[ : , 3:-2+1]
    
    st.title('사용된 데이터 확인')
    st.write('이 앱은 당뇨병 환자에 대한 내용을 담고 있습니다. 특정 정보를 입력하면 당뇨병 가능성을 도출해낼 수 있는 앱입니다.')
    columns = df.columns
    # print(columns)
    # print(df.dtypes != object)

    st.write('\n')
    st.write('\n')

    number_columns = df.columns[df.dtypes != object]
    multiselected_colums = st.multiselect('컬럼을 선택하세요',number_columns)
    # st.write((df.loc(df['Age'] == df['Age'].max()).to_frame(),))

    if multiselected_colums != []:
        st.dataframe(df[multiselected_colums])    
        
        st.write('\n')
        st.write('\n')

        radio_menu = ['통계치','상관 관계']
        selected_radio = st.radio('선택한 데이터의 가공된 데이터를 확인해보세요', radio_menu)
        
        if selected_radio == '통계치':
            st.dataframe(df[multiselected_colums].describe())

        if selected_radio == '상관 관계':
            if len(multiselected_colums) > 1:
                st.dataframe(df[multiselected_colums].corr())
                
                fig = sns.pairplot(data = df[multiselected_colums])
                st.pyplot(fig)
            
            else:
                st.write('두 가지 이상의 데이터를 선택해주세요')
    
    else:
        st.write('선택한 컬럼이 없습니다.')